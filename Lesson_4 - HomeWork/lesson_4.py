# 1. Вычислить число c заданной точностью d

def round_num():
    from decimal import Decimal
    n = input('Enter a real number: --> ')
    n2 = input('Enter the required accuracy "0.0001": --> ')

    number = Decimal(n)
    number = number.quantize(Decimal(n2))
    print(number)       # 0.44


# round_num()                # Вызов функции к задаче №1

# ==========================================================

# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def fined_list_prime_factors(number):
    from math import sqrt
    while number % 2 == 0:
        print(2,)
        number //= 2

    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            print(i,)
            number //= i
    if number > 2:
        print(number)


#fined_list_prime_factors(int(input('Введите число: --> ')))       # Вызов функции к задаче №2

# ==========================================================

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

def fill_ramdom_list():
    from random import randint

    number = int(input('Введите длину списка: --> '))
    random_list = []
    for i in range(number):
        random_list.append(randint(0, 10))

    print(random_list)

    return random_list


def fined_repeating_element(list):
    list_hash = {}
    new_list = []
    for i in range(len(list)):
        if list[i] in list_hash.keys():
            list_hash[list[i]] = 1
        else:
            list_hash[list[i]] = 0

    for key, event in list_hash.items():
        if event == 0:
            new_list.append(key)

    print(new_list)

    return new_list


fined_repeating_element(fill_ramdom_list())        # Вызов функции к задаче №3
