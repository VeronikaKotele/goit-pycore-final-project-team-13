from personal_assistant.models import Notebook

class NotesManager:
    def __init__(self):
        self.__notebook = Notebook()

    def add_note(self, title: str, note: str):
        note_exists = self.__notebook.get(title)
        if note_exists:
            raise ValueError(f"Note with title '{title}' already exists.")
        self.__notebook[title] = note

    def find(self, title: str):
        return self.__notebook.get(title) or None

    def delete(self, title: str):
        pass

    def __str__(self):
        return "\n".join(str(record) for record in self.__notebook.data.values())
