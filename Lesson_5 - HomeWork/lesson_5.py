# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

from typing import Text


def fill_list():
    from random import sample

    number = int(input('Number of words: '))
    if number <= 0:
        return 0
    #sources = input('Введите текст: ')    # Для произвольного ввода слова
    sources = 'абв'
    list = []
    for i in range(number):
        temp = sample(sources, k=3)
        list.append(''.join(temp))
    s = ' '.join(list)
    print(s)

    return s


def fined_words():
    list = fill_list()
    if not list:
        return print('The data is incorrect')
    else:
        #find_word = input('Введите удаляемое слово: ') # Произвольный выбор удаления слова
        find_word = 'абв'
        lst = [i for i in list.split() if find_word not in i]
        print(f'Результат: {" ".join(lst)}')


fined_words()  # Вызов функции для первого примера

# =====================================================================

# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'


def main():

    def encoding_text(text):
        count = 1
        encode_text = ''
        char_befor = ''

        for i in text:
            if i != char_befor:
                if char_befor != '':
                    encode_text += str(count) + char_befor
                char_befor = i
                count = 1
            else:
                count += 1
        encode_text += str(count) + char_befor
        return encode_text


    def decoding_text(text):
        decode_text = ''
        number = 1
        for i in text:
            if i.isdigit():
                number = int(i)
                # print(type(number))
            else:
                decode_text += i * number
        return decode_text


    def read_write_text_en():
        file_en = input('Enter the file name to record: ')
        try:
            with open(file, 'r') as f_read,  open(file_en, 'a') as f_en_write:
                list = ''
                for line in f_read:
                    list = ''.join(line + '\n')
                    en = encoding_text(list)
                    print(en)
                    f_en_write.write(en)

            return list
        except:
            print('Sorry, please enter the correct file name')
            return ''


    def read_write_text_d():
        file_de = input('Enter the name of the file to decode: ')
        print(f"'{file_de}'")
        try:
            with open(file, 'r') as f_read,  open(file_de, 'w') as f_de_write:
                list = ''
                for line in f_read:
                    list = ''.join(line)
                    de = decoding_text(list)
                    print(de)
                    f_de_write.write(de)
            return list
        except:
            print('Sorry, please enter the correct file name')
            return ''

    file = input('Enter the name of the file with the text: ')
    read_write_text_en()
    read_write_text_d()

#main()  # Вызов функции для вторго примера
