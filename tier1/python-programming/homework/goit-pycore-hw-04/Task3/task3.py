from __future__ import annotations

import sys
from pathlib import Path

from colorama import Fore, Style, init


def supports_unicode_tree_chars() -> bool:
    """Return True if current stdout encoding supports tree drawing chars."""
    encoding = sys.stdout.encoding or "utf-8"
    try:
        "\u2514\u251c\u2502".encode(encoding)
    except UnicodeEncodeError:
        return False
    return True


def print_directory_tree(
    directory: Path, prefix: str = "", use_unicode: bool = True
) -> None:
    """Recursively print directory tree with colored names."""
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower()),
        )
    except PermissionError:
        print(f"{prefix}{Fore.RED}[ACCESS DENIED]{Style.RESET_ALL} {directory.name}")
        return

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1

        if use_unicode:
            connector = "\u2514\u2500\u2500 " if is_last else "\u251c\u2500\u2500 "
            next_prefix = prefix + ("    " if is_last else "\u2502   ")
        else:
            connector = "`-- " if is_last else "|-- "
            next_prefix = prefix + ("    " if is_last else "|   ")

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{entry.name}{Style.RESET_ALL}")
            print_directory_tree(entry, next_prefix, use_unicode)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main() -> int:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Usage: python task3.py <directory_path>")
        return 1

    root_path = Path(sys.argv[1]).expanduser().resolve()

    if not root_path.exists():
        print(f"Error: path does not exist: {root_path}")
        return 1

    if not root_path.is_dir():
        print(f"Error: path is not a directory: {root_path}")
        return 1

    print(f"{Fore.CYAN}{root_path}{Style.RESET_ALL}")
    print_directory_tree(root_path, use_unicode=supports_unicode_tree_chars())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
