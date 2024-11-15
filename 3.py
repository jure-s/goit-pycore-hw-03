import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та знака '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Перевірка чи номер починається з '+'
    if cleaned_number.startswith('+'):
        # Якщо номер починається з '+', але не має коду країни
        if not cleaned_number.startswith('+38'):
            cleaned_number = '+38' + cleaned_number[1:]
    else:
        # Якщо номер не має коду країни
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    
    return cleaned_number

# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)