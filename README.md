# Neoversity MSc: навчання + ERC

Репозиторій для дворічної магістратури **Master of Science in Computer Science
(Specialization in Artificial Intelligence Product Management)**, Neoversity (GO IT),
диплом Woolf University.

У репозиторію чотири мети одночасно:

1. **Пам'ять курсу.** Все, що пройдено (лекції, ДЗ, висновки), лежить структуровано
   по Tier → Дисципліна → ДЗ, а не розмазано по чатах різних ІІ.
2. **Портативність.** Звичайні markdown/ipynb-файли. Однаково відкриваються у
   VS Code, Claude Code, ChatGPT (вставкою), Gemini, без прив'язки до пам'яті
   одного конкретного продукту.
3. **Міст до реальної роботи (головна мета).** Навчання тут не самоціль.
   Кожна пройдена тема курсу перевіряється питанням «як це застосувати в
   реальному житті і на моїй роботі в ERC?». Окрема гілка `erc-work/`
   збирає конкретні робочі AI-проєкти (product/project manager, internal ERP),
   список яких з часом росте, а не фіксований трьома пунктами: див.
   `erc-work/context.md` для актуального переліку і статусів.
4. **Критичний фільтр зовнішнього контенту.** Окрема гілка `ai-trends/`:
   розбір навчальних і новинних відео про AI з YouTube (за транскриптом):
   резюме, факт-чек, звірка з актуальними трендами, і головне, чи
   застосовно це до мого навчання і роботи в ERC, чи ні. Див.
   [ai-trends/README.md](ai-trends/README.md).

## Структура

Ключові файли: [PROGRAM.md](PROGRAM.md) (навчальний план) ·
[CALENDAR.md](CALENDAR.md) (дати й статуси дисциплін) ·
[STATE.md](STATE.md) (де я зараз) ·
[DECISIONS_LOG.md](DECISIONS_LOG.md) (закріплені висновки) ·
[prompts/](prompts/README.md) (багаторазові промпти) ·
[erc-work/context.md](erc-work/context.md) (міст курс↔робота) ·
[ai-trends/](ai-trends/README.md) (розбір AI-відео з YouTube) ·
[capstone-studymate/](capstone-studymate/README.md) (наскрізний диплом StudyMate) ·
[to-learn/backlog.md](to-learn/backlog.md) (інструменти, які хочу освоїти).

Інструкції для ІІ-агентів: [AGENTS.md](AGENTS.md), Claude Code читає його
через міст [CLAUDE.md](CLAUDE.md).

**Tier 1:**
[Python Programming](tier1/python-programming/README.md) ·
[JavaScript Fundamentals](tier1/javascript-fundamentals/README.md) ·
[Human-Computer Interaction Design](tier1/human-computer-interaction-design/README.md)

**Tier 2:**
[AI Fundamentals](tier2/ai-fundamentals/README.md) (поточна) ·
[Generative and Agentic AI](tier2/generative-agentic-ai/README.md) ·
[MLOps CI/CD](tier2/mlops-cicd/README.md) ·
[Interaction Design and Design Thinking for UX/UI](tier2/interaction-design-thinking-uxui/README.md) ·
[UX Research Methods and Usability Testing](tier2/ux-research-usability-testing/README.md) ·
[AI Interfaces Design](tier2/ai-interfaces-design/README.md) ·
[Agile Product Management](tier2/agile-product-management/README.md) ·
[Product Marketing](tier2/product-marketing/README.md) ·
[Product Analytics](tier2/product-analytics/README.md)

**Tier 3:**
[Market Strategy Capstone](tier3/market-strategy-capstone/README.md) ·
[Business Case Studies](tier3/business-case-studies/README.md) ·
[Data Privacy and AI Regulation](tier3/data-privacy-ai-regulation/README.md) ·
[Responsible AI Leadership](tier3/responsible-ai-leadership/README.md) ·
[Applied Computer Science Capstone](tier3/applied-cs-capstone/README.md)

## Як цим користуватись

- Кожна дисципліна має свій `README.md` (короткий опис курсу, з чого складається
  фінальний проєкт) і папку `homework/`, куди докидаються реальні файли ДЗ.
- `STATE.md` і `DECISIONS_LOG.md` це головні файли для швидкого вводу в контекст
  будь-якого ІІ-асистента (Claude Code, ChatGPT, Gemini): вставляєш їх на початку
  нового чату замість переказу історії вручну.
- `erc-work/` наповнюється вручну: реальні задачі з ERC, які можна
  розв'язати тим, що вивчено на курсі.
- Tier 1 (Python, JavaScript, HCI) пройдено повністю і повністю наповнено
  реальними ДЗ. Більшість Tier 2/3, окрім AI Fundamentals, наразі це лише
  каркас папок з описом курсу з офіційної таблиці. Наповнення (конспекти,
  ДЗ) йде по мірі завершення курсів.

## Секрети (API-ключі)

`.env` у корені містить реальні `OPENAI_API_KEY` і `GOOGLE_API_KEY` для
завдань AI Fundamentals. Файл у `.gitignore` (рядок `.env`), тому в git він
ніколи не потрапить, навіть якщо цей репозиторій пізніше опублікувати на
GitHub. `.env.example` показує лише назви змінних, без значень, для
довідки/публікації. У коді читати ключі через `os.environ` /
`python-dotenv` (`load_dotenv()`), ніколи не хардкодити значення в `.py`/
`.ipynb`, які потрапляють у git.

## Frontmatter у ДЗ (для Obsidian/Dataview)

Кожна папка/файл ДЗ у `homework/` починається з YAML frontmatter:

```yaml
---
tier: 1|2|3
discipline: python-programming|javascript-fundamentals|...
topic: 2            # номер теми курсу, якщо застосовно
type: homework|final-project|scientific-review|reference-material
status: done|in-progress|planned
date: 2026-07-30    # тільки якщо дата точно відома, не вигадувати
---
```

Додано 30.07.2026, щоб репозиторій можна було відкрити як Obsidian vault і
будувати автоматичні таблиці статусів плагіном Dataview замість ручного
ведення в `STATE.md`/`CALENDAR.md`. Коли додаєш нове ДЗ, одразу став цей
блок зверху файлу чи README папки.

Файли в `erc-work/tasks/` (реальні робочі задачі, не ДЗ) використовують
`tier: erc-work` і `type: task` замість дисципліни курсу. Аналогічно файли в
`ai-trends/reviews/` використовують `tier: ai-trends` і `type: video-review`.

## Важливо

Це не автоматичний експорт "пам'яті Claude": Claude не має доступу до окремого
"банку пам'яті", який можна скачати файлом. Все, що в цьому репозиторії, зібрано
вручну з того, що обговорювалося в чатах і що завантажено як файли. Тому
структура це стартова точка, яку потрібно активно наповнювати, а не готовий
архів "усіх знань".
