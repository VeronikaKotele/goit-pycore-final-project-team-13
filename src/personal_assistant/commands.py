from .managers import AddressBookManager, NotesManager
from .models import HomeAddress, Phone, Birthday

class CommandsHandler:
    """
    Main command handler for the Personal Assistant Bot.
    
    This class manages all user commands by coordinating between contacts and notes
    managers. It provides a unified interface for command execution with built-in
    error handling and argument validation.
    
    The handler maintains a registry of available commands and their metadata,
    including argument requirements and descriptions for help functionality.
    
    Attributes:
        address_book_manager (AddressBookManager): Handles contact-related operations
        notes_manager (NotesManager): Handles note-related operations
        commands (dict): Registry of available commands with their metadata
    """

    def __init__(self):
        self.address_book_manager = AddressBookManager()
        self.notes_manager = NotesManager()

    def __add_phone(self, name, phone) -> str:
        self.address_book_manager.add_phone(name, Phone(phone))
        return f"Phone {phone} added for contact {name}."

    def __remove_phone(self, name, phone) -> str:
        self.address_book_manager.remove_phone(name, Phone(phone))
        return f"Phone {phone} removed from contact {name}."

    def __add_birthday(self, name, birthday) -> str:
        self.address_book_manager.add_birthday(name, Birthday(birthday))
        return f"Birthday {birthday} added for contact {name}."

    def __add_address(self, name, address) -> str:
        self.address_book_manager.add_address(name, HomeAddress(address))
        return f"Address {address} added for contact {name}."

    def __upcoming_birthdays(self, days) -> str:
        birthdays = self.address_book_manager.get_upcoming_birthdays(int(days))
        if not birthdays:
            return "No upcoming birthdays."
        return "Upcoming birthdays:\n" + "\n".join(birthdays)

    def __show_contact(self, name) -> str:
        contact = self.address_book_manager.find(name)
        if contact is None:
            raise KeyError(f"Contact with name '{name}' not found.")
        return str(contact)

    def __add_note(self, title, content) -> str:
        self.notes_manager.add_note(title, content)
        return f"Note '{title}' added."

    def __update_note(self, title, content) -> str:
        note = self.notes_manager.find(title)
        if not note:
            raise KeyError(f"Note with title '{title}' not found.")
        note = content
        return f"Note '{title}' updated. New content: {self.notes_manager.find(title)}"

    def __delete_note(self, title):
        self.notes_manager.delete(title)
        return f"Note '{title}' deleted."

    def __show_note(self, title) -> str:
        note = self.notes_manager.find(title)
        if not note:
            raise KeyError(f"Note with title '{title}' not found.")
        return f"Note '{title}': {note}"

    def __show_all(self):
        return f"Contacts:\n{self.address_book_manager}\n\nNotes:\n{self.notes_manager}"


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
            return CommandsHandler.Response(f"Error: {e}", is_error=True)

    def show_all_commands(self) -> str:
        return "Available commands:\n" + \
            "| command name         | arguments               | description                              |\n" + \
            "|----------------------|-------------------------|------------------------------------------|\n" + \
            "\n".join(f"| {name:<20} | {(', '.join(command.arguments)):<23} | {command.description:40} |" for name, command in self.commands.items())
