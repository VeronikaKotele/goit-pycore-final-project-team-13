from models.contacts.address import HomeAddress
from models.contacts.address_book import AddressBook
from models.contacts.adress_book_record import AddressBookRecord
from models.contacts.phone import Phone
from models.contacts.birthday import Birthday
from state_storage_manager import StateStorageManager

class AddressBookManager:
    def __init__(self):
        self.__address_book = AddressBook()
        # todo: store state on hard drive using StateStorageManager("address_book_cache.pkl")

    def add_record(self, record: AddressBookRecord):
        pass

    def find(self, name: str):
        pass
    
    def delete(self, name: str):
        pass

    def add_phone(self, name: str, phone: Phone):
        pass

    def remove_phone(self, name: str, phone: Phone):
        pass

    def add_birthday(self, name: str, birthday: Birthday):
        pass

    def add_address(self, name: str, address: HomeAddress):
        pass

    def get_upcoming_birthdays(self, next_days = 7):
        pass