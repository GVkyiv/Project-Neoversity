from __future__ import annotations


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Вкажіть ім'я та телефон."
        except KeyError:
            return "Користувача не знайдено."
        except IndexError:
            return "Вкажіть аргумент для команди."
    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name.lower()] = phone
    return "Контакт додано."


@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    name = name.lower()
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Контакт оновлено."


@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0].lower()
    return f"{name}: {contacts[name]}"


@input_error
def show_all(args: list[str], contacts: dict[str, str]) -> str:
    if not contacts:
        return "Контакти відсутні."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: dict[str, str] = {}
    print("Вітаю в боті-помічнику!")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit", "bye"):
            print("До побачення!")
            break
        if command == "hello":
            print("Чим можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "":
            print("Вкажіть команду.")
        else:
            print("Невідома команда.")




