import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка на коректність вхідних параметрів
    if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity < 1:
        return []  # Повернення пустого списку, якщо параметри некоректні
    
    # Генерація унікального набору чисел
    numbers = sorted(random.sample(range(min, max + 1), quantity))
    
    return numbers

# Приклад виклику функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)