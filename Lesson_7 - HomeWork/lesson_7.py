
def read_sprav():
    with open('spravochnik.txt', 'r', encoding='utf-8') as fil:
        for line in fil.readlines():
            print(line, end='')


def write_sprav():
    with open('spravochnik.txt', 'a', encoding='utf-8') as fil:
        sec_name= input("Введите фамилию: ")
        name= input("Введите имя: ")
        phone= input("Введите номер телефона: ")
        descript = input("Введите описание: ")
        print(f"{sec_name} {name} - {phone}: {descript}", file=fil)


def menu():
    
    while True:
        try:
            num = int(input("1. Прочитать телефонный справочник\n"
                        "2. Добавить запись в справочник\n"
                        "0. Выход\n"))
            if num == 1:
                read_sprav()
            elif num == 2:
                write_sprav()
            elif num == 0:
                break
            else:
                print("Вы ввели не то")
        except:
            print("Вы ввели не то")


menu()