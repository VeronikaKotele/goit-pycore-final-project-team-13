from personal_assistant.models import Notebook

class NotesManager:
    def __init__(self):
        self.__notebook = Notebook()

    def add_note(self, title: str, content: str):
        note_exists = self.__notebook.get(title)
        if note_exists:
            raise ValueError(f"Note with title '{title}' already exists.")
        self.__notebook[title] = content

    def update(self, title: str, content: str):
        if title in self.__notebook:
            self.__notebook[title] = content
        else:
            raise KeyError(f"Note with title '{title}' not found.")

    def find(self, title: str):
        return self.__notebook.get(title) or None

    def delete(self, title: str):
        if title in self.__notebook:
            del self.__notebook[title]
        else:
            raise KeyError(f"Note with title '{title}' not found.")

    def get_all_notes(self) -> list[str]:
        return list(f"{title}: {content}" for title, content in self.__notebook.data.items())

    def __str__(self):
        return "\n".join(f"{title}: {content}" for title, content in self.__notebook.data.items())