import random

numbers = set()

#    Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
#    Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

def correct_input():

    while True:
        try:    
            min = int(input("Введіть мінімальне значення не менше 1: "))
            max = int(input("Введіть максимальне значення не більше 1000: "))
            quantity = int(input(f"Введіть кількість чисел не менше {min} та не більше {max}: "))

            if min < 1 or max > 1000 or min > max: 
                print("Некоректне мінімальне чи максимальне значення. Повторіть спробу!")
            elif quantity < min or quantity > max: 
                print("Некоректна кількість чисел. Повторіть спробу!")
            else:
                return min, max, quantity
        except ValueError:
            print("Введіть ціле число!!!")

def get_numbers_ticket(min, max, quantity):

    while len(numbers) < quantity:
        num = random.randint(min, max+1)
        numbers.add(num)
    print(sorted(numbers))



get_numbers_ticket(*correct_input())
