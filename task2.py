import random

#    Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
#    Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

min = random.randint(1, 1000)                # Генеруємо випадкове число min
max = random.randint(1, 1000)                # Генеруємо випадкове число max
quantity = random.randint(1, 10)             # Генеруємо випадкове число quantity

def get_numbers_ticket(min, max, quantity):

    numbers = set()                          # Задаємо пусту множину 


    if min < 1 or max > 1000 or min >= max or min > 1000 or max < 1 or max-min < quantity:  # перевіряємо значення 
        print("Некоректні дані")             # якщо дані невалідні, повертається пустий список
        return numbers                       
    else:                                    # Якщо валідні, повертається множина з відсортованими та унікольними числами 
        while len(numbers) < quantity:   
            num = random.randint(min, max)
            numbers.add(num)
        return sorted(numbers)

# Перевіряємо роботу ф-ції 
print("-"*16)
print("min     : ", min)
print("max     : ", max)
print("quantity: ", quantity)
print("-"*16)
print(get_numbers_ticket(min, max, quantity))