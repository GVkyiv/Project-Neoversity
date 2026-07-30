# Діаграми архітектури: ChefBot на LangGraph (Тема 9)

**Файл коду:** `yudbox_hw09_chef_bot.ipynb`
**Опис рішення:** `IMPLEMENTATION-PLAN-CHEFBOT-LANGGRAPH.md`

Два різні представлення однієї й тієї самої системи:

1. **Діаграма 1** — топологія графа станів (вузли й ребра), як він виконується в базовому/автоматичному
   режимі, коли немає живої людини, яка натискає кнопки.
2. **Діаграма 2** — послідовність подій під час реального human-in-the-loop: коли граф справді зупиняється
   і чекає на клік людини (демонстраційна комірка з `ipywidgets`).

Це не дві різні архітектури — механізм зупинки (`interrupt()`/`Command(resume=...)`) один і той самий в
обох випадках. Різниця лише в тому, **хто** приймає рішення про продовження: реальна людина (діаграма 2)
чи код автотесту, що імітує підтвердження (примітка в діаграмі 1).

---

## Діаграма 1. Топологія графа (`StateGraph`) — базовий/автоматичний потік

```mermaid
flowchart TD
    START(["START"]) --> ER["extract_restrictions
    AI-визначення dietary_restrictions
    з останнього повідомлення"]

    ER --> AGENT["agent
    LLM + динамічний системний промпт
    (підставляє поточні dietary_restrictions)"]

    AGENT -->|"AIMessage має tool_calls"| COND{"tools_condition"}
    AGENT -->|"AIMessage без tool_calls
    (звичайна відповідь)"| END(["END"])

    COND -->|"tools"| TOOLS["tools (ToolNode)
    recipe_search / unit_converter /
    substitution_finder"]

    TOOLS --> CHECK["check_allergy_risk"]

    CHECK -->|"конфлікту з алергією немає
    (no-op — більшість випадків)"| AGENT

    CHECK -.->|"substitution_finder повернув
    щось, що збігається з
    зареєстрованою алергією"| INT{{"interrupt()
    зупинка + збереження стану
    через checkpointer"}}

    INT -.->|"у run_automatic_tests():
    авто-approve в коді,
    БЕЗ реальної людини"| AGENT

    style INT fill:#4a1f1f,stroke:#e06c75,color:#fff
    style CHECK fill:#1f2d3a,stroke:#61afef,color:#fff
```

**Як читати цю діаграму.** Суцільні лінії — звичайний, найчастіший шлях виконання (цикл ReAct:
агент викликає інструмент, отримує результат, вирішує викликати ще один або відповісти). Пунктирні лінії —
рідкісна гілка, що трапляється, лише коли `substitution_finder` пропонує замінник, який конфліктує з
зареєстрованою алергією користувача. У режимі автоматичного тестування (`run_automatic_tests`) ця гілка,
навіть якщо активується, не чекає жодної людини — код одразу сам підтверджує продовження, щоб тест міг
завершитися без втручання. Реальне очікування людини показане окремо, у діаграмі 2.

---

## Діаграма 2. Human-in-the-loop із реальним підтвердженням людини

Ця послідовність відповідає комірці `hitl_config` / демонстрації з кнопками `ipywidgets` у ноутбуці:
користувач спершу повідомляє про алергію на нут, потім просить замінник для яєць — один із варіантів у
базі (аквафаба) якраз готується з нуту.

```mermaid
sequenceDiagram
    actor Ви as Людина (у ноутбуці)
    participant RT as run_turn / handle_result
    participant G as graph.invoke(...)
    participant CP as Checkpointer (InMemorySaver)
    participant UI as ipywidgets (кнопки)

    Ви->>RT: run_turn("У мене алергія на нут.")
    RT->>G: graph.invoke({messages: [...]}, config)
    G->>G: extract_restrictions -> agent
    G-->>RT: звичайна відповідь ("врахую алергію на нут")
    RT-->>Ви: 🤖 ChefBot: Дякую, врахую...

    Ви->>RT: run_turn("Чим замінити яйця у випічці?")
    RT->>G: graph.invoke({messages: [...]}, config)
    G->>G: agent -> tools (substitution_finder) -> check_allergy_risk
    Note over G: Результат tool'а згадує "нут" —<br/>збіг із зареєстрованою алергією
    G->>CP: зберегти стан саме на check_allergy_risk
    G-->>RT: результат містить "__interrupt__" з payload (ризик, замінник)
    RT->>UI: show_confirmation_widget(payload)
    UI-->>Ви: показує попередження + кнопки<br/>"✅ Так, все одно" / "❌ Ні, запропонуй інше"

    Ви->>UI: клік по кнопці

    alt Клік "✅ Так, все одно" (resume="approve")
        UI->>G: graph.invoke(Command(resume="approve"), config)
        G->>CP: відновити стан з check_allergy_risk
        G->>G: check_allergy_risk повертає {} (no-op) -> agent -> END
        G-->>UI: фінальна відповідь (варіант з аквафабою залишається)
        UI-->>Ви: 🤖 ChefBot: показує відповідь як є
    else Клік "❌ Ні, запропонуй інше" (resume="reject")
        UI->>G: graph.invoke(Command(resume="reject"), config)
        G->>CP: відновити стан з check_allergy_risk
        G->>G: check_allergy_risk додає службове HumanMessage<br/>"людина відхилила варіант через нут" -> agent
        G->>G: agent пропонує інший замінник (без нуту)
        G-->>UI: нова відповідь без ризикованого інгредієнта
        UI-->>Ви: 🤖 ChefBot: показує безпечну альтернативу
    end
```

**Ключова відмінність від діаграми 1.** Тут кроки «UI показує кнопки» і «Ви клікаєте» — реальні, з паузою
невизначеної тривалості (граф технічно "заморожений" між `interrupt()` і моментом кліка). У режимі
автотестування ця пауза відсутня: замість блоку `alt` з реальним вибором людини код одразу і безумовно йде
шляхом `resume="approve"`.
