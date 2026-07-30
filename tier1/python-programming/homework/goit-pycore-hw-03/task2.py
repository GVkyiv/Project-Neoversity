import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
 
    if min < 1 or max > 1000 or min > max: #Діапозон чісел
        return []

    available_numbers = max - min + 1
    if quantity < 1 or quantity > available_numbers: # Перевірка унікальності та заборона 0 та-  
        return []

    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 666, 13) # Ніжня та верхня межа та кількисть чичел
    print("Ваші лотерейні числа:", lottery_numbers)
