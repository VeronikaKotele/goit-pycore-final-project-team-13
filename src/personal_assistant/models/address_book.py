from .address_book_entities import AddressBookRecord
from collections import UserDict

class AddressBook(UserDict):
    def __setitem__(self, name, record: AddressBookRecord):
        if not isinstance(record, AddressBookRecord):
            raise TypeError("Item must be an instance of Record")
        self.data[name] = record

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
