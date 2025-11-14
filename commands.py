"""Commands Handler Module

This module provides the CommandsHandler class which acts as the main interface
for executing user commands in the Personal Assistant Bot. It coordinates between
the address book manager and notes manager to handle all user operations.

The module defines a command system that maps user input to specific functions,
handles argument validation, and provides error handling for all operations.
"""

from managers.address_book_manager import AddressBookManager
from managers.notes_manager import NotesManager
from models.contacts.address import HomeAddress
from models.contacts.phone import Phone
from models.contacts.birthday import Birthday

class CommandsHandler:
    """
    Main command handler for the Personal Assistant Bot.
    
    This class manages all user commands by coordinating between contacts and notes
    managers. It provides a unified interface for command execution with built-in
    error handling and argument validation.
    
    The handler maintains a registry of available commands and their metadata,
    including argument requirements and descriptions for help functionality.
    
    Attributes:
        contacts_manager (AddressBookManager): Handles contact-related operations
        notes_manager (NotesManager): Handles note-related operations
        commands (dict): Registry of available commands with their metadata
    """
    
    def __init__(self):
        """
        Initialize the CommandsHandler with manager instances.
        
        Creates instances of AddressBookManager and NotesManager to handle
        contacts and notes operations respectively.
        """
        self.contacts_manager = AddressBookManager()
        self.notes_manager = NotesManager()

    def __add_phone(self, name, phone) -> str:
        """
        Add a phone number to a contact.
        
        Args:
            name (str): The contact's name
            phone (str): The phone number to add
            
        Returns:
            str: Success message confirming the phone was added
        """
        self.contacts_manager.add_phone(name, Phone(phone))
        return f"Phone {phone} added for contact {name}."

    def __remove_phone(self, name, phone) -> str:
        """
        Remove a phone number from a contact.
        
        Args:
            name (str): The contact's name
            phone (str): The phone number to remove
            
        Returns:
            str: Success message confirming the phone was removed
        """
        self.contacts_manager.remove_phone(name, Phone(phone))
        return f"Phone {phone} removed from contact {name}."

    def __add_birthday(self, name, birthday) -> str:
        """
        Add a birthday to a contact.
        
        Args:
            name (str): The contact's name
            birthday (str): The birthday in DD.MM.YYYY format
            
        Returns:
            str: Success message confirming the birthday was added
        """
        self.contacts_manager.add_birthday(name, Birthday(birthday))
        return f"Birthday {birthday} added for contact {name}."

    def __add_address(self, name, address) -> str:
        """
        Add an address to a contact.
        
        Args:
            name (str): The contact's name
            address (str): The home address to add
            
        Returns:
            str: Success message confirming the address was added
        """
        self.contacts_manager.add_address(name, HomeAddress(address))
        return f"Address {address} added for contact {name}."

    def __upcoming_birthdays(self, days) -> str:
        """
        Get upcoming birthdays within the specified number of days.
        
        Args:
            days (str): Number of days to look ahead (will be converted to int)
            
        Returns:
            str: List of upcoming birthdays or message if none found
        """
        birthdays = self.contacts_manager.get_upcoming_birthdays(int(days))
        if not birthdays:
            return "No upcoming birthdays."
        return "Upcoming birthdays:\n" + "\n".join(birthdays)

    def __show_contact(self, name) -> str:
        """
        Display details for a specific contact.
        
        Args:
            name (str): The contact's name to display
            
        Returns:
            str: String representation of the contact
            
        Raises:
            KeyError: If contact with the given name is not found
        """
        contact = self.contacts_manager.find(name)
        if not contact:
            raise KeyError(f"Contact with name '{name}' not found.")
        return str(contact)

    def __add_note(self, title, content) -> str:
        """
        Add a new note with the given title and content.
        
        Args:
            title (str): The title of the note
            content (str): The content of the note
            
        Returns:
            str: Success message confirming the note was added
        """
        self.notes_manager.add_note(title, content)
        return f"Note '{title}' added."

    def __update_note(self, title, content) -> str:
        """
        Update an existing note with new content.
        
        Args:
            title (str): The title of the note to update
            content (str): The new content for the note
            
        Returns:
            str: Success message with the updated content
            
        Raises:
            KeyError: If note with the given title is not found
        """
        note = self.notes_manager.find(title)
        if not note:
            raise KeyError(f"Note with title '{title}' not found.")
        note = content
        return f"Note '{title}' updated. New content: {self.notes_manager.find(title)}"

    def __delete_note(self, title):
        """
        Delete a note with the specified title.
        
        Args:
            title (str): The title of the note to delete
        """
        self.notes_manager.delete(title)

    def __show_note(self, title) -> str:
        """
        Display a specific note by title.
        
        Args:
            title (str): The title of the note to display
            
        Returns:
            str: The note title and content
            
        Raises:
            KeyError: If note with the given title is not found
        """
        note = self.notes_manager.find(title)
        if not note:
            raise KeyError(f"Note with title '{title}' not found.")
        return f"Note '{title}': {note}"

    def __show_all(self):
        """
        Display all contacts and notes.
        
        Returns:
            str: Formatted string containing all contacts and notes
        """
        return f"Contacts:\n{self.contacts_manager}\n\nNotes:\n{self.notes_manager}"


    class Response:
        """
        Represents a command execution response.
        
        This class encapsulates the result of a command execution, including
        the response message and whether an error occurred.
        
        Attributes:
            message (str): The response message to display to the user
            is_error (bool): True if the response represents an error condition
        """
        
        def __init__(self, message: str, is_error: bool = False):
            """
            Initialize a Response object.
            
            Args:
                message (str): The response message
                is_error (bool, optional): Whether this is an error response. Defaults to False.
            """
            self.message = message
            self.is_error = is_error


    class Command:
        """
        Represents a command with its metadata.
        
        This class stores information about a command including its function,
        argument requirements, and description for help functionality.
        
        Attributes:
            function (callable): The function to execute for this command
            arg_count (int): Number of arguments the command expects
            arguments (tuple): Names of the command arguments
            description (str): Human-readable description of the command
        """
        
        def __init__(self, function: callable, description: str):
            """
            Initialize a Command object.
            
            Args:
                function (callable): The function to execute for this command
                description (str): Description of what the command does
            """
            self.function = function
            self.arg_count = function.__code__.co_argcount - 1  # exclude 'self'
            self.arguments = function.__code__.co_varnames[1:self.arg_count + 1]  # exclude 'self'
            self.description = description


    commands = {
        "add-phone":        Command(__add_phone, "Add a phone number to a contact"),
        "add-birthday":     Command(__add_birthday, "Add a birthday to a contact"),
        "add-address":      Command(__add_address, "Add an address to a contact"),
        "remove-phone":     Command(__remove_phone, "Remove a phone number from a contact"),
        "show-contact":     Command(__show_contact, "Show contact details"),
        "birthdays":        Command(__upcoming_birthdays, "Show upcoming birthdays"),
        "add-note":         Command(__add_note, "Add a note"),
        "update-note":      Command(__update_note, "Update a note"),
        "delete-note":      Command(__delete_note, "Delete a note"),
        "show-note":        Command(__show_note, "Show a note"),
        "show-all":         Command(__show_all, "Show all contacts and notes"),
    }

    def execute_command(self, cmd_name, args) -> Response:
        """
        Execute a command with the given arguments.
        
        This method validates the command exists, checks argument count,
        and executes the command function with proper error handling.
        
        Args:
            cmd_name (str): The name of the command to execute
            args (list): List of arguments for the command
            
        Returns:
            Response: Response object containing the result or error message
        """
        if cmd_name not in CommandsHandler.commands:
            return CommandsHandler.Response("Unknown command", is_error=True)

        command = self.commands[cmd_name]
        if len(args) != command.arg_count:
            return CommandsHandler.Response(f"Arguments error: Expected {command.arg_count} arguments, got {len(args)}.", is_error=True)

        try:
            result = command.function(self, *args)
            return CommandsHandler.Response(result)
        except ValueError as ve:
            return CommandsHandler.Response(f"Value error: {ve}", is_error=True)
        except KeyError as ke:
            return CommandsHandler.Response(f"Key error: {ke}", is_error=True)
        except Exception as e:
            print(f"Error: {e}")

    def show_all_commands(self) -> str:
        """
        Generate a formatted help string showing all available commands.
        
        Returns:
            str: Multi-line string with command names, arguments, and descriptions
        """
        return "\n".join(f"{name} {', '.join(command.arguments)}: {command.description}" for name, command in self.commands.items())
