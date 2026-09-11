# Перевірка коду з лекції про LangGraph (email-агент підтримки) з фейковою
# моделлю, без викликів API. Висновки: DECISIONS_LOG.md, пункт 10.
#
# Вузли скопійовано з лекції як є, змінено тільки дві речі:
#   - llm: фейкова модель замість ChatOpenAI(model="gpt-4");
#   - search_documentation: захардкоджений список винесено в real_search(),
#     щоб зімітувати падіння справжнього пошуку (сценарій C).
# Баги лекції залишено навмисно, кожен позначено коментарем «БАГ».
#
# Запуск (перевірено 11.09.2026 на langgraph 1.2.11, Python 3.14):
#   PYTHONUTF8=1 py langgraph_email_agent_probe.py
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command, RetryPolicy
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage


class EmailClassification(TypedDict):
    intent: Literal["question", "bug", "billing", "feature", "complex"]
    urgency: Literal["low", "medium", "high", "critical"]
    topic: str
    summary: str


class EmailAgentState(TypedDict):
    email_content: str
    sender_email: str
    email_id: str
    classification: EmailClassification | None
    search_results: list[str] | None
    customer_history: dict | None  # БАГ: жоден вузол це поле не заповнює
    draft_response: str | None
    messages: list[str] | None


# --- фейкова модель замість ChatOpenAI ---
FAKE_CLASS: dict = {}
PROMPTS: list[str] = []
SEARCH_FAILS = False
SENT: list[str] = []


class _Resp:
    def __init__(self, content):
        self.content = content


class _Structured:
    def invoke(self, prompt):
        return dict(FAKE_CLASS)


class FakeLLM:
    def with_structured_output(self, schema):
        return _Structured()

    def invoke(self, prompt):
        PROMPTS.append(prompt)
        return _Resp("Draft reply text")


llm = FakeLLM()


def real_search(query):
    if SEARCH_FAILS:
        raise ConnectionError("KB timeout")
    return [
        "Скинути пароль через Налаштування > Безпека > Змінити пароль",
        "Пароль має бути щонайменше 12 символів",
    ]


# --- вузли з лекції ---
def read_email(state: EmailAgentState) -> dict:
    return {"messages": [HumanMessage(content=f"Обробка email: {state['email_content']}")]}


def classify_intent(state: EmailAgentState) -> Command[Literal["search_documentation", "human_review", "draft_response", "bug_tracking"]]:
    structured_llm = llm.with_structured_output(EmailClassification)
    classification = structured_llm.invoke("...")
    # БАГ (архітектурний): billing іде на human_review раніше, ніж з'явилась чернетка
    if classification['intent'] == 'billing' or classification['urgency'] == 'critical':
        goto = "human_review"
    elif classification['intent'] in ['question', 'feature']:
        goto = "search_documentation"
    elif classification['intent'] == 'bug':
        goto = "bug_tracking"
    else:
        goto = "draft_response"
    return Command(update={"classification": classification}, goto=goto)


def search_documentation(state: EmailAgentState) -> Command[Literal["draft_response"]]:
    classification = state.get('classification', {})
    query = f"{classification.get('intent', '')} {classification.get('topic', '')}"
    try:
        search_results = real_search(query)  # у лекції тут захардкоджений список
    except SearchAPIError as e:  # noqa: F821  БАГ: клас ніде не визначено
        search_results = [f"Пошук тимчасово недоступний: {str(e)}"]
    return Command(update={"search_results": search_results}, goto="draft_response")


def bug_tracking(state: EmailAgentState) -> Command[Literal["draft_response"]]:
    ticket_id = "BUG-12345"
    return Command(
        # БАГ: current_step немає в схемі стану, оновлення мовчки губиться
        update={"search_results": [f"Створено тикет багу {ticket_id}"], "current_step": "bug_tracked"},
        goto="draft_response",
    )


def draft_response(state: EmailAgentState) -> Command[Literal["human_review", "send_reply"]]:
    classification = state.get('classification', {})
    context_sections = []
    if state.get('search_results'):
        # БАГ: "\\n" дає буквальні символи \n у промпті (артефакт копіювання)
        formatted_docs = "\\n".join([f"- {doc}" for doc in state['search_results']])
        context_sections.append(f"Відповідна документація:\\n{formatted_docs}")
    if state.get('customer_history'):
        context_sections.append(f"Рівень клієнта: {state['customer_history'].get('tier', 'стандартний')}")
    draft_prompt = f"""
    Склади відповідь на цей email клієнта:
    {state['email_content']}
    {chr(10).join(context_sections)}
    """
    response = llm.invoke(draft_prompt)
    # БАГ (архітектурний): чи побачить відповідь людина, вирішує класифікація моделі
    needs_review = (
        classification.get('urgency') in ['high', 'critical'] or
        classification.get('intent') == 'complex'
    )
    goto = "human_review" if needs_review else "send_reply"
    return Command(update={"draft_response": response.content}, goto=goto)


def human_review(state: EmailAgentState) -> Command[Literal["send_reply", END]]:
    classification = state.get('classification', {})
    human_decision = interrupt({
        "draft_response": state.get('draft_response', ''),
        "intent": classification.get('intent'),
    })
    if human_decision.get("approved"):
        return Command(
            update={"draft_response": human_decision.get("edited_response", state.get('draft_response', ''))},
            goto="send_reply",
        )
    return Command(update={}, goto=END)


def send_reply(state: EmailAgentState) -> dict:
    SENT.append(state['draft_response'])
    return {}


def build():
    wf = StateGraph(EmailAgentState)
    wf.add_node("read_email", read_email)
    wf.add_node("classify_intent", classify_intent)
    wf.add_node("search_documentation", search_documentation, retry_policy=RetryPolicy(max_attempts=3))
    wf.add_node("bug_tracking", bug_tracking)
    wf.add_node("draft_response", draft_response)
    wf.add_node("human_review", human_review)
    wf.add_node("send_reply", send_reply)
    wf.add_edge(START, "read_email")
    wf.add_edge("read_email", "classify_intent")
    wf.add_edge("send_reply", END)
    return wf.compile(checkpointer=MemorySaver())


def base_state(text):
    return {"email_content": text, "sender_email": "c@example.com", "email_id": "e1", "messages": []}


def run(title, cls, text, thread, search_fails=False):
    global FAKE_CLASS, SEARCH_FAILS
    FAKE_CLASS, SEARCH_FAILS = cls, search_fails
    SENT.clear()
    PROMPTS.clear()
    app = build()
    print(f"\n=== {title} ===")
    try:
        result = app.invoke(base_state(text), {"configurable": {"thread_id": thread}})
    except Exception as e:
        print(f"invoke упав: {type(e).__name__}: {e}")
        return None, None
    print("ключі результату:", sorted(result.keys()))
    print("зупинився на human_review:", "__interrupt__" in result)
    print("надіслано без людини:", SENT)
    return app, result


if __name__ == "__main__":
    # A. Сценарій з тесту лекції: подвійне списання
    app, result = run("A. billing, як у тесті лекції",
                      {"intent": "billing", "urgency": "high", "topic": "t", "summary": "s"},
                      "З мене двічі стягнули плату за підписку! Це терміново!", "a")
    try:
        print(f"Чернетка готова до перегляду: {result['draft_response'][:100]}...")
    except Exception as e:
        print(f"рядок print з лекції упав: {type(e).__name__}: {e}")

    # B. Баг, низька терміновість
    app, result = run("B. bug, low", {"intent": "bug", "urgency": "low", "topic": "export", "summary": "s"},
                      "Експорт у PDF падає", "b")
    if app:
        st = app.get_state({"configurable": {"thread_id": "b"}}).values
        print("current_step у стані:", "current_step" in st)
        print("буквальний \\n у промпті:", any("\\n" in p for p in PROMPTS))

    # C. Питання, справжній пошук упав
    run("C. question, low, пошук недоступний", {"intent": "question", "urgency": "low", "topic": "pwd", "summary": "s"},
        "Як скинути пароль?", "c", search_fails=True)

    # D. Питання, все працює
    run("D. question, low", {"intent": "question", "urgency": "low", "topic": "pwd", "summary": "s"},
        "Як скинути пароль?", "d")
