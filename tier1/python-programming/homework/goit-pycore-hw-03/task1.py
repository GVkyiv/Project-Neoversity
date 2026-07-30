
from datetime import date, datetime


def get_days_from_today(date_str: str) -> int:
 
    try:
        # Перетворюємо рядок у об'єкт datetime за заданим форматом
    
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        # Якщо формат дати неправильний — виникає ValueError
        # Ми перехоплюємо його і викидаємо власне пояснення
        raise ValueError(
            "Неправильний формат. Використовуйте YYYY-MM-DD, наприклад 2020-10-09"
        )

    # date.today() — поточна дата
    # Віднімаємо введену дату від сьогоднішньої
    # Результат — timedelta, у якого беремо кількість днів
    return (date.today() - given_date).days


# Цей блок виконається тільки якщо файл запускається напряму,
# а не імпортується як модуль
if __name__ == "__main__":
    # Запитуємо дату у користувача
    user_input = input("Введіть дату (YYYY-MM-DD): ")

    try:
        # Викликаємо функцію і виводимо результат
        print(get_days_from_today(user_input))
    except ValueError as error:
        # Якщо функція викинула помилку — виводимо її текст
        print(error)
