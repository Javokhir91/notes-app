from view import *
from model import *


def start():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Просмотреть список заметок")
        print("3. Просмотреть заметку по ID")
        print("4. Редактировать заметку по ID")
        print("5. Удалить заметку по ID")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(title, message)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки: "))
            view_note(note_id)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новое тело заметки: ")
            edit_note(note_id, new_title, new_message)
        elif choice == "5":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите существующее действие.")
