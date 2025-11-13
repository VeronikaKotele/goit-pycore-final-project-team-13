from collections import UserDict
from adress_book_record import AddressBookRecord

class AddressBook(UserDict):
    def __setitem__(self, name, record: AddressBookRecord):
        if not isinstance(record, AddressBookRecord):
            raise TypeError("Item must be an instance of Record")
        value = self.data.get(name)
        if value:
            pass # todo: define update behavior
        else:
            self.data[name] = record

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
    def update_item(self, name, record: AddressBookRecord):
        """Combine information."""
        pass
