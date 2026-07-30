from __future__ import annotations

import sys
from pathlib import Path


def get_cats_info(path: str | Path) -> list[dict[str, str]]:
    """Return list of cats info from a comma-separated text file."""
    cats: list[dict[str, str]] = []
    file_path = Path(path)

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                cat_id, name, age = line.split(",")
            except ValueError as error:
                raise ValueError(
                    f"Invalid data format in line {line_number}: {line!r}"
                ) from error

            cats.append({"id": cat_id, "name": name, "age": age})

    return cats


def main() -> int:
    file_path = (
        Path(sys.argv[1]).expanduser()
        if len(sys.argv) == 2
        else Path(__file__).with_name("cats_file.txt")
    )

    if not file_path.exists():
        print(f"Error: path does not exist: {file_path}")
        return 1

    if not file_path.is_file():
        print(f"Error: path is not a file: {file_path}")
        return 1

    cats_info = get_cats_info(file_path)
    print(cats_info)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
