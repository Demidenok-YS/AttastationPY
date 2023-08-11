import json
import os
import datetime

def save_notes(notes, filename):
    with open(filename, 'w') as file:
        json.dump(notes, file, default=str)

def load_notes(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def list_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Дата/время: {note['timestamp']}")
        print('-' * 20)

def add_note(notes, title, body):
    if not notes:
        new_id = 1
    else:
        new_id = max(note['id'] for note in notes) + 1
    new_note = {
        'id': new_id,
        'title': title,
        'body': body,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(new_note)
    return notes

def find_note_by_id(notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

def edit_note(notes, note_id, new_title, new_body):
    note_to_edit = find_note_by_id(notes, note_id)
    if note_to_edit is not None:
        note_to_edit['title'] = new_title
        note_to_edit['body'] = new_body
        note_to_edit['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    else:
        print("Заметка с указанным ID не найдена.")
    return notes

def delete_note(notes, note_id):
    notes = [note for note in notes if note['id'] != note_id]
    return notes

def view_note(notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело заметки:\n{note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            return
    print("Заметка с указанным ID не найдена.")

def view_all_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки:\n{note['body']}")
        print(f"Дата/время: {note['timestamp']}")
        print('-' * 20)

def main():
    notes_filename = 'notes.json'

    notes = load_notes(notes_filename)

    while True:
        print("1. Вывести список заметок")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Просмотреть заметку")
        print("6. Просмотреть все заметки")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            list_notes(notes)
        elif choice == '2':
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            notes = add_note(notes, title, body)
            save_notes(notes, notes_filename)
        elif choice == '3':
            note_id = int(input("Введите ID заметки для редактирования: "))
            note_to_edit = find_note_by_id(notes, note_id)
            if note_to_edit is not None:
                new_title = input("Введите новый заголовок: ")
                new_body = input("Введите новый текст: ")
                notes = edit_note(notes, note_id, new_title, new_body)
                save_notes(notes, notes_filename)
            else:
                print("Заметка с указанным ID не найдена.")
        elif choice == '4':
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = delete_note(notes, note_id)
            save_notes(notes, notes_filename)
        elif choice == '5':
            note_id = int(input("Введите ID заметки для просмотра: "))
            view_note(notes, note_id)
        elif choice == '6':
            view_all_notes(notes)
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()