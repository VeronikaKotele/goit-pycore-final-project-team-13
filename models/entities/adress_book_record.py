from fields.phone import Phone
from fields.field import Field
from fields.birthday import Birthday
from models.managers.notes_manager import Notes

class AddressBookRecord:
    def __init__(self, name):
        self.name = Field(name)
        self.phones = []
        self.birthday = None
        self.address = None

    def add_phone(self, phone):
        pass

    def add_birthday(self, date):
        pass

    def add_address(self, address):
        pass
    
    def edit_phone(self, old_phone, new_phone):
        pass

    def find_phone(self, number):
        pass

    def __str__(self):
        pass
    



