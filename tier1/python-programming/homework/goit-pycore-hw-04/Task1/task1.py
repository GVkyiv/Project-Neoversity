from __future__ import annotations

import sys
from pathlib import Path


def total_salary(path: str | Path) -> tuple[int, float]:
    """Return total and average salary from a comma-separated text file."""
    total = 0
    count = 0
    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                _, salary_text = line.split(",", maxsplit=1)
                salary = int(salary_text)
            except ValueError as error:
                raise ValueError(
                    f"Invalid data format in line {line_number}: {line!r}"
                ) from error

            total += salary
            count += 1

    average = total / count if count else 0.0
    return total, average


def main() -> int:
    file_path = (
        Path(sys.argv[1]).expanduser()
        if len(sys.argv) == 2
        else Path(__file__).with_name("salary_file.txt")
    )

    if not file_path.exists():
        print(f"Error: path does not exist: {file_path}")
        return 1

    if not file_path.is_file():
        print(f"Error: path is not a file: {file_path}")
        return 1

    total, average = total_salary(file_path)
    print(f"Total salary: {total}, Average salary: {average}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
