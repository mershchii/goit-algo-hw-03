from datetime import datetime


# Створюємо ф-цію get_days_from_today() яка:
#   - Приймає date --> яку вводить користувач
#   - Ф-ція перетіорює дату на кількість днів (ігнорує години, хвилини, секунди)
#   - Рахує різницю між датою вводу та сьогодіншньою датою та повертає результат

def get_days_from_today(date: str) -> int:    # Тепер в ф=цію date є str та повертає int
    days_from_today = datetime.today().date().toordinal() - date.toordinal()
    return days_from_today                    # <-- Виправлено ф-цію, тепер повертає результат


# Перевіряємо корекність дати 
while True:
    try:                                # Просимо ввести дату, зразу ж перетворюючи її в об'єкт datetime 
                                        # При некоректній даті, цикл повідомляє "Дата некореткна" та повторно просить ввести дату
        date = datetime.strptime(input("Введіть дату в форматі 'РРРР-ММ-ДД': "), "%Y-%m-%d").date()
        break                           # завершуємо цикл while
    except ValueError:                  
        print("Дата некореткна")

result = get_days_from_today(date)               # Застосовуємо ф-цію 
print(result)                                    # виводимо результат в термінал для зручності 