#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не #индексах).


from unittest import result


def fill_list(number):
    list = []
    from random import randint
    for i in range(0, number):
        temp = randint(-10, 10)
        list.append(temp)
    return list


def search_amount(list):
    s = 0
    len_ls = len(list)
    for i in range(0, len_ls, 2):
        s += list[i]
    return s


#ls = fill_list(int(input('Введите число --> ')))
#s = search_amount(ls)
#print(f'*{ls} -> {s}')

#---------------------------------------------------------------

#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.


def sum_pairs_numbers(list):
    s = 0
    list_2 = []
    len_ls = len(list)
    for i in range(0, len_ls // 2):
        list_2.append(list[i] + list[(len_ls - 1) - i])

    if len(list) % 2 != 0:
        list_2.append(list[(len_ls // 2)])

    return list_2


#ls = fill_list(int(input('Введите число --> ')))
#s = sum_pairs_numbers(ls)
#print(f'*{ls} -> {s}')

#---------------------------------------------------------------

#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.Без использования #встроенной функции преобразования, без строк.


def conv_to_binary_number(number):
    temp = 0
    nules = []
    result = []
    while number:
        temp = temp * 10 + (number % 2)
        nules.append(number % 2)
        #result = int(''.join(map(str, nules)))
        number //= 2

    for i in range(0, len(nules)):
        n = nules[(len(nules) - i) - 1]
        result.append(n)
    print(*result)
    temp = revers_binary(temp)
    return temp


def revers_binary(temp):
    number = 0
    while temp:
        number = number * 10 + (temp % 10)
        temp //= 10
    return number


#t = conv_to_binary_number(int(input('Введите число --> ')))
#print(t)
##print(revers_binary(t))

#====================================================================

#4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением #дробной части элементов.

def fill_float_list(number):
    list = []
    from random import randint, random
    for i in range(0, number):
        temp = round(randint(0, 10) * random(), 2)
        list.append(temp)
    return list


def search_amount():
    list = fill_float_list(int(input('Введите число --> ')))
    min = round(list[0] % 1, 2)
    max = round(list[0] % 1, 2)
    len_ls = len(list)
    new_list = []
    for i in range(len_ls):
        new_list.append(round(list[i] % 1, 2))
        if new_list[i] < min:
            min = round(new_list[i], 2)
        elif new_list[i] > max:
            max = round(new_list[i], 2)

    result = round(max-min, 2)
    print(f'{list} \n Min: {min}, Max: {max} Difference: {result}')


#search_amount()
