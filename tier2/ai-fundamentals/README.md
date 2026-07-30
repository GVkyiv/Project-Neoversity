# AI Fundamentals

Tier 2. **Поточна дисципліна** — саме тут зроблено найбільше реальної роботи.
Статус: за програмою 133,92 год, фінальний проєкт 35% ваги.

Модулі за таблицею: AI у цифрових продуктах, архітектура AI-систем, інтеграція
LLM у продукт, робота з даними в AI-продуктах, розгортання AI-сервісів,
LangChain, embeddings, чат-бот на LangChain (продуктова рамка), агентні
workflow у LangGraph, Streamlit/Gradio, фреймворк Agno, оцінювання AI-систем.
Окремо: наукова публікація (рев'ю статті), фінальний проєкт.

## Зроблено (у `homework/`)

- [hw02_studymate_product_arch.md](homework/hw02_studymate_product_arch.md) — тема 2, продукт і архітектура StudyMate
- [hw06_risks.md](homework/hw06_risks.md) — тема 6, архітектурні рішення і документація ризиків
- [hw07_task.md](homework/hw07_task.md) + [hw07_notebook.ipynb](homework/hw07_notebook.ipynb) — тема 7, embeddings
- [hw08_embeddings.ipynb](homework/hw08_embeddings.ipynb) — тема 8, пайплайн семантичного пошуку (продуктова
  рамка чат-бота на LangChain)
- [hw08_task_001_variant3.ipynb](homework/hw08_task_001_variant3.ipynb), [hw08_variant3_studymate_notes.md](homework/hw08_variant3_studymate_notes.md),
  [hw08_preparation_notes.md](homework/hw08_preparation_notes.md), [hw08_progress_notes.md](homework/hw08_progress_notes.md) — тема 8, Task_001
  Variant 3: LangChain tools + LangGraph агент у Colab (4 інструменти),
  включно з живою перевіркою обмежень (GPT-4o-mini порушував текстову
  заборону в промпті)
- [hw09_architecture_diagram_chefbot_langgraph.md](homework/hw09_architecture_diagram_chefbot_langgraph.md),
  [hw09_implementation_plan_chefbot_langgraph.md](homework/hw09_implementation_plan_chefbot_langgraph.md), [hw09_progress_notes.md](homework/hw09_progress_notes.md) —
  тема 9, агентний workflow ChefBot на LangGraph
- [hw10_streamlit_app/](homework/hw10_streamlit_app/README.md) — тема 10, повний Streamlit-застосунок StudyMate
  (`app.py`, `requirements.txt`, продуктова рамка, `Knowledge/`)
- [scientific-publication-articles/](homework/scientific-publication-articles/README.md) — довідкові статті з AI Product
  Management, використані як матеріал для теми «Наукова публікація»
- [scientific-review/](homework/scientific-review/README.md) — тема «Наукова публікація», завершено 30.07.2026:
  рецензія на статтю «Trust by Interface: How Different User Interfaces
  Shape Human Trust in Health Information from Large Language Models»
  (Sun et al., CHI EA '24). Ключові інсайти: звичка користувача переважає
  над об'єктивною якістю інтерфейсу; текст легше перечитати ніж переслухати
  (застосовано до StudyMate: голосовий інтерфейс йому не потрібен через
  формули); недостатньо переконливий людиноподібний інтерфейс шкодить
  довірі більше, ніж нейтральний пристрій

Промпт для розбору наукової статті (переклад + рецензія) винесено на рівень
репозиторію: [`prompts/scientific-article-review.md`](../../prompts/scientific-article-review.md)
— бо ця задача повторюється в кожному курсі, а не тільки тут.

Ключові висновки з цих ДЗ зафіксовані в кореневому [DECISIONS_LOG.md](../../DECISIONS_LOG.md) — не
переспорювати заново.

Пряма паралель з наскрізним дипломним проєктом: [capstone-studymate](../../capstone-studymate/README.md).

## Не вистачає

- ДЗ для теми 11 (Фреймворк Agno) — ще не пройдено.
- Фінальний проєкт курсу.

## Примітка щодо найменування файлів

Файл `HW7/ДЗ[8]_Воленбовський.ipynb` (у вихідній папці ДЗ) названо як «ДЗ8»,
хоча лежить у теці HW7 — очевидна помилка нумерації при збереженні файлу
автором. Збережено тут як [hw07_notebook.ipynb](homework/hw07_notebook.ipynb), прив'язка до теми 7
підтверджена вмістом і датою файлу, а не назвою.

## Пов'язано

[← до README репозиторію](../../README.md) · [STATE.md](../../STATE.md) ·
[CALENDAR.md](../../CALENDAR.md)
