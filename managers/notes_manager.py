from models.notes.notebook import Notebook

class NotesManager:
    def __init__(self):
        self.__notebook = Notebook()

    def add_note(self, title: str, note: str):
        pass

    def find(self, title: str):
        return self.__notebook.get(title) or None

    def delete(self, title: str):
        pass
