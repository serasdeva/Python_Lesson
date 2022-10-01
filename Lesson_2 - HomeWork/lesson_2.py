#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27

def sum_float_number():
    input_nimber = float(input('Введите вещественное число --> '))
    number = input_nimber
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
    print(f'Сумма цифр данного числа {input_nimber} равна ', '->', sum)


sum_float_number()