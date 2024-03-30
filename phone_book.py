import json
from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')

def save():
    with open("contacts.json", "w", encoding = "utf-8") as contact:
        contact.write(json.dumps(contacts, ensure_ascii = False))
    clear()
    print("Cохранение файла успешно")

def load_contacts():
    try:
        with open("contacts.json", "r", encoding = "utf-8") as contact:
            contacts = json.load(contact)
    except:
        contacts = [
        { 
        "name": "Миша",
        "surname": "Петров",
        "phone number": "123456789",
        "additional phone number": "23402340",
        "birthday": "01.01.2000",
        "email": "name1@email.internet"
        },
        {
        "name": "Славик",
        "surname": "",
        "phone number": "78904563",
        "additional phone number": "",
        "birthday": "02.02.2002",
        "email": "name1@email.internet"
        },
        {
        "name": "Юра",
        "surname": "Иванов",
        "phone number": "45632107",
        "additional phone number": "3695214",
        "birthday": "03.03.2003",
        "email": ""
        }
        ]
    return contacts

def show(contacts):
    clear()
    for i in contacts:
        for k, v in i.items():
            print("{0}: {1}".format(k, v))
        print("___________")

def find_anything(contacts):
    clear()
    smth = input("Что ищем (введите имя, фамилию, номер телефона, дату рождения или e-mail)? ")
    if smth == "":
        print("Вы ничего не ввели")
        return
    flag = False
    for i in contacts:
        if smth.casefold() in i["name"].casefold() or smth.casefold() in i["surname"].casefold() or smth.casefold() in i["email"].casefold() or smth in i["phone number"] or smth in i["additional phone number"] or smth in i["birthday"]:
            flag = True
            for k, v in i.items():
                print(f"{k}: {v}")
            print("___________")
    if flag == False:
        print("Ничего не нашлось")
     
def remove(contacts):
    clear()
    print("Введите порядковый номер контакта, который хотите удалить")
    for i in range(len(contacts)):
        print(f"{i + 1} - {contacts[i]["name"]} {contacts[i]["surname"]}")
    print("Чтобы выйти в меню, введите 0")
    while True:
        try:
            choice = int(input())
            if choice == 0:
                break
            elif choice > 0 and choice <= len(contacts):
                print(f"Контакт {contacts[choice - 1]["name"]} {contacts[choice - 1]["surname"]} удалён")
                del contacts[choice - 1]
                break
            else:
                print("Что-то не то ввели, попробуйте ещё раз")   
        except:
            print("Что-то не то ввели, попробуйте ещё раз")
    return contacts

def add(contacts):
    clear()
    new_contact = { 
        "name": "",
        "surname": "",
        "phone number": "",
        "additional phone number": "",
        "birthday": "",
        "email": ""
        }
    new_contact["name"] = input("Введите имя: ")
    new_contact["surname"] = input("Введите фамилию: ")
    new_contact["phone number"] = input("Введите номер телефона: ")
    new_contact["additional phone number"] = input("Введите дополнительный номер телефона: ")
    new_contact["birthday"] = input("Введите дату рождения: ")
    new_contact["email"] = input("Введите e-mail: ")
    contacts.append(new_contact)
    print("Контакт добавлен")
    return contacts

def change(contacts):
    clear()
    print("Введите порядковый номер контакта, который хотите изменить")
    for i in range(len(contacts)):
        print(f"{i + 1} - {contacts[i]["name"]} {contacts[i]["surname"]}")
    print("Чтобы выйти в меню, введите 0")
    while True:
        try:
            choice = int(input())
            if choice == 0:
                break
            elif choice > 0 and choice <= len(contacts):
                print(f"Вы выбрали контакт {contacts[choice - 1]["name"]} {contacts[choice - 1]["surname"]}")
                new_name = input("Введите имя: ")
                if new_name == "":
                    print("Не изменено")
                else:
                    contacts[choice - 1]["name"] = new_name
                new_surname = input("Введите фамилию: ")
                if new_surname == "":
                    print("Не изменено")
                else:
                    contacts[choice - 1]["surname"] = new_surname
                new_phone_number = input("Введите номер телефона: ")
                if new_phone_number == "":
                    print("Не изменено")
                else:
                    contacts[choice - 1]["phone number"] = new_phone_number
                new_additional_phone_number = input("Введите дополнительный номер телефона: ")
                if new_additional_phone_number == "":
                    print("Не изменено")
                else:
                    contacts[choice - 1]["additional phone number"] = new_additional_phone_number
                new_birthday = input("Введите дату рождения: ")
                if new_birthday == "":
                    print("Не изменено")
                else:
                    contacts[choice - 1]["birthday"] = new_birthday
                new_email = input("Введите e-mail: ")
                if new_email == "":
                    print("Не изменено")
                else:
                    contacts[choice - 1]["email"] = new_email
                break
            else:
                print("Что-то не то ввели, попробуйте ещё раз")   
        except:
            print("Что-то не то ввели, попробуйте ещё раз")
    return contacts

contacts = load_contacts()

while True:
    user_choice = input("\
            Введите символ, чтобы выбрать действие:\n\
            1 - Посмотреть справочник\n\
            2 - Найти контакт\n\
            3 - Добавить контакт\n\
            4 - Изменить контакт\n\
            5 - Удалить контакт\n\
            Чтобы выйти, введите любой иной символ\n")
    if user_choice == "1":
        show(contacts)
    elif user_choice == "2":
        find_anything(contacts)
    elif user_choice == "3":
        add(contacts)
        save()
    elif user_choice == "4":
        change(contacts)
        save()
    elif user_choice == "5":
        remove(contacts)
        save()
    else:
        save()
        print("Увидимся")
        break