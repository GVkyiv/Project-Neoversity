from __future__ import annotations


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """Parse user input into command and arguments."""
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Add a new contact to the contacts dictionary."""
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Change an existing contact phone number."""
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    name = name.lower()
    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Return phone by contact name."""
    if len(args) != 1:
        return "Invalid command."

    name = args[0].lower()
    return contacts.get(name, "Contact not found.")


def show_all(contacts: dict[str, str]) -> str:
    """Return all contacts in a printable format."""
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> int:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            return 0
        if command == "hello":
            print("How can I help you?")
            continue
        if command == "add":
            print(add_contact(args, contacts))
            continue
        if command == "change":
            print(change_contact(args, contacts))
            continue
        if command == "phone":
            print(show_phone(args, contacts))
            continue
        if command == "all":
            print(show_all(contacts))
            continue

        print("Invalid command.")


if __name__ == "__main__":
    raise SystemExit(main())
