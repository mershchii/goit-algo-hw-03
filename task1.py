from datetime import datetime


# Створюємо ф-цію get_days_from_today() яка:
#   - Приймає date --> яку вводить користувач
#   - Ф-ція перетіорює дату на кількість днів (ігнорує години, хвилини, секунди)
#   - Рахує різницю між датою вводу та сьогодіншньою датою та повертає результат

date = "2025-02-14"

def get_days_from_today(date: str) -> int:   

    while True:
        try:                                
            date_datetime = datetime.strptime(date, "%Y-%m-%d").date().toordinal()
            return datetime.today().date().toordinal() - date_datetime
        except ValueError:                  
            print("Дата некореткна")
            break
    
print(get_days_from_today(date))                                    