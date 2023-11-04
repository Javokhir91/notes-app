from view import *
from model import *


def start():
    while True:

        choice = menu()
        match choice:
            case 1:
                title = input("Введите заголовок заметки: ")
                message = input("Введите тело заметки: ")
                add_note(title, message)
            case 2:
                list_notes()
            case 3:
                note_id = int(input("Введите ID заметки: "))
                view_note(note_id)
            case 4:
                note_id = int(input("Введите ID заметки для редактирования: "))
                new_title = input("Введите новый заголовок заметки: ")
                new_message = input("Введите новое тело заметки: ")
                edit_note(note_id, new_title, new_message)
            case 5:
                note_id = int(input("Введите ID заметки для удаления: "))
                delete_note(note_id)
            case 6:
                print("Выход из программы.")
                break
