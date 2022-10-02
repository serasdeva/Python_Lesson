# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

from random import random


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


# Вызов функции к первой задаче
# sum_float_number()

# ----------------------------------------------------------------------------------------------------

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def func_fibo():
    number = int(input('Введите число --> '))

    start_value = 1
    list_nums = []

    for i in range(1, number + 1):
        start_value *= i
        list_nums.append(start_value)

    print(number, '->', list_nums)


# Вызов функции к второй задаче
# func_fibo()

# ----------------------------------------------------------------------------------------------------

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

# Вызов функции к третьей задаче
# sum_list_nums()


# 4. * Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

def two_element():
    position_1 = int(input('Position one: '))
    position_2 = int(input('Position two: '))
    number = int(input('Number of elements: '))
    list_numbers = []

    for i in range(-number, number+1):
        list_numbers.append(i)

    print(list_numbers)
    sum = int(list_numbers[position_1 - 1]) * int(list_numbers[position_2 - 1])

    print(sum)


# Вызов функции к четвертой задаче со звездочкой
# two_element()

# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

def fill_unsorted_list():
    number = int(input('Введите длину списка: '))
    unmixed_list = []
    if number > 0:
        for i in range(number):
            unmixed_list.append(i)
    elif number < 0:
        for i in range(number+1, 1):
            unmixed_list.append(i)

    print('Неперемешанный -> ', unmixed_list)
    return unmixed_list


def my_random(unmixed_list):
    from random import randint as rand

    len_unsorted_list = len(unmixed_list)
    for i in range(len_unsorted_list):
        randomer = rand(0, len_unsorted_list-1)
        unmixed_list[i], unmixed_list[randomer] = unmixed_list[randomer], unmixed_list[i]

    print('Перемешанный список -> ', unmixed_list)


my_random(fill_unsorted_list())
