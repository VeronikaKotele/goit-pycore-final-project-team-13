from personal_assistant.models import Notebook, Note


class NotesManager:
    def __init__(self):
        self.__notebook = Notebook()

    def add_note(self, title: str, content: str):
        note_exists = self.__notebook.get(title)
        if note_exists:
            raise ValueError(f"Note with title '{title}' already exists.")
        self.__notebook[title] = Note(title, content)

    def update(self, title: str, content: str):
        if title in self.__notebook:
            self.__notebook[title].content = content
        else:
            raise KeyError(f"Note with title '{title}' not found.")

    def find(self, title: str) -> Note | None:
        return self.__notebook.get(title) or None

    def delete(self, title: str):
        if title in self.__notebook:
            del self.__notebook[title]
        else:
            raise KeyError(f"Note with title '{title}' not found.")
        
    def add_tag(self, title: str, tag: str):
        if title in self.__notebook:
            self.__notebook[title].add_tag(tag)
        else:
            raise KeyError(f"Note with title '{title}' not found.")
    
    def search_by_tag(self, tag: str) -> list[Note]:
        return [note for note in self.__notebook.values() if tag in note.tags]

    def get_all_notes(self) -> list[str]:
        return list(str(note) for title, note in self.__notebook.data.items())

    def save_data(self):
        self.__notebook.save_data_to_cache()