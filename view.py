from Note.model import load_notes


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