"""
Address Book Module

This module provides the AddressBook class, which is a specialized CacheableDict
for storing and managing contact records. It provides automatic persistence of
contacts and type validation for stored records.

The address book stores contacts as key-value pairs where keys are contact names
and values are AddressBookRecord instances.
"""

from .address_book_entities import AddressBookRecord
from .cacheable_dict import CacheableDict

class AddressBook(CacheableDict):
    """
    An address book for storing and managing contacts with automatic persistence.
    
    This class extends CacheableDict to provide a specialized storage container
    for contact records. Contacts are automatically persisted to 'addressbook_state.pkl'
    file and type validation ensures only AddressBookRecord instances are stored.
    """
    
    def __init__(self):
        """
        Initialize an AddressBook with automatic persistence to 'addressbook_state.pkl'.
        """
        CacheableDict.__init__(self, "addressbook_state.pkl")

    def __setitem__(self, name, record: AddressBookRecord):
        """
        Set a contact record in the address book with type validation.
        
        Args:
            name (str): The contact's name (key)
            record (AddressBookRecord): The contact record to store
            
        Raises:
            TypeError: If record is not an instance of AddressBookRecord
        """
        if not isinstance(record, AddressBookRecord):
            raise TypeError("Item must be an instance of Record")
        self.data[name] = record

    def __str__(self):
        """
        Return a string representation of all contacts in the address book.
        
        Returns:
            str: A formatted string containing all contact records, one per line
        """
        return "\n".join(str(record) for record in self.data.values())
