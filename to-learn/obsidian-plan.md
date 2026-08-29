---
tier: to-learn
type: study-plan
status: in-progress
date: 2026-08-29
---

# Учебный план: Obsidian

Составлен 29.08.2026. Режим: **один модуль в неделю**, внутри модуля по
часу в день. Всего 13 занятий, то есть 13 часов чистого времени, за
четыре недели. Старт 31.08.2026, финиш 27.09.2026.

Цель не «изучить Obsidian вообще», а конкретная: превратить этот
репозиторий в рабочую базу знаний, где Claude Code пишет файлы, а
Obsidian даёт по ним навигацию, дашборды и связи, без ручного ведения
таблиц в `STATE.md` и `CALENDAR.md`. Это уже заявлено в `README.md`
(раздел «Frontmatter у ДЗ»), но не сделано.

## Модули

Источник правды по статусу это поле `status` во frontmatter каждого
файла модуля. Здесь статусы не дублируются, чтобы не расходились.

| # | Модуль | Неделя | Занятий | Файл |
|---|---|---|---|---|
| 1 | База и гигиена vault | 31.08-06.09 | 3 | [obsidian-module-1.md](obsidian-module-1.md) |
| 2 | Vault как база данных | 07.09-13.09 | 4 | [obsidian-module-2.md](obsidian-module-2.md) |
| 3 | Ввод и шаблоны | 14.09-20.09 | 3 | [obsidian-module-3.md](obsidian-module-3.md) |
| 4 | Сшивка с Claude Code | 21.09-27.09 | 3 | [obsidian-module-4.md](obsidian-module-4.md) |

### Ссылки для открытия в Obsidian

Копируются в письма-напоминания как есть, не пересобирать:

- Модуль 1: `obsidian://open?vault=Project%20Neoversity&file=to-learn%2Fobsidian-module-1`
- Модуль 2: `obsidian://open?vault=Project%20Neoversity&file=to-learn%2Fobsidian-module-2`
- Модуль 3: `obsidian://open?vault=Project%20Neoversity&file=to-learn%2Fobsidian-module-3`
- Модуль 4: `obsidian://open?vault=Project%20Neoversity&file=to-learn%2Fobsidian-module-4`
- Общий список тем: `obsidian://open?vault=Project%20Neoversity&file=to-learn%2Fbacklog`
- Этот план: `obsidian://open?vault=Project%20Neoversity&file=to-learn%2Fobsidian-plan`

Дублирующие ссылки на GitHub, на случай если письмо открыто с телефона
и Obsidian там не установлен:

- [Модуль 1](https://github.com/GVkyiv/Project-Neoversity/blob/master/to-learn/obsidian-module-1.md)
  · [Модуль 2](https://github.com/GVkyiv/Project-Neoversity/blob/master/to-learn/obsidian-module-2.md)
  · [Модуль 3](https://github.com/GVkyiv/Project-Neoversity/blob/master/to-learn/obsidian-module-3.md)
  · [Модуль 4](https://github.com/GVkyiv/Project-Neoversity/blob/master/to-learn/obsidian-module-4.md)
  · [Общий список тем](https://github.com/GVkyiv/Project-Neoversity/blob/master/to-learn/backlog.md)

## Как ведётся статус

Два письма в неделю, оба генерируются облачной рутиной из GitHub.

**Понедельник 10:00.** Что учим на этой неделе: один модуль, ссылка на
него, ссылка на общий список тем. Не больше одного модуля в неделю.

**Пятница 18:00.** Напоминание обновить статусы. По этому письму нужно
проставить, что сделано, а что нет.

**Как отвечать (два способа, любой):**

1. Через Claude Code, в проекте `Project Neoversity`: сказать
   «обновил модуль N, занятия 1 и 2 сделал, третье нет, причина такая-то».
   Claude Code проставит чекбоксы, поменяет `status` во frontmatter,
   запишет строку в «Журнал» и закоммитит
2. Руками в Obsidian: открыть файл модуля по ссылке из письма,
   проставить чекбоксы, поменять `status`, дописать строку в «Журнал»

**Важно.** Письма собираются из GitHub, а не с локального диска. Если
статус обновлён локально, но не запушен, письмо покажет старые данные.
Поэтому после правки нужен `git push`. Способ 1 делает это сам.

**Значения `status` во frontmatter** (по схеме из `README.md`):
`planned`, `in-progress`, `done`. В письмах и в тексте показываются как
«в плане», «в процессе», «освоено».

## Что уже есть (проверено 29.08.2026)

Часть работы сделана, план это учитывает и не начинает с нуля:

- Obsidian установлен, репозиторий уже открыт как vault
- Стоят community-плагины: **Dataview**, **Omnisearch**,
  **Notebook Navigator**
- Включены core-плагины: graph, backlink, outgoing-link, canvas,
  properties, daily-notes, templates, bookmarks, outline, tag-pane,
  **bases**, sync
- Frontmatter проставлен в 59 файлах из 105, схема в `README.md`
- Есть два собственных факт-чек разбора по теме, их выводы учтены:
  [second-brain-obsidian-zettelkasten-critique](../ai-trends/reviews/2026-08-13_second-brain-obsidian-zettelkasten-critique.md)
  и [notebooklm-gemini-obsidian-optimization](../ai-trends/reviews/2026-08-13_notebooklm-gemini-obsidian-optimization.md)

Найденный мусор, убирается в модуле 1: пустой `2026-08-09.md` в корне
(создан плагином daily-notes, папка не настроена, файл попал в git) и
`Untitled.canvas` (в `.gitignore`, в git не попал).

## Плагины

Ставить по ходу плана, не все сразу.

| Плагин | Статус | Когда ставить | Зачем именно здесь |
|---|---|---|---|
| Dataview | стоит | | Запросы, которые Bases не умеет: inline в тексте, задачи, вычисления |
| Omnisearch | стоит | | Полнотекстовый поиск по vault |
| Notebook Navigator | стоит | | Навигация по папкам вместо стандартного проводника |
| Templater | ставим | модуль 3 | Шаблоны frontmatter, чтобы новые файлы совпадали с тем, что пишет Claude Code |
| QuickAdd | ставим | модуль 3 | Быстрый захват заметки по шаблону в нужную папку |
| Obsidian Git | ставим | модуль 4 | Видеть и коммитить изменения Claude Code, не выходя из vault |
| Excalidraw | опционально | после плана | Схемы для ДЗ и capstone. Для базы знаний не нужен, есть core-плагин Canvas |

Bases отдельно ставить не нужно, это core-плагин, уже включён.

## Чего в плане намеренно нет

**Платный курс «Obsidian. Полный курс»** (obsidian.second-brain.ru,
7990-17990 ₽). Не берём по трём причинам: 60+ уроков рассчитаны на
человека, который не знает markdown, YAML, git и файловую систему, то
есть около 70% курса будет уже пройденным материалом; оплата в рублях
российскому продавцу из Киева это отдельная проблема, а не деталь; и
курс учит вести vault с нуля, тогда как задача здесь обратная,
надстроить Obsidian над готовым репозиторием со своей структурой и
своими правилами в `AGENTS.md`.

**Сбор плагинов.** Из 2700+ community-плагинов в плане шесть, и ставятся
они не сразу, а в тот модуль, когда доходит очередь. Это прямо следует
из собственного вывода в разборе про «второй мозг»: граф и плагины это
форма, а не механизм мышления.

**Философия Zettelkasten и PARA.** Уже разобрана в факт-чеке 13.08.2026,
повторно проходить нечего. Аренс и Форте остаются фоновым чтением, но не
условием старта.

## Фоновое чтение (не обязательно, вне часа в день)

- Зонке Аренс, «Как делать полезные заметки» (перевод «How to Take Smart
  Notes»), метод Zettelkasten. Про мышление и письмо, не про инструмент
- Тьяго Форте, «Building a Second Brain», метод PARA. На английском,
  перевода не нашёл. Читать с поправкой на собственный факт-чек от
  13.08.2026
- Telegram-канал «Про Obsidian на русском»: https://t.me/s/obsidianru,
  читать по ходу, а не перед стартом

## Источники по плану

- Официальная документация Obsidian: https://obsidian.md/help/
- Документация Dataview: https://blacksmithgu.github.io/obsidian-dataview/
- Сравнение Bases и Dataview, состояние на 2026: https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases/
- Обзор core-плагина Bases: https://practicalpkm.com/bases-plugin-overview/
- Подборка плагинов 2026: https://www.dsebastien.net/the-must-have-obsidian-plugins-for-2026/
