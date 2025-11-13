from phone import Phone
from birthday import Birthday
from address import HomeAddress

class AddressBookRecord:
    def __init__(self, name: str):
        self.name = name
        self.phones = []
        self.birthday = None
        self.address = None

    def add_phone(self, phone: Phone):
        pass

    def add_birthday(self, date: Birthday):
        pass

    def add_address(self, address: HomeAddress):
        pass
    
    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        pass

    def find_phone(self, number: Phone):
        pass

    def __str__(self):
        pass
