import numpy as np
import streamlit as st
from google import genai
from google.genai import types
from sklearn.neighbors import NearestNeighbors

st.set_page_config(
    page_title="StudyMate — Освітній асистент",
    page_icon="📚",
    layout="wide",
)

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

CHAT_MODEL = "gemini-3.5-flash-lite"
EMBEDDING_MODEL = "gemini-embedding-001"

# Поріг 0.55 підібраний емпірично під embeddings OpenAI (ДЗ8). Embedding-простір
# Gemini інший — після першого реального тестування треба перевірити, чи поріг
# ще адекватний, а не переносити його сліпо.
SIMILARITY_THRESHOLD = 0.55

# --- Довідник формул (математика: квадратні рівняння, прогресії, геометрія) ---
FORMULAS = [
    {"name": "Дискримінант квадратного рівняння", "formula": "D = b² − 4ac",
     "conditions": "Рівняння ax² + bx + c = 0, потрібно визначити кількість коренів",
     "example": "2x² − 3x − 5 = 0 → D = 9 + 40 = 49"},
    {"name": "Корені квадратного рівняння через дискримінант", "formula": "x = (−b ± √D) / (2a)",
     "conditions": "Застосовується, коли D ≥ 0",
     "example": "D = 49 → x1 = 2.5, x2 = −1"},
    {"name": "Неповне квадратне рівняння без члена b", "formula": "ax² + c = 0 → x = ±√(−c/a)",
     "conditions": "В рівнянні відсутній доданок з x",
     "example": "3x² − 12 = 0 → x = ±2"},
    {"name": "Неповне квадратне рівняння без вільного члена c", "formula": "ax² + bx = 0 → x1 = 0, x2 = −b/a",
     "conditions": "В рівнянні відсутній вільний член",
     "example": "5x² − 10x = 0 → x1 = 0, x2 = 2"},
    {"name": "Теорема Вієта", "formula": "x1 + x2 = −b/a;  x1·x2 = c/a",
     "conditions": "Дозволяє перевірити корені без обчислення дискримінанта",
     "example": "x² − 5x + 6 = 0 → сума 5, добуток 6 → корені 2 і 3"},
    {"name": "Зведене квадратне рівняння (a = 1)", "formula": "x² + px + q = 0 → x1+x2 = −p, x1·x2 = q",
     "conditions": "Коефіцієнт при x² дорівнює 1",
     "example": "x² − 7x + 12 = 0 → корені 3 і 4"},
    {"name": "n-й член арифметичної прогресії", "formula": "aₙ = a1 + (n−1)d",
     "conditions": "d — різниця прогресії",
     "example": "a1=2, d=3, n=5 → a5 = 2 + 4·3 = 14"},
    {"name": "Сума n членів арифметичної прогресії", "formula": "Sₙ = (a1 + aₙ)/2 × n",
     "conditions": "Потрібно знати перший і n-й член",
     "example": "a1=2, a5=14, n=5 → S5 = 8×5 = 40"},
    {"name": "n-й член геометричної прогресії", "formula": "bₙ = b1 × qⁿ⁻¹",
     "conditions": "q — знаменник прогресії",
     "example": "b1=3, q=2, n=4 → b4 = 3×8 = 24"},
    {"name": "Сума n членів геометричної прогресії (q ≠ 1)", "formula": "Sₙ = b1(qⁿ − 1)/(q − 1)",
     "conditions": "q не дорівнює 1",
     "example": "b1=3, q=2, n=4 → S4 = 3×15 = 45"},
    {"name": "Сума нескінченної спадної геометричної прогресії", "formula": "S = b1 / (1 − q)",
     "conditions": "Застосовується лише коли |q| < 1",
     "example": "b1=4, q=0.5 → S = 4/0.5 = 8"},
    {"name": "Площа кола", "formula": "S = πr²",
     "conditions": "r — радіус кола",
     "example": "r=3 → S ≈ 28.3"},
    {"name": "Довжина кола", "formula": "C = 2πr",
     "conditions": "r — радіус кола",
     "example": "r=3 → C ≈ 18.85"},
    {"name": "Площа трикутника через основу і висоту", "formula": "S = (1/2)·a·h",
     "conditions": "a — основа, h — висота до цієї основи",
     "example": "a=6, h=4 → S = 12"},
    {"name": "Площа трикутника за формулою Герона", "formula": "S = √(p(p−a)(p−b)(p−c)), p — півпериметр",
     "conditions": "Відомі всі три сторони трикутника",
     "example": "a=3,b=4,c=5 → p=6 → S=6"},
    {"name": "Теорема Піфагора", "formula": "c² = a² + b²",
     "conditions": "Прямокутний трикутник, c — гіпотенуза",
     "example": "a=3, b=4 → c=5"},
    {"name": "Площа прямокутника", "formula": "S = a × b",
     "conditions": "a, b — сторони",
     "example": "a=5, b=3 → S=15"},
    {"name": "Площа трапеції", "formula": "S = ((a+b)/2) × h",
     "conditions": "a, b — основи, h — висота",
     "example": "a=6, b=4, h=3 → S=15"},
    {"name": "Площа паралелограма", "formula": "S = a × h",
     "conditions": "a — сторона, h — висота до неї",
     "example": "a=7, h=4 → S=28"},
]

# --- Перелік тем курсу (довідково для планувальника) ---
TOPICS = [
    {"topic": "Квадратні рівняння (повні)", "hours": 3},
    {"topic": "Неповні квадратні рівняння", "hours": 1.5},
    {"topic": "Теорема Вієта", "hours": 1},
    {"topic": "Арифметична прогресія", "hours": 2},
    {"topic": "Геометрична прогресія", "hours": 2},
    {"topic": "Коло: площа і довжина", "hours": 1},
    {"topic": "Площі трикутників", "hours": 2},
    {"topic": "Теорема Піфагора", "hours": 1.5},
    {"topic": "Площі чотирикутників", "hours": 2},
]


@st.cache_resource(show_spinner="Індексація довідника формул...")
def build_formula_index():
    texts = [f"{f['name']}. {f['formula']}. {f['conditions']}" for f in FORMULAS]
    resp = client.models.embed_content(model=EMBEDDING_MODEL, contents=texts)
    embeddings = np.array([e.values for e in resp.embeddings])
    nn = NearestNeighbors(n_neighbors=1, metric="cosine")
    nn.fit(embeddings)
    return nn


formula_index = build_formula_index()


def formula_search(query: str) -> dict:
    """Семантичний пошук у довіднику формул. Якщо впевненість нижча за поріг — чесно каже 'не знайдено'."""
    resp = client.models.embed_content(model=EMBEDDING_MODEL, contents=[query])
    q_emb = np.array([resp.embeddings[0].values])
    dist, idx = formula_index.kneighbors(q_emb, n_neighbors=1)
    similarity = round(1 - dist[0][0], 3)
    if similarity < SIMILARITY_THRESHOLD:
        return {"found": False, "similarity": similarity}
    return {"found": True, "similarity": similarity, **FORMULAS[idx[0][0]]}


def study_planner(topics_count: int, days: int, hours_per_day: int, weak_topics: str = "") -> dict:
    """Детермінований розрахунок розподілу часу. Без LLM — жодних вигаданих чисел."""
    total_hours = days * hours_per_day
    hours_per_topic = round(total_hours / topics_count, 1) if topics_count else 0
    weak_list = [t.strip() for t in weak_topics.split(",") if t.strip()]
    return {
        "topics_count": topics_count,
        "days": days,
        "hours_per_day": hours_per_day,
        "total_hours": total_hours,
        "hours_per_topic": hours_per_topic,
        "weak_topics": weak_list,
        "sufficient": total_hours >= topics_count * 1.5,
        "note": "Розрахунок ґрунтується лише на введеній кількості тем і часу. "
                "Слабкі теми — це самооцінка учня, система її не перевіряє.",
    }


# Базові фізичні величини (обмежений набір: довжина, швидкість, час, маса).
# base_factor — множник для переводу одиниці в базову (м, м/с, с, кг).
UNIT_ALIASES = {
    "м": ("length", 1.0), "m": ("length", 1.0), "метр": ("length", 1.0), "метри": ("length", 1.0), "метрів": ("length", 1.0),
    "км": ("length", 1000.0), "km": ("length", 1000.0), "кілометр": ("length", 1000.0), "кілометрів": ("length", 1000.0),
    "см": ("length", 0.01), "cm": ("length", 0.01), "сантиметр": ("length", 0.01), "сантиметрів": ("length", 0.01),
    "мм": ("length", 0.001), "mm": ("length", 0.001),
    "м/с": ("speed", 1.0), "m/s": ("speed", 1.0),
    "км/год": ("speed", 1000.0 / 3600.0), "km/h": ("speed", 1000.0 / 3600.0), "км/г": ("speed", 1000.0 / 3600.0),
    "с": ("time", 1.0), "s": ("time", 1.0), "сек": ("time", 1.0), "секунда": ("time", 1.0), "секунд": ("time", 1.0),
    "хв": ("time", 60.0), "min": ("time", 60.0), "хвилина": ("time", 60.0), "хвилин": ("time", 60.0),
    "год": ("time", 3600.0), "h": ("time", 3600.0), "година": ("time", 3600.0), "годин": ("time", 3600.0),
    "кг": ("mass", 1.0), "kg": ("mass", 1.0),
    "г": ("mass", 0.001), "g": ("mass", 0.001), "грам": ("mass", 0.001), "грамів": ("mass", 0.001),
}


def unit_converter_physics(value: float, from_unit: str, to_unit: str) -> dict:
    """Детермінована конвертація фізичних одиниць (довжина/швидкість/час/маса). Без LLM."""
    f = UNIT_ALIASES.get(from_unit.strip().lower())
    t = UNIT_ALIASES.get(to_unit.strip().lower())
    if not f or not t:
        unknown = from_unit if not f else to_unit
        return {"error": f"Одиницю '{unknown}' не підтримано.", "supported_units": sorted(UNIT_ALIASES)}
    if f[0] != t[0]:
        return {"error": f"'{from_unit}' і '{to_unit}' — різні фізичні величини ({f[0]} vs {t[0]}), конвертація неможлива."}
    result = value * f[1] / t[1]
    return {"value": value, "from_unit": from_unit, "to_unit": to_unit, "result": round(result, 6)}


FUNCTION_DECLARATIONS = [
    types.FunctionDeclaration(
        name="formula_search",
        description=(
            "Шукає формулу у перевіреному довіднику StudyMate за змістом запиту. "
            "Використовуй завжди, коли учень питає про конкретну формулу з математики "
            "(квадратні рівняння, прогресії, геометрія). Ніколи не подавай формулу з власної пам'яті."
        ),
        parameters={
            "type": "OBJECT",
            "properties": {
                "query": {"type": "STRING", "description": "Запит учня про формулу власними словами"}
            },
            "required": ["query"],
        },
    ),
    types.FunctionDeclaration(
        name="study_planner",
        description="Розраховує розподіл часу підготовки до іспиту між темами. Викликай, коли учень просить скласти план.",
        parameters={
            "type": "OBJECT",
            "properties": {
                "topics_count": {"type": "INTEGER"},
                "days": {"type": "INTEGER"},
                "hours_per_day": {"type": "INTEGER"},
                "weak_topics": {"type": "STRING", "description": "Теми, названі учнем слабкими, через кому"},
            },
            "required": ["topics_count", "days", "hours_per_day"],
        },
    ),
    types.FunctionDeclaration(
        name="unit_converter_physics",
        description=(
            "Конвертує фізичну величину між одиницями виміру (довжина, швидкість, час, маса). "
            "Використовуй завжди, коли учень просить перевести одні одиниці в інші. "
            "Ніколи не рахуй конвертацію в пам'яті."
        ),
        parameters={
            "type": "OBJECT",
            "properties": {
                "value": {"type": "NUMBER", "description": "Число, яке потрібно конвертувати"},
                "from_unit": {"type": "STRING", "description": "Одиниця, з якої конвертуємо, напр. 'км/год', 'м', 'кг'"},
                "to_unit": {"type": "STRING", "description": "Одиниця, в яку конвертуємо, напр. 'м/с', 'см', 'г'"},
            },
            "required": ["value", "from_unit", "to_unit"],
        },
    ),
]

GEMINI_TOOLS = [types.Tool(function_declarations=FUNCTION_DECLARATIONS)]

SYSTEM_PROMPT = """Ти StudyMate — освітній асистент з математики і обмеженої фізики (хімія — поза межами теми).

Правила, яких треба дотримуватись суворо:
1. Якщо учень питає формулу — ЗАВЖДИ викликай formula_search. Ніколи не подавай формулу з власної пам'яті напряму.
2. Якщо formula_search повертає found=false — чесно скажи, що точної формули в довіднику не знайдено, і попроси уточнити запит. НЕ вигадуй і не підставляй формулу з власних знань.
3. Якщо учень просить план підготовки — викликай study_planner. Якщо кількість тем, днів або годин не вказана — запитай, не вигадуй значення.
4. Якщо study_planner повертає sufficient=false — прямо попередь, що часу може не вистачити.
5. Якщо учень просить перевести фізичні одиниці (довжина, швидкість, час, маса) — ЗАВЖДИ викликай unit_converter_physics. Ніколи не рахуй конвертацію в пам'яті.
6. Хімія поза межами продукту — ввічливо відмов, поясни, що модуль хімії не підтримується.
7. Не розв'язуй контрольні роботи під ключ цілком — пояснюй логіку та формули, а не готову відповідь на конкретне завдання учня.

У кожному повідомленні учня може бути технічний контекст sidebar у форматі [Контекст із sidebar: ...] —
це параметри інтерфейсу (предмет, дні до іспиту, години на день, заявлені слабкі теми), а не слова учня.
"""


def call_agent(messages: list[dict]):
    contents = [
        types.Content(role="user" if m["role"] == "user" else "model", parts=[types.Part(text=m["content"])])
        for m in messages
    ]
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, tools=GEMINI_TOOLS)

    response = client.models.generate_content(model=CHAT_MODEL, contents=contents, config=config)
    parts = response.candidates[0].content.parts
    tool_calls = [p.function_call for p in parts if p.function_call]

    if not tool_calls:
        return response.text, None

    contents.append(response.candidates[0].content)

    last_result = None
    for fc in tool_calls:
        args = dict(fc.args)
        if fc.name == "formula_search":
            result = formula_search(**args)
        elif fc.name == "study_planner":
            result = study_planner(**args)
        elif fc.name == "unit_converter_physics":
            result = unit_converter_physics(**args)
        else:
            result = {"error": "unknown tool"}
        last_result = result
        contents.append(
            types.Content(role="user", parts=[types.Part.from_function_response(name=fc.name, response=result)])
        )

    final = client.models.generate_content(model=CHAT_MODEL, contents=contents, config=config)
    return final.text, last_result


# --- Стан сесії ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "saved_formulas" not in st.session_state:
    st.session_state.saved_formulas = []
if "study_plan" not in st.session_state:
    st.session_state.study_plan = None

st.title("📚 StudyMate — Освітній асистент")

# --- Sidebar ---
with st.sidebar:
    st.header("📖 Налаштування")
    subject = st.selectbox("Предмет", ["Математика", "Фізика (обмежено)"])

    st.divider()
    st.header("📅 До іспиту")
    exam_days = st.number_input("Днів до іспиту", min_value=1, max_value=60, value=3)
    hours_per_day = st.slider("Годин на день", min_value=1, max_value=8, value=2)
    weak_topics_input = st.text_input("Теми, які вважаєте слабкими (через кому)")
    st.caption("⚠️ Це самооцінка. Система її не перевіряє — реальний рівень може відрізнятись.")
    st.metric("Годин всього до іспиту", exam_days * hours_per_day)

    st.divider()
    st.header("📊 Прогрес")
    st.metric("Збережено формул", f"{len(st.session_state.saved_formulas)} / {len(FORMULAS)}")
    st.progress(min(len(st.session_state.saved_formulas) / len(FORMULAS), 1.0))

    st.divider()
    with st.expander("📚 Перелік тем курсу (довідково)"):
        for t in TOPICS:
            st.write(f"• {t['topic']} — {t['hours']} год")

    st.divider()
    if st.button("🗑️ Очистити чат"):
        st.session_state.messages = []
        st.rerun()

# --- Вкладки ---
tab_chat, tab_formulas, tab_plan = st.tabs(["💬 Чат", "📐 Формули", "📅 План"])

with tab_chat:
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.write(
                "Привіт! Я StudyMate 📚 Можу знайти формулу з математики (квадратні рівняння, "
                "прогресії, геометрія) або скласти план підготовки до іспиту. Про що запитаєш?"
            )

    if prompt := st.chat_input("Запитайте про формулу або попросіть скласти план..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Параметри з sidebar передаються моделі щоразу, а не лише коли заповнене поле слабких тем —
        # інакше вибір предмета/днів/годин у sidebar ні на що не впливає (декоративний UI).
        sidebar_context = f"[Контекст із sidebar: предмет {subject}, днів до іспиту {exam_days}, годин на день {hours_per_day}"
        if weak_topics_input:
            sidebar_context += f", заявлені слабкі теми: {weak_topics_input}"
        sidebar_context += "]"
        full_prompt = f"{prompt}\n{sidebar_context}"
        st.session_state.messages[-1]["content"] = full_prompt

        with st.chat_message("assistant"):
            with st.spinner("StudyMate шукає відповідь..."):
                answer, tool_result = call_agent(st.session_state.messages)
            st.write(answer)

            if tool_result and tool_result.get("found") is False:
                st.info(f"Пошук у довіднику дав недостатню впевненість ({tool_result['similarity']}) — точної формули не знайдено.")

            if tool_result and "sufficient" in tool_result:
                if not tool_result["sufficient"]:
                    st.warning("⚠️ За розрахунком, часу на всі теми може не вистачити.")
                if not st.session_state.saved_formulas:
                    st.warning("⚠️ Історія прогресу поки порожня — план ґрунтується лише на введених щойно даних.")
                st.session_state.study_plan = tool_result

        st.session_state.messages.append({"role": "assistant", "content": answer})

        if tool_result and tool_result.get("found"):
            if st.button("💾 Зберегти цю формулу", key=f"save_{len(st.session_state.messages)}"):
                st.session_state.saved_formulas.append(tool_result)
                st.rerun()

with tab_formulas:
    st.subheader("📐 Збережені формули")
    if not st.session_state.saved_formulas:
        st.info("Ще немає збережених формул. Знайди формулу через чат і натисни «Зберегти».")
    else:
        for i, f in enumerate(st.session_state.saved_formulas):
            with st.expander(f"📐 {f['name']}"):
                st.write(f"**Формула:** {f['formula']}")
                st.write(f"**Умови:** {f['conditions']}")
                st.write(f"**Приклад:** {f['example']}")
                st.caption(f"Впевненість пошуку: {f['similarity']}")
                if st.button("🗑️ Видалити", key=f"del_{i}"):
                    st.session_state.saved_formulas.pop(i)
                    st.rerun()

with tab_plan:
    st.subheader("📅 План підготовки до іспиту")
    plan = st.session_state.study_plan
    if plan is None:
        st.info("План ще не створено. Попроси StudyMate через чат: «Склади план підготовки: 9 тем, 3 дні, 2 години на день».")

        st.subheader("⚡ Швидке планування (без чату)")
        with st.form("quick_plan"):
            topics_count_q = st.number_input("Кількість тем", min_value=1, max_value=100, value=len(TOPICS))
            col1, col2 = st.columns(2)
            with col1:
                days_q = st.number_input("Днів", min_value=1, value=exam_days)
            with col2:
                hours_q = st.number_input("Годин/день", min_value=1, max_value=12, value=hours_per_day)
            weak_q = st.text_input("Слабкі теми (через кому)", value=weak_topics_input)
            if st.form_submit_button("📅 Скласти план"):
                st.session_state.study_plan = study_planner(topics_count_q, days_q, hours_q, weak_q)
                st.rerun()
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Тем всього", plan["topics_count"])
        col2.metric("Годин на тему", plan["hours_per_topic"])
        col3.metric("Годин всього", plan["total_hours"])

        if plan["weak_topics"]:
            st.write("**Заявлені слабкі теми:** " + ", ".join(plan["weak_topics"]))

        if plan["sufficient"]:
            st.success("✅ За розрахунком, часу достатньо.")
        else:
            st.warning("⚠️ Часу може не вистачити. Збільш години або скороти обсяг тем.")

        st.caption(plan["note"])

        days_passed = st.slider("Пройдено днів підготовки", 0, plan["days"], 0)
        progress_ratio = days_passed / plan["days"] if plan["days"] else 0
        st.progress(progress_ratio)
        st.caption(f"Орієнтовний прогрес: {days_passed} / {plan['days']} днів")

        if st.button("🔄 Перепланувати"):
            st.session_state.study_plan = None
            st.rerun()
