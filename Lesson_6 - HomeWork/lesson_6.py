# 1. Представлен список чисел. 
# Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. 
# Use comprehension.

from random import randint


def fill_list_not_compr():
    from random import randint
    try:
        num = int(input('Введите длину списка: '))
        gen_list = []
        for i in range(0, num):
            gen_list.append(randint(0, 20))

        return gen_list
    except ValueError:
        print('Неверный ввод')
        return fill_list()


def sort_list_next(list):
    sorted_list = []
    try:
        temp = list[0]
        for i in range(1, len(list)):
            if list[i] > list[i - 1]:
                sorted_list.append(list[i])

        return sorted_list
    except:
        return sorted_list


def main_not_use_compr():
    f_l = fill_list_not_compr()
    print(f_l)
    s_l = sort_list_next(f_l)
    print(s_l)

# main_not_use_compr() # Вызов функции - Not use comprehension


def fill_list():
    len_list = int(input('Введите длину списка: '))
    nums = [randint(0, 10) for i in range(len_list)]
    return nums


def sort_list(list):
    m = [j for i, j in zip(list, list[1:]) if j > i]
    return m


def main():
    f_l = fill_list()
    print(f_l)
    s_l = sort_list(f_l)
    print(s_l)


# main()  # Вызов функции - Use comprehension

# ==================================================================================

# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. 
# Use comprehension.

def nums_div():
    len_num =  int(input('Введите длину списка чисел: '))
    nums = [i for i in range(20, len_num + 1) if i % 20 == 0 or i % 21 == 0]
    return nums

#print(nums_div())  # Вызов функции

# ==================================================================================

# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "" "Бибочка"]

def dictionary_names(list):
    dictionary = {}
    for name in list:
        name_key = name[0]
        if name_key not in dictionary:
            dictionary[name_key] = []
        dictionary[name_key].append(name)
    return dictionary

print(dictionary_names(list))  # Вызов функции


