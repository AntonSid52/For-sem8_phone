from csv import DictReader, DictWriter
from os.path import exists

def get_info():

    is_valid_first_name = False
    is_valid_last_name = False
    is_valid_number = False
    while not is_valid_first_name:
        first_name = input('Введите имя: ')
        if len(first_name) < 2:
            print('Имя введено некорректно')
            continue
        elif not first_name.isalpha():
            print('Имя должно состоять из букв')
            continue
        else:
            is_valid_first_name = True
    while not is_valid_last_name:
        last_name = input('Введите фамилию: ')
        if len(last_name) == 0:
            print('Необходимо ввести фамилию!')
            continue
        else:
            is_valid_last_name = True
    while not is_valid_number:
        phone_number = input('Введите номер: ')
        if len(str(phone_number)) != 11:
            print('Невалидная длина')
            continue
        elif phone_number.isdigit():
            is_valid_number = True 
        else:
            print('Номер телефона должен состоять из цифр!')  
    return[first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['Телефон'] == user_data[2]:
            print('Такой пользователь уже существует!')
            return
    obj = {'Имя':user_data[0], 'Фамилия':user_data[1], 'Телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def change_contact(file_name):
    res = read_file(file_name)
    index_change = int(input('Введите номер строки для изменения: '))
    if index_change > len(res):
        print('Такой строки не существует!')
        return
    else:
        print(f'Контакт {res[index_change-1]}  будет изменен')
        el_change = int(input('Что вы хотите изменить (имя - 1, фамилию - 2, номер телефона - 3): '))
        if el_change == 1:
            name = input('Введите новое имя: ')
            res[index_change-1]['Имя'] = name
        elif el_change == 2:
            name = input('Введите новую фамилию: ')
            res[index_change-1]['Фамилия'] = name
        elif el_change == 3:
            name = int(input('Введите новый номер телефона: '))
            res[index_change-1]['Телефон'] = name
        with open(file_name, 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
            f_writer.writeheader()  
            f_writer.writerows(res)
        print("Контакт успешно изменен")

def delete_contact(file_name):
    res = read_file(file_name)
    index_delete = int(input("Введите номер строки для удаления: "))
    if index_delete > len(res):
        print('Такой строки не существует!')
        return
    print(f'Контакт {res[index_delete-1]}  будет удален')
    res.pop(index_delete-1)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()  
        f_writer.writerows(res) 

def copy_in_file(file_name, user_file_name):
    res_main = read_file(file_name)
    res_user = read_file(user_file_name)
    index_copy = int(input('Введите номер строки для копирования: '))
    if index_copy > len(res_main):
        print('Такой строки не существует!')
        return
    res_user.append(res_main[index_copy-1])
    with open(user_file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()  
        f_writer.writerows(res_user)

def copy_from_file(file_name, user_file_name):
    res_main = read_file(file_name)
    res_user = read_file(user_file_name)
    index_copy = int(input('Введите номер строки для копирования: '))
    if index_copy > len(res_user):
        print('Такой строки не существует!')
        return
    for el in res_main:
        if el['Телефон'] == res_user[index_copy-1]['Телефон']:
            print('Такой пользователь уже существует!')
            return
    res_main.append(res_user[index_copy-1])
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()  
        f_writer.writerows(res_main)

file_name = 'phone.csv'

def main():
    while True:
        print('Список команд:')
        print('r - Вывести телефонный справочник на экран')
        print('w - Внести новые данные')
        print('copy - Сделать копию данных')
        print('ch - Внести изменения в справочник')
        print('del - Удалить данные из справочника')
        print('q - Выход из программы')
        command = input('Введите команду: ')
        if command =='q':
            print('Спасибо за использавание нашего справочника. До свидания!')
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command =='r':
            if not exists(file_name): 
                print('Файл не создан, создайте его')
                continue
            print(read_file(file_name))
        elif command == 'ch':
            change_contact(file_name)
        elif command == 'del':
            delete_contact(file_name)
        elif command == 'copy':
            user_choiсe = int(input('Вы хотите скопировать контакт в новый файл - 1 или скопировать контакт из файла - 2?: '))
            user_file_name = input('Укажите имя файла: ')
            if user_choiсe == 1:
                if not exists(user_file_name): 
                    create_file(user_file_name)
                copy_in_file(file_name, user_file_name)
            elif user_choiсe == 2:
                if not exists(user_file_name): 
                    print('Такого файла не существует, создайте его')
                else:
                    copy_from_file(file_name, user_file_name)
        else:
            print('Такой команды не существует')
main()


