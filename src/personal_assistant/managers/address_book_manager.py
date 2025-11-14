from personal_assistant.models import AddressBook, AddressBookRecord, Phone, Birthday, HomeAddress

class AddressBookManager:
    def __init__(self):
        self.__address_book = AddressBook()

    def add_phone(self, name: str, phone: str):
        record = self.__address_book.get(name)
        if not record:
            record = AddressBookRecord(name)
        record.add_phone(Phone(phone))
        self.__address_book[name] = record

    def find(self, name: str):
        return self.__address_book.get(name) or None

    def delete(self, name: str):
        pass

    def remove_phone(self, name: str, phone: Phone):
        pass

    def add_birthday(self, name: str, birthday: Birthday):
        pass

    def add_address(self, name: str, address: HomeAddress):
        pass

    def get_upcoming_birthdays(self, next_days = 7):
        return []
    
    def __str__(self):
        return "\n".join(str(record) for record in self.__address_book.data.values())
