from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must contain exactly 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError("Phone not found")

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = Phone(new_phone).value
        else:
            raise ValueError("Phone not found")

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# ===== Приклад використання =====
if __name__ == "__main__":

    book = AddressBook()

    # Діма
    dima_record = Record("Діма")
    dima_record.add_phone("0501234567")
    dima_record.add_phone("0679876543")
    book.add_record(dima_record)

    # Гена
    gena_record = Record("Гена")
    gena_record.add_phone("0505555555")
    book.add_record(gena_record)

    # Юра
    yura_record = Record("Юра")
    yura_record.add_phone("0671112233")
    book.add_record(yura_record)

    # Вивід усіх записів
    for name, record in book.data.items():
        print(record)

    # Редагування телефону Діми
    dima = book.find("Діма")
    dima.edit_phone("0501234567", "0500000000")

    print(dima)

    # Пошук конкретного телефону
    found_phone = dima.find_phone("0679876543")
    print(f"{dima.name}: {found_phone}")

    # Видалення Юри
    book.delete("Юра")
