def choose_action(phonebook):
    while True:
        print('Что бы вы хотели сделать?: ')
        user_choice = input('1 - Добавить контакт\n2 - Найти контакт\n3 - Распечтать все контакты\n0 - Выход\n4 - Импортировать контакты\n')
        print()
        if user_choice == '1':
            add_new_name(phonebook)
        elif user_choice == '2':
            contact_list = find_contact_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            contact_list = find_contact_dict(phonebook)
            print_contacts(contact_list)
        elif user_choice == '4':
             file_to_add = input('Введите название импортируемого файла: ')
             contact_list = find_contact_dict(file_to_add)
             print_contacts(contact_list)
             found_contacts = find_number(contact_list)
             copy_name(phonebook, found_contacts)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

def copy_name(file_name, found_contacts):
    info_ = []
    for word in found_contacts:
        for v in word.values():
            info_.append(v)
    info = ' '.join(info_)
    with open(file_name, 'a', encoding='utf-8') as file:
         file.write(f'{info}\n')

def add_new_name(file_name):
    numbers_of_line = input('Введите номер строки: ')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    info_ = [numbers_of_line, last_name,first_name, phone_number]
    info = ' '.join(info_)
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}', end='')

def find_contact_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
         lines = file.readlines()
    headers = ['№', 'Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list

def search_parameters():
    print('По какому значению искать контакт?: ')
    searching_field = input('1 - Номер строки \n' '2 - Фамилия\n' '3 - Имя\n' '4 - Номер\n')
    search_value = None
    if searching_field == '1':
        search_value = input('Введите номер строки: ')
    if searching_field == '2':
       search_value = input('Введите фамилию: ')
    if searching_field == '3':
        search_value = input('Введите имя: ')
    if searching_field == '4':
        search_value = input('Введите номер: ')
    return searching_field, search_value

def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': '№', '2': 'Фамилия', '3': 'Имя', '4': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:   # перебор словарей
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
        return found_contacts
    print()


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)