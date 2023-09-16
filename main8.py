
def interface_contact(phone_note = 'phone_book.txt'):
    interface_contact = int(input(
                                 '\nВведите 1 для поиска по имени\
                                 \nВведите 2 для добовления контакта\
                                 \nВведите 3 для изменения контакта\
                                  \nВведите 4 для удаления контакта\
                                 \nВведите 5 для вывода всех контактов\
                                 \nВведите 0 для выхода:'))
    while interface_contact != 0:
        if interface_contact == 1:
            search_name()
        elif interface_contact == 2:
            add_person()
        elif interface_contact == 3:
            update_contact()
        elif interface_contact == 4:
            delete_contact()
        else:
            print_contacts()
            print()
        interface_contact = int(input('\nВведите 1 для поиска по имени\
                                      \nВведите 2 для добовления контакта \
                                      \nВведите 3 для изменения контакта\
                                      \nВведите 4 для удаления контакта \
                                        \nВведите 5 для вывода всех контактов\
                                       \nВведите 0 для выхода:\n'))

def add_person():
    name = input('Введите имя: ').title()
    surname = input('Введите фамилию: ').title()
    phone = input('Введите телефон: ')
    with open('phone_book.txt', 'a', encoding='utf-8') as book:
        
         while len(phone) != 11 or not phone.isdigit():
            print('Вы ввели неправильный телефон')
            phone = input("Введите телефон: ")
         book.write('\n'  + name + ' '  + surname + ' ' +  phone)

        
def search_name():
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        name_search = input('Введите имя для поиска: ').title()
        lines = book.readlines()
        none_contact = True
        for i in lines:
            if name_search in i:
              print(' Контакт найден: ', i, end = '')
            none_contact = False
        if none_contact:     
          return "Запись не найдена"


def update_contact(phone_note = 'phone_book.txt'):
    name = input('Введите имя контакта, который хотите изменить: ').title()
    surname = input('Введите фамилия контакта, который хотите изменить: ').title()
    with open(phone_note, "r",encoding='utf-8') as book:
       lines = book.readlines()  
    desired_contact = False
    for i in range(len(lines)):
      contact_data = lines[i].strip().split()
      contact_name = contact_data[0].strip()
      contact_surname = contact_data[1].strip()
      if contact_surname == surname and contact_name == name:
          new_name = input('Введите новое имя контакта: ').title()
          new_surname = input('Введите новую фамилию контакта: ').title()
          new_phone = input('Введите новый номер телефона контакта:')
          while len(new_phone) != 11 or not new_phone.isdigit(): 
           print('Вы ввели неправильный телефон')
           phone = input('Введите новый номер телефона контакта (11 цифр ):')
          contact_data[0] = new_name
          contact_data[1] = new_surname
          contact_data[2] = new_phone
          lines[i] = ' '.join(contact_data) + '\n'
          desired_contact = True
          break
    if desired_contact:
        with open(phone_note, 'w', encoding='UTF-8') as book:
         book.writelines(lines)
        print('Контакт  обновлен.')
    else:
        print('Контакт не найден.')   

def delete_contact(phone_note = 'phone_book.txt'):
    find_name_1 = input('Введите фамилию контакта, который хотите удалить: ').title()
    find_name_2 = input('Введите имя контакта, который хотите удалить: ').title()
    with open(phone_note, 'r', encoding='UTF-8') as phone_list:
        lines = phone_list.readlines()
    with open(phone_note, 'w', encoding='UTF-8') as phone_list:
        desired_contact = False
        for line in lines:
            contact = line.strip().split(' ')
            if not ((find_name_1 in contact[0]) and (find_name_2 in contact[1])):
                phone_list.write(line)
            else:
                desired_contact = True
        if desired_contact:
            print('Контакт успешно удален.')
        else:
            print('Контакт не найден.')
 
   
            
def print_contacts():
    with open('phone_book.txt', "r",encoding='utf-8') as book:
        lines = book.readlines()
        for i in lines:
            print(i, end = '')            


interface_contact()