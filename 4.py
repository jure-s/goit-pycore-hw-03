from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворення дати народження на об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Рік дня народження замінюємо на поточний рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув цього року, розглядаємо його в наступному році
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Визначаємо, чи день народження настає протягом наступного тижня
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження на вихідних, переносимо його на наступний понеділок
            if birthday_this_year.weekday() >= 5:  # 5 - субота, 6 - неділя
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            
            # Додаємо до списку результатів
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Michael Brown", "birthday": "1995.01.21"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)