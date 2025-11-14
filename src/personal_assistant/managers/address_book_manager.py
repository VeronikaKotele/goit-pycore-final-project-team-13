from personal_assistant.models import AddressBook, AddressBookRecord, Phone, Birthday, HomeAddress

class AddressBookManager:
    def __init__(self):
        self.__address_book = AddressBook()

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