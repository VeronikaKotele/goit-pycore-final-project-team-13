from models.managers.address_book_manager import AddressBookManager
from models.managers.notes_manager import NotesManager

class PersonalAssistance():
    def __init__(self):
        self.adrress_book_manager = AddressBookManager
        self.notes_manager = NotesManager