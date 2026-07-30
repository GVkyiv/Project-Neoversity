# Neoversity MSc — навчання + ERC

Репозиторій для дворічної магістратури **Master of Science in Computer Science
(Specialization in Artificial Intelligence Product Management)**, Neoversity (GO IT),
диплом — Woolf University.

Мета репозиторію — три речі одночасно:

1. **Пам'ять курсу.** Все, що пройдено (лекції, ДЗ, висновки), лежить структуровано
   по Tier → Дисципліна → ДЗ, а не розмазано по чатах різних ІІ.
2. **Портативність.** Звичайні markdown/ipynb-файли. Однаково відкриваються у
   VS Code, Claude Code, ChatGPT (вставкою), Gemini — без прив'язки до пам'яті
   одного конкретного продукту.
3. **Міст до реальної роботи (головна мета).** Навчання тут не самоціль.
   Кожна пройдена тема курсу перевіряється питанням «як це застосувати в
   реальному житті і на моїй роботі в ERC?». Окрема гілка `erc-work/`
   збирає конкретні робочі AI-проєкти (product/project manager, internal ERP),
   список яких з часом росте, а не фіксований трьома пунктами — див.
   `erc-work/context.md` для актуального переліку і статусів.

## Структура

```
neoversity-msc/
├── PROGRAM.md            # мій навчальний план (відфільтровано з повної таблиці Neoversity)
├── CALENDAR.md            # дати початку/кінця кожної дисципліни + статус (завершено/в процесі/заплановано)
├── STATE.md               # де я зараз, що зроблено, що далі
├── DECISIONS_LOG.md        # закріплені висновки з курсу — не перегравати заново
├── prompts/                 # багаторазові промпти (наукова стаття, python-tutor, vibe coding)
├── erc-work/                # міст курс <-> реальна робота в ERC
│   ├── context.md            # хто я в ERC, які продукти плануються
│   └── tasks/                  # конкретні робочі задачі, де можна застосувати тему курсу
├── capstone-studymate/     # наскрізний дипломний проєкт StudyMate
├── tier1/
│   ├── python-programming/
│   ├── javascript-fundamentals/
│   └── human-computer-interaction-design/
├── tier2/
│   ├── ai-fundamentals/               # поточна дисципліна з реальними ДЗ
│   ├── generative-agentic-ai/        # ще не розпочато
│   ├── mlops-cicd/
│   ├── interaction-design-thinking-uxui/
│   ├── ux-research-usability-testing/
│   ├── ai-interfaces-design/
│   ├── agile-product-management/
│   ├── product-marketing/
│   └── product-analytics/
└── tier3/
    ├── market-strategy-capstone/
    ├── business-case-studies/
    ├── data-privacy-ai-regulation/
    ├── responsible-ai-leadership/
    └── applied-cs-capstone/
```

## Як цим користуватись

- Кожна дисципліна має свій `README.md` (короткий опис курсу, з чого складається
  фінальний проєкt) і папку `homework/`, куди докидаються реальні файли ДЗ.
- `STATE.md` і `DECISIONS_LOG.md` — головні файли для швидкого вводу в контекст
  будь-якого ІІ-асистента (Claude Code, ChatGPT, Gemini): вставляєш їх на початку
  нового чату замість переказу історії вручну.
- `erc-work/` наповнюється вручну — реальні задачі з ERC, які можна
  розв'язати тим, що вивчено на курсі.
- Tier 1 (Python, JavaScript, HCI) пройдено повністю і повністю наповнено
  реальними ДЗ. Більшість Tier 2/3, окрім AI Fundamentals, наразі — лише
  каркас папок з описом курсу з офіційної таблиці. Наповнення (конспекти,
  ДЗ) — по мірі завершення курсів.

## Секрети (API-ключі)

`.env` у корені містить реальні `OPENAI_API_KEY` і `GOOGLE_API_KEY` для
завдань AI Fundamentals. Файл у `.gitignore` (рядок `.env`), тому в git він
ніколи не потрапить — навіть якщо цей репозиторій пізніше опублікувати на
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
ведення в `STATE.md`/`CALENDAR.md`. Коли додаєш нове ДЗ — одразу став цей
блок зверху файлу чи README папки.

## Важливо

Це не автоматичний експорт "пам'яті Claude" — Claude не має доступу до окремого
"банку пам'яті", який можна скачати файлом. Все, що в цьому репозиторії, зібрано
вручну з того, що обговорювалося в чатах і що завантажено як файли. Тому
структура — стартова точка, яку потрібно активно наповнювати, а не готовий
архів "усіх знань".
