# Copilot instructions for goit-pycore-hw-04

These instructions are intended to help an AI coding agent be productive immediately in this small Python exercise repository.

Overview
- This repo is a collection of independent task scripts under `Task1/`..`Task4/`.
- Each task is a small CLI-style Python script with a `main()` that returns an `int` and the module entrypoint `raise SystemExit(main())`.
- Common patterns: `pathlib.Path` for path handling, explicit `utf-8` file reads, and PEP 484 style type hints (Python 3.10+ syntax such as `str | Path`).

Key files to inspect
- `Task1/task1.py` — parses `salary_file.txt`, exposes `total_salary(path)` which returns `(total, average)` and validates malformed lines with `ValueError` including line numbers. Example run: `python Task1/task1.py` uses `salary_file.txt` next to the script; you can pass a path as the first arg.
- `Task2/task2.py` — parses `cats_file.txt` into a list of dicts via `get_cats_info(path)`. Uses strict comma-separated splitting and raises `ValueError` for format errors.
- `Task3/task3.py` — prints a colored directory tree; depends on `colorama` (listed in `requirements.txt`). Detects whether stdout supports Unicode tree characters.
- `Task4/task4.py` — small interactive assistant loop; parsing is handled in `parse_input()` and commands mutate an in-memory `contacts` dict.

Project-specific conventions and patterns
- CLI structure: prefer `main() -> int` and `raise SystemExit(main())` at module bottom rather than calling `sys.exit()` directly.
- File defaults: scripts look for default sample files placed beside the script via `Path(__file__).with_name("<file>")`. When adding tests or runners, mirror this relative-file behavior.
- Error handling: data-parsing functions raise `ValueError` with contextual information (line numbers). Keep this pattern when adding new parsers so callers can present helpful errors.
- Typing: functions are fully typed using modern syntax (e.g., `list[dict[str, str]]` and union `str | Path`). Generate type-compatible changes.
- Encoding: files are opened with `encoding='utf-8'`. Preserve encoding in new file IO.

Developer workflows (how to run and debug)
- Install dependencies: `pip install -r requirements.txt` (project uses `colorama`).
- Run a task script directly from repo root, for example:
  - `python Task1/task1.py` (uses `Task1/salary_file.txt` by default)
  - `python Task2/task2.py` `./Task2/cats_file.txt`
  - `python Task3/task3.py` `.`
  - `python Task4/task4.py` (interactive)
- Debugging notes: these scripts assume direct CLI invocation. For debugger runs, set `sys.argv` or pass the expected args; `main()` returns status codes so you can call it and inspect outputs programmatically.

Integration points & external deps
- The only declared dependency is `colorama` in `requirements.txt`. There are no network calls or databases.

What to change and how to add features
- When adding a new task, follow the same layout: one script under `TaskN/`, a `main() -> int`, and `raise SystemExit(main())` at the bottom.
- If adding file-based inputs, place sample files alongside the task file and mirror the `Path(__file__).with_name('...')` default logic.
- Preserve type annotations and UTF-8 file handling in any new code.

Examples to copy/paste
- Read-safely and raise contextual error (follow `Task1` pattern):

```py
file_path = Path(path)
with file_path.open('r', encoding='utf-8') as fh:
    for i, raw in enumerate(fh, 1):
        s = raw.strip()
        if not s:
            continue
        try:
            ...  # parse
        except ValueError as e:
            raise ValueError(f"Invalid data format in line {i}: {s!r}") from e
```

Ask for feedback
- If any of these notes are incomplete or you'd like additional examples (unit test skeletons, a CI workflow, or refactoring guidelines), tell me which area to expand and I'll update this file.
