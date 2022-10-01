# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

def sum_float_number():
    input_number = float(input('Введите вещественное число --> '))
    number = input_number
    list = []
    num_int = int(number)
    len_int_number = len(str(num_int))
    if number > 0:
        len_number = len(str(number)) - len_int_number - 1
    elif number < 0:
        number *= -1
        len_number = len(str(number)) - len_int_number

    number *= 10 ** len_number

    number = int(number)
    len_number = len(str(number))
    sum = 0
    for i in range(len_number):
        list.append(number % 10)
        sum += number % 10
        number //= 10
    print(f'Сумма цифр данного числа {input_number} равна ', '->', sum)


#Вызов функции к первой задаче
#sum_float_number()

#----------------------------------------------------------------------------------------------------

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def func_fibo():
    number = int(input('Введите число --> '))

    start_value = 1
    list_nums = []

    for i in range(1, number + 1):
        start_value *= i
        list_nums.append(start_value)

    print(number, '->', list_nums)


#Вызов функции к второй задаче
#func_fibo()

#----------------------------------------------------------------------------------------------------

# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


def sum_list_nums():
    number = int(input('Введите число --> '))

    list_nums = []
    sum = 0

    for i in range(1, number + 1):
        temp = round((1 + 1 / i) ** i)
        list_nums.append(temp)
        sum += temp

    print(list_nums, sum)

sum_list_nums()
