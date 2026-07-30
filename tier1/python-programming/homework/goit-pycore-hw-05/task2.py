# -*- coding: utf-8 -*-
import re
from typing import Callable, Iterable


def generator_numbers(text: str) -> Iterable[float]:
    """Генерує всі дійсні числа, що відокремлені пробілами."""
    pattern = re.compile(r"(?<!\S)\d+(?:\.\d+)?(?!\S)")
    for match in pattern.finditer(text):
        yield float(match.group(0))


def sum_profit(text: str, func: Callable[[str], Iterable[float]]) -> float:
    """Повертає суму чисел, згенерованих заданою функцією."""
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими "
        "надходженнями 127.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
