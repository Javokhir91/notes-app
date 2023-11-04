from model import *
import text


def list_notes():
    """Вывод списка всех заметок."""
    notes = load_notes()
    if not notes:
        print("Нет заметок.")
    else:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['timestamp']})")


def view_note(note_id):
    """Вывод конкретной заметки по ее ID."""
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            print(f"{note['title']} ({note['timestamp']}):\n{note['message']}")
            return
    print(f"Заметка с ID {note_id} не найдена.")


def menu():
    for i, item in enumerate(text.main_menu):
        if i == 0:  # if not i:
            print(item)
        else:
            print(f'\t{i}. {item}')

    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.input_menu_error)


def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')

