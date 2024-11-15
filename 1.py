from datetime import datetime

def get_days_from_today(date):
    # перетворення введеної дати
    our_date = datetime.strptime(date, "%d.%m.%y")
    # поточна дата
    current_date = datetime.now()
    # обчислення кількості днів
    return (current_date - our_date).days

# Тестові дати
print(get_days_from_today("20.11.24"))  # дата в форматі "дд.мм.рр"
print(get_days_from_today("30.11.24"))  # також перевірка на некоректну дату