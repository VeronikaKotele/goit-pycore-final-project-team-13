from models.notes.notebook import Notebook
from state_storage_manager import StateStorageManager

class NotesManager:
    def __init__(self):
        self.__notebook = Notebook()
        self.__storage_manager = StateStorageManager("notes_cache.pkl")
        if self.__storage_manager.try_load(self.__notebook):
            print("Notebook loaded from cache.")

    def __del__(self):
        self.__storage_manager.save(self.__notebook)

    def add_note(self, note: str):
        pass

    def find(self, title: str):
        pass

    def delete(self, title: str):
        pass
