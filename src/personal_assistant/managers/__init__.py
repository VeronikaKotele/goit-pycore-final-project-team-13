"""Managers Package
This package contains manager classes responsible for handling the business logic
of the Personal Assistant Bot application, such as managing contacts and notes.
Exposed classes:
- AddressBookManager: Handles operations related to contacts, including adding,
  editing, searching, and deleting contact information.
- NotesManager: Manages note-taking functionality, including creating, editing,
  searching, and deleting notes.
"""

from .address_book_manager import AddressBookManager
from .notes_manager import NotesManager

__all__ = ['AddressBookManager', 'NotesManager']