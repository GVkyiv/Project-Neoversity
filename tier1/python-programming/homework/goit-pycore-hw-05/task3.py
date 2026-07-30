# -*- coding: utf-8 -*-
import sys
from typing import Dict, List


def parse_log_line(line: str) -> Dict[str, str]:
    """Парсить один рядок логу на компоненти."""
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        raise ValueError("Невірний формат рядка логу")
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """Завантажує та парсить рядки логу з файлу."""
    logs: List[Dict[str, str]] = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не знайдено: {file_path}")
    except OSError as exc:
        raise OSError(f"Не вдалося прочитати файл: {file_path}") from exc
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """Фільтрує логи за рівнем (без урахування регістру)."""
    level = level.upper()
    return [log for log in logs if log.get("level") == level]


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """Підраховує кількість логів за рівнями."""
    counts: Dict[str, int] = {}
    for log in logs:
        level = log.get("level", "НЕВІДОМО")
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    """Виводить підрахунок у вигляді таблиці."""
    print("Рівень логування".ljust(18) + "| Кількість")
    print("-" * 19 + "|" + "-" * 10)
    for level, count in counts.items():
        print(level.ljust(18) + f"| {count}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Використання: python task3.py /path/to/logfile.log [level]")
        return

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(str(exc))
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
