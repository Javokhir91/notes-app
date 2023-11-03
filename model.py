# Путь к файлу, в котором будут храниться заметки
import json
import os
from datetime import datetime

PATH = "notes.json"

# Проверка существования файла и его создание, если он не существует
if not os.path.exists(PATH):
    with open(PATH, "w") as file:
        json.dump([], file)


def load_notes():
    """Загрузка заметок из JSON файла."""
    with open(PATH, "r") as file:
        return json.load(file)


def save_notes(notes):
    """Сохранение заметок в JSON файл."""
    with open(PATH, "w") as file:
        json.dump(notes, file, indent=4)


def add_note(title, message):
    """Добавление новой заметки."""
    notes = load_notes()
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")


def edit_note(note_id, new_title, new_message):
    """Редактирование существующей заметки по ее ID."""
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["message"] = new_message
            note["timestamp"] = datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print(f"Заметка с ID {note_id} не найдена.")


def delete_note(note_id):
    """Удаление существующей заметки по ее ID."""
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print(f"Заметка с ID {note_id} не найдена.")
