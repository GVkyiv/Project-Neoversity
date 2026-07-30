from datetime import datetime, timedelta

# Основна функція: повертає список користувачів, яких треба привітати протягом найближчих 7 днів
def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date()  # Поточна дата (без часу)
    upcoming_birthdays: list[dict[str, str]] = []  # Сюди будемо збирати результати

    # Проходимо по кожному користувачу зі списку
    for user in users:
        # Перетворюємо рядок дати "YYYY.MM.DD" на об’єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Робимо дату дня народження на поточний рік (щоб порівнювати з today)
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже був цього року — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Рахуємо, скільки днів залишилось до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Беремо тільки ті дні народження, які в межах 0..7 днів включно
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year  # Початково вітаємо в сам день народження

            # Якщо дата припадає на суботу (5) — переносимо привітання на понеділок (+2)
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            # Якщо дата припадає на неділю (6) — переносимо привітання на понеділок (+1)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Додаємо у результати ім’я та дату привітання у форматі "YYYY.MM.DD"
            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays  # Повертаємо список усіх привітань, що потрапили у вікно 7 днів


# Допоміжна функція: якщо дата випала на вихідні — переносить на понеділок, інакше лишає як є
def _shift_to_monday_if_weekend(day):
    if day.weekday() == 5:          # 5 = субота
        return day + timedelta(days=2)
    if day.weekday() == 6:          # 6 = неділя
        return day + timedelta(days=1)
    return day                      # Будній день — нічого не змінюємо


# Допоміжна функція: готує тестові дані (користувачів) і очікуваний результат для перевірки
def _build_test_data():
    today = datetime.today().date()  # Поточна дата (основа для генерації дат)

    # Знаходимо найближчий будній день у вікні 0..7 днів
    regular_day = next(
        today + timedelta(days=offset)
        for offset in range(0, 8)
        if (today + timedelta(days=offset)).weekday() < 5
    )

    # Знаходимо найближчу суботу та найближчу неділю від today
    saturday = today + timedelta(days=(5 - today.weekday()) % 7)
    sunday = today + timedelta(days=(6 - today.weekday()) % 7)

    # Дата поза вікном (8 днів) — має НЕ потрапити у результати
    outside_window = today + timedelta(days=8)

    # Формуємо список користувачів з днями народження (рік не важливий — важливі місяць/день)
    users = [
        {"name": "Regular User", "birthday": regular_day.strftime("1990.%m.%d")},
        {"name": "Saturday User", "birthday": saturday.strftime("1991.%m.%d")},
        {"name": "Sunday User", "birthday": sunday.strftime("1992.%m.%d")},
        {"name": "Outside Window", "birthday": outside_window.strftime("1993.%m.%d")},
    ]

    # Очікувані дати привітань: вихідні переносимо на понеділок
    expected = {
        "Regular User": _shift_to_monday_if_weekend(regular_day).strftime("%Y.%m.%d"),
        "Saturday User": _shift_to_monday_if_weekend(saturday).strftime("%Y.%m.%d"),
        "Sunday User": _shift_to_monday_if_weekend(sunday).strftime("%Y.%m.%d"),
    }

    return users, expected  # Повертаємо тестові дані та еталон для перевірки


# Точка входу: цей блок виконується лише якщо файл запущено напряму (а не імпортовано як модуль)
if __name__ == "__main__":
    users, expected = _build_test_data()            # Беремо тестові дані
    upcoming = get_upcoming_birthdays(users)        # Запускаємо основну функцію

    print("Upcoming birthdays:", upcoming)          # Друкуємо, що отримали

    # Перетворюємо список результатів у словник "ім’я -> дата", щоб зручно порівняти з expected
    result_by_name = {item["name"]: item["congratulation_date"] for item in upcoming}

    # Перевіряємо, що для кожного очікуваного імені дата збігається
    checks_passed = all(result_by_name.get(name) == date for name, date in expected.items())
    # Додатково перевіряємо, що користувач поза вікном не потрапив у результати
    checks_passed = checks_passed and ("Outside Window" not in result_by_name)

    print("Checks passed:", checks_passed)          # Виводимо результат перевірки

