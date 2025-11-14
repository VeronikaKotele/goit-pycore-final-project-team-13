"""Models Package

This package contains the data models and entity classes for the Personal
Assistant Bot application.

The models provide:
- Data structures for contacts, notes, and related entities
- Validation logic for phone numbers, emails, and dates
- Persistence capabilities through serialization
- Search and filtering functionality

Main Classes:
    AddressBook: Container for managing contact records
    Notebook: Container for managing notes
    AddressBookRecord: Individual contact record
    Phone: Phone number with validation
    Birthday: Birthday date with validation
    HomeAddress: Address information

The models use proper encapsulation and validation to ensure data integrity
and provide a robust foundation for the application's functionality.
"""

from .address_book import AddressBook
from .notebook import Notebook
from .address_book_entities import AddressBookRecord, Phone, Birthday, HomeAddress

__all__ = ['AddressBook', 'Notebook', 'AddressBookRecord', 'HomeAddress', 'Phone', 'Birthday']