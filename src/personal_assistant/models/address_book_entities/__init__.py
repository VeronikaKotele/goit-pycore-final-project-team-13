"""Address Book Entities Package

This package contains the entity classes that represent individual components
of contact records in the Personal Assistant Bot's address book.

Entities:
    AddressBookRecord: Complete contact record containing name and associated data
    Phone: Phone number field with validation (10-digit format)
    Birthday: Birthday field with date validation and age calculation
    HomeAddress: Address field for storing contact addresses
    Email: Email field with format validation

Each entity class includes:
- Input validation specific to the data type
- String representation methods
- Comparison and equality operations where appropriate
- Error handling for invalid data

These entities form the building blocks of the address book system,
ensuring data integrity and providing consistent interfaces for
contact information management.
"""

from .address_book_record import AddressBookRecord
from .address import HomeAddress
from .phone import Phone
from .birthday import Birthday
from .email import Email

__all__ = ['AddressBookRecord', 'HomeAddress', 'Phone', 'Birthday', 'Email']