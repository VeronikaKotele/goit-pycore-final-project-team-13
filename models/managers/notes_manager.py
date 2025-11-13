from collections import UserDict


class NotesManager(UserDict):
    def add_note(self, note):
        self.data[note.name.value] = note

    def find(self, note: str):
        if note in self.data:
            return self.data[note]

    def delete(self, note: str):
        if note in self.data:
            del self.data[note]
