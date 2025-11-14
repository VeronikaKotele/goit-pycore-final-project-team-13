from models.contacts.address_book_record import AddressBookRecord
from models.cacheable_dict import CacheableDict

class AddressBook(CacheableDict):
    def __init__(self):
        CacheableDict.__init__(self, "addressbook_state.pkl")

    def __setitem__(self, name, record: AddressBookRecord):
        if not isinstance(record, AddressBookRecord):
            raise TypeError("Item must be an instance of Record")
        self.data[name] = record

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
