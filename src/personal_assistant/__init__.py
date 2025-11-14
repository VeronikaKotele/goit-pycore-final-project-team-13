"""Personal Assistant Bot - Root Package

This is the main package for the Personal Assistant Bot application.
The bot provides functionality to manage contacts and notes through an interactive
command-line interface.

The package includes:
- Contact management with phone numbers, addresses, emails, and birthdays
- Note-taking functionality with search and editing capabilities
- Data persistence and validation

Modules:
    managers: Contains manager classes for handling business logic
    models: Contains data models for contacts, notes, and related entities
    commands: Command handlers for user interactions
    commands_palette: Command palette for mapping user inputs to commands
    main: Entry point for the application

Authors: Team 13 (Veronika, Ilona, Vitalii)
Project: GoIT Python Core Final Project
"""

from . import commands
from . import commands_palette
from .managers import AddressBookManager, NotesManager
from .models import AddressBook, Notebook, AddressBookRecord, HomeAddress, Phone, Birthday

__all__ = ['models', 'commands', 'commands_palette', 'AddressBookManager', 'NotesManager', 'AddressBook', 'Notebook', 'AddressBookRecord', 'HomeAddress', 'Phone', 'Birthday', 'commands', 'commands_palette']