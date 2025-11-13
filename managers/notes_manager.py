from models.notes.notebook import Notebook
from state_storage_manager import StateStorageManager

class NotesManager:
    def __init__(self):
        self.__notebook = Notebook()
        # todo: store state on hard drive using StateStorageManager("notes_cache.pkl")

    def add_note(self, note: str):
        pass

    def find(self, title: str):
        pass

    def delete(self, title: str):
        pass
