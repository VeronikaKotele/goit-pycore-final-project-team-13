from .address_book_entities import AddressBookRecord
from .interfaces.cacheable_dict import CacheableDict

class AddressBook(CacheableDict):
    """
    An address book for storing and managing contacts with automatic persistence.
    
    This class extends CacheableDict to provide a specialized storage container
    for contact records. Contacts are automatically persisted to 'addressbook_state.pkl'
    file and type validation ensures only AddressBookRecord instances are stored.
    """
    
    def __init__(self):
        CacheableDict.__init__(self, "addressbook_state.pkl")

    def __setitem__(self, name, record: AddressBookRecord):
        if not isinstance(record, AddressBookRecord):
            raise TypeError("Item must be an instance of Record")
        self.data[name] = record

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
