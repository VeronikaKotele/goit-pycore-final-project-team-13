from models.managers.address_book_manager import AddressBook
from models.managers.notes_manager import Notes

class PersonalAssistance():
    def __init__(self):
        self.adrress_book = AddressBook
        self.notes = Notes