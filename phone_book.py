from easygui import *
import json

def save():
    with open("contacts.json", "w", encoding = "utf-8") as contact:
        contact.write(json.dumps(contacts, ensure_ascii = False))

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
        "email": "name2@email.internet"
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
    if len(contacts) == 0:
        title_for_notification = "Уведомление"
        message_for_notification = "Справочник пуст"
        button = "Ладно"
        msgbox(message_for_notification, title_for_notification, button)        
    elif len(contacts) == 1:
        msg_for_bbox = f"\
        Имя: {contacts[0]["name"]}\n\
        Фамилия: {contacts[0]["surname"]}\n\
        Номер телефона: {contacts[0]["phone number"]}\n\
        Дополнительный номер телефона: {contacts[0]["additional phone number"]}\n\
        Дата рождения: {contacts[0]["birthday"]}\n\
        email: {contacts[0]["email"]}\n"
        title_for_bbox = "Информация о контакте"
        choices_for_bbox = ["Изменить контакт", "Удалить контакт", "Выйти в главное меню"]
        user_choice_in_bbox = buttonbox(msg_for_bbox, title_for_bbox, choices_for_bbox)
        if user_choice_in_bbox == choices_for_bbox[0]:
            change(contacts, contacts[0])
        if user_choice_in_bbox == choices_for_bbox[1]:
            remove(contacts, contacts[0])
        if user_choice_in_bbox == choices_for_bbox[2]:
            return
    else:
        try:
            choices_of_contacts = []
            for i in contacts:
                choices_of_contacts.append(i["name"] + " " + i["surname"])
            title = "Телефонный справочник"
            msg = "Выберите контакт для получения дополнительной информации"
            user_choice = choicebox(msg, title, choices_of_contacts)
            msg_for_bbox = f"\
        Имя: {contacts[choices_of_contacts.index(user_choice)]["name"]}\n\
        Фамилия: {contacts[choices_of_contacts.index(user_choice)]["surname"]}\n\
        Номер телефона: {contacts[choices_of_contacts.index(user_choice)]["phone number"]}\n\
        Дополнительный номер телефона: {contacts[choices_of_contacts.index(user_choice)]["additional phone number"]}\n\
        Дата рождения: {contacts[choices_of_contacts.index(user_choice)]["birthday"]}\n\
        email: {contacts[choices_of_contacts.index(user_choice)]["email"]}\n"
            title_for_bbox = "Информация о контакте"
            choices_for_bbox = ["Изменить контакт", "Удалить контакт", "Назад", "Выйти в главное меню"]
            if user_choice:
                user_choice_in_bbox = buttonbox(msg_for_bbox, title_for_bbox, choices_for_bbox)
                if user_choice_in_bbox == choices_for_bbox[0]:
                    change(contacts, contacts[choices_of_contacts.index(user_choice)])
                if user_choice_in_bbox == choices_for_bbox[1]:
                    remove(contacts, contacts[choices_of_contacts.index(user_choice)])
                if user_choice_in_bbox == choices_for_bbox[2]:
                    show(contacts)
                if user_choice_in_bbox == choices_for_bbox[3]:
                    return
        except:
            return

def show_for_search(contacts, found_contacts):     
    if len(found_contacts) == 1:
        msg_for_bbox = f"\
        Имя: {found_contacts[0]["name"]}\n\
        Фамилия: {found_contacts[0]["surname"]}\n\
        Номер телефона: {found_contacts[0]["phone number"]}\n\
        Дополнительный номер телефона: {found_contacts[0]["additional phone number"]}\n\
        Дата рождения: {found_contacts[0]["birthday"]}\n\
        email: {found_contacts[0]["email"]}\n"
        title_for_bbox = "Результаты поиска"
        choices_for_bbox = ["Изменить контакт", "Удалить контакт", "Выйти в главное меню"]
        user_choice_in_bbox = buttonbox(msg_for_bbox, title_for_bbox, choices_for_bbox)
        if user_choice_in_bbox == choices_for_bbox[0]:
            change(contacts, contacts[contacts.index(found_contacts[0])])
        if user_choice_in_bbox == choices_for_bbox[1]:
            remove(contacts, contacts[contacts.index(found_contacts[0])])
        if user_choice_in_bbox == choices_for_bbox[2]:
            return
    else:
        try:
            choices_of_contacts = []
            for i in found_contacts:
                choices_of_contacts.append(i["name"] + " " + i["surname"])
            title = "Результаты поиска"
            msg = "Выберите контакт для получения дополнительной информации"
            user_choice = choicebox(msg, title, choices_of_contacts)
            msg_for_bbox = f"\
        Имя: {found_contacts[choices_of_contacts.index(user_choice)]["name"]}\n\
        Фамилия: {found_contacts[choices_of_contacts.index(user_choice)]["surname"]}\n\
        Номер телефона: {found_contacts[choices_of_contacts.index(user_choice)]["phone number"]}\n\
        Дополнительный номер телефона: {found_contacts[choices_of_contacts.index(user_choice)]["additional phone number"]}\n\
        Дата рождения: {found_contacts[choices_of_contacts.index(user_choice)]["birthday"]}\n\
        email: {found_contacts[choices_of_contacts.index(user_choice)]["email"]}\n"
            title_for_bbox = "Информация о контакте"
            choices_for_bbox = ["Изменить контакт", "Удалить контакт", "Назад", "Выйти в главное меню"]
            if user_choice:
                user_choice_in_bbox = buttonbox(msg_for_bbox, title_for_bbox, choices_for_bbox)
                if user_choice_in_bbox == choices_for_bbox[0]:
                    change(contacts, contacts[contacts.index(found_contacts[choices_of_contacts.index(user_choice)])])
                if user_choice_in_bbox == choices_for_bbox[1]:
                    remove(contacts, contacts[contacts.index(found_contacts[choices_of_contacts.index(user_choice)])])
                if user_choice_in_bbox == choices_for_bbox[2]:
                    show_for_search(contacts, found_contacts)
                if user_choice_in_bbox == choices_for_bbox[3]:
                    return
        except:
            return

def find_anything(contacts):
    try:
        msg_for_ebox = "Что ищем (введите имя, фамилию, номер телефона, дату рождения или e-mail)?"
        title_for_ebox = "Поиск"
        smth = enterbox(msg_for_ebox, title_for_ebox)
        while True:
            errmsg = ""
            if smth == "":
                errmsg = "Вы ничего не ввели"
            if errmsg == "":
                break
            smth = enterbox(errmsg, title_for_ebox)
        found_contacts = []
        for i in contacts:
            if smth.casefold() in i["name"].casefold() or smth.casefold() in i["surname"].casefold() or smth.casefold() in i["email"].casefold() or smth in i["phone number"] or smth in i["additional phone number"] or smth in i["birthday"]:
                found_contacts.append(i)
        if len(found_contacts) == 0:
            title_for_notification = "Уведомление"
            message_for_notification = "Ничего не нашлось"
            button = "Ну ладно"
            msgbox(message_for_notification, title_for_notification, button)
        else:
            show_for_search(contacts, found_contacts)
    except:
        return

def remove(contacts, contact_to_remove):
    message = f"Хотите удалить контакт {contact_to_remove["name"]} {contact_to_remove["surname"]}?"
    title = "Удаление контакта"
    choices = ["Да, удаляю", "Нет, пусть останется"]
    choice = buttonbox(message, title, choices)
    if choice == choices[0]:
        title = "Уведомление"
        message = f"Контакт {contact_to_remove["name"]} {contact_to_remove["surname"]} удалён"
        button = "Хорошо"
        msgbox(message, title, button)
        del contacts[contacts.index(contact_to_remove)]
        save()
        return contacts
    else:
        return contacts

def add(contacts):
    try:
        new_contact = { 
            "name": "",
            "surname": "",
            "phone number": "",
            "additional phone number": "",
            "birthday": "",
            "email": ""
            }
        msg = "Введите информацию о контакте"
        title = "Добавляем контакт"
        fieldNames = ["Имя", "Фамилия", "Номер телефона", "Дополнительный номер телефона", "Дата рождения", "Email"]
        fieldValues = multenterbox(msg, title, fieldNames)
        while True:
            errmsg = ""
            if fieldValues[0] == "":
                errmsg += "Давайте хотя бы введём имя\n"
            if fieldValues[2] != "":
                if fieldValues[2].isdigit() == False:
                    errmsg += "Номер телефона следует написать цифрами\n"
            if fieldValues[3] != "":
                if fieldValues[3].isdigit() == False:
                    errmsg += "Дополнительный номер телефона следует написать цифрами"
            if errmsg == "":
                break
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
        new_contact["name"] = fieldValues[0]
        new_contact["surname"] = fieldValues[1]
        new_contact["phone number"] = fieldValues[2]
        new_contact["additional phone number"] = fieldValues[3]
        new_contact["birthday"] = fieldValues[4]
        new_contact["email"] = fieldValues[5]
        contacts.append(new_contact)
        save()
        title = "Уведомление"
        message = "Контакт добавлен"
        button = "Хорошо"
        msgbox(message, title, button)
        return contacts
    except:
        return

def change(contacts, contact_to_change):
    try:
        values_to_change = list(map(lambda x: x, contact_to_change.values()))
        msg = "Заполните поля"
        title = "Изменяем информацию о контакте"
        fieldNames = ["Имя", "Фамилия", "Номер телефона", "Дополнительный номер телефона", "Дата рождения", "Email"]
        fieldValues = multenterbox(msg, title, fieldNames, values_to_change)
        while True:
            errmsg = ""
            if fieldValues[0] == "":
                errmsg += "Давайте хотя бы введём имя\n"
            if fieldValues[2] != "":
                if fieldValues[2].isdigit() == False:
                    errmsg += "Номер телефона следует написать цифрами\n"
            if fieldValues[3] != "":
                if fieldValues[3].isdigit() == False:
                    errmsg += "Дополнительный номер телефона следует написать цифрами"
            if errmsg == "":
                break
            fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
        contacts[contacts.index(contact_to_change)]["name"] = fieldValues[0]
        contacts[contacts.index(contact_to_change)]["surname"] = fieldValues[1]
        contacts[contacts.index(contact_to_change)]["phone number"] = fieldValues[2]
        contacts[contacts.index(contact_to_change)]["additional phone number"] = fieldValues[3]
        contacts[contacts.index(contact_to_change)]["birthday"] = fieldValues[4]
        contacts[contacts.index(contact_to_change)]["email"] = fieldValues[5]
        save()
        title = "Уведомление"
        message = "Наверное, Вы что-то изменили"
        button = "Возможно"
        msgbox(message, title, button)
        return contacts
    except:
        return contacts

def main_menu():
    while True:
        title = "Телефонный справочник"
        msg = "Выберите действие"
        choices = ["Посмотреть справочник", "Найти контакт", "Добавить контакт", "Сохранить и выйти"]
        user_choice = buttonbox(msg, title, choices)
        if user_choice == choices[0]:
            show(contacts)
        if user_choice == choices[1]:
            find_anything(contacts)
        if user_choice == choices[2]:
            add(contacts)
        if user_choice == choices[3]:
            save()
            title = "Уведомление"
            message = "Увидимся"
            button = "Чао"
            msgbox(message, title, button)
            break

contacts = load_contacts()
main_menu()