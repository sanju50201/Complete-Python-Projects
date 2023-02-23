class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self):
        title = input("Enter the note title: ")
        content = input("Enter the note content: ")
        note = Note(title, content)
        self.notes.append(note)

    def delete_note_by_title(self):
        title = input("Enter the note title to delete: ")
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print(f"{title} has been deleted.")
                return
        print(f"Note with title '{title}' not found.")

    def edit_note_by_title(self):
        title = input("Enter the note title to edit: ")
        for note in self.notes:
            if note.title == title:
                new_content = input("Enter the new content: ")
                note.content = new_content
                print(f"{title} has been updated.")
                return
        print(f"Note with title '{title}' not found.")

    def print_all_notes(self):
        if not self.notes:
            print("No notes found.")
            return
        for note in self.notes:
            print(f"{note.title}: {note.content}")


def main():
    notes_app = NotesApp()
    while True:
        print("What would you like to do?")
        print("1. Add a new note")
        print("2. Delete a note by title")
        print("3. Edit a note by title")
        print("4. Print all notes")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            notes_app.add_note()
        elif choice == "2":
            notes_app.delete_note_by_title()
        elif choice == "3":
            notes_app.edit_note_by_title()
        elif choice == "4":
            notes_app.print_all_notes()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
