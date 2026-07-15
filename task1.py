from datetime import datetime


# Створюємо ф-цію get_days_from_today() яка:
#   - Приймає date --> яку вводить користувач
#   - Ф-ція перетіорює дату на кількість днів (ігнорує години, хвилини, секунди)
#   - Рахує різницю між датою вводу та сьогодіншньою датою та виводить в консоль різницю 

def get_days_from_today(date):
    days_from_today = datetime.today().date().toordinal() - date.toordinal()
    return days_from_today  # <-- Виправлено ф-цію, тепер повертає результат


# Перевіряємо корекність дати 
while True:
    try:                                   # Просимо ввести дату, зразу ж перетворюючи її в об'єкт datetime 
        date = datetime.strptime(input("Введіть дату в форматі 'РРРР-ММ-ДД': "), "%Y-%m-%d").date()

        result = get_days_from_today(date) # Використовуємо ф-цію та зберігаємо результат
        print(result)                      # Виводимо значення

        break                              # завершуємо цикл while
    except ValueError:                     # При неправильному вводі повідомляємо про помилку та повторюємо запит 
        print("Дата некореткна")

