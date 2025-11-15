from .managers import AddressBookManager, NotesManager
from .models import HomeAddress, Phone, Birthday
from .commands_palette import COMMANDS, get_help_message

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

        # Map command names to their handler methods
        self.commands = COMMANDS.copy()
        self.commands["help"].function = self.get_help
        self.commands["add-phone"].function = self.__add_phone
        self.commands["remove-phone"].function = self.__remove_phone
        self.commands["add-birthday"].function = self.__add_birthday
        self.commands["add-address"].function = self.__add_address
        self.commands["upcoming-birthdays"].function = self.__upcoming_birthdays
        self.commands["search"].function = self.__show_contact
        self.commands["delete"].function = self.__delete_contact
        self.commands["all"].function = self.__show_all_contacts
        self.commands["add-note"].function = self.__add_note
        self.commands["search-note"].function = self.__show_note
        self.commands["update-note"].function = self.__update_note
        self.commands["delete-note"].function = self.__delete_note
        self.commands["all-notes"].function = self.__show_all_notes

    def __add_phone(self, name, phone) -> str:
        self.address_book_manager.add_phone(name, Phone(phone))
        return f"Phone {phone} added for contact {name}."

    def __remove_phone(self, name, phone) -> str:
        self.address_book_manager.remove_phone(name, Phone(phone))
        return f"Phone {phone} removed from contact {name}."

    def __add_birthday(self, name, birthday) -> str:
        self.address_book_manager.add_birthday(name, Birthday(birthday))
        return f"Birthday {birthday} added for contact {name}."

    def __add_address(self, name, *args) -> str:
        self.address_book_manager.add_address(name, HomeAddress(*args))
        return f"Address {args} added for contact {name}."

    def __upcoming_birthdays(self, days) -> str:
        birthdays = self.address_book_manager.get_upcoming_birthdays(int(days))
        if not birthdays:
            return f"No upcoming birthdays in {days} days."
        return "Upcoming birthdays:\n" + "\n".join(
            f"\t{b['name']} - {b['next_date']} (turning {b['years_reached']})" for b in birthdays
        )

    def __show_contact(self, name) -> str:
        contact = self.address_book_manager.find(name)
        if contact is None:
            raise KeyError(f"Contact with name '{name}' not found.")
        return str(contact)
    
    def __delete_contact(self, name) -> str:
        self.address_book_manager.delete(name)
        return f"Contact '{name}' deleted."

    def __add_note(self, *args) -> str:
        self.notes_manager.add_note(*args)
        return "Note is added."

    def __update_note(self, title, content) -> str:
        self.notes_manager.update(title, content)
        return f"Note '{title}' updated. New content: {self.notes_manager.find(title)}"

    def __delete_note(self, title):
        self.notes_manager.delete(title)
        return f"Note '{title}' deleted."

    def __show_note(self, title) -> str:
        note = self.notes_manager.find(title)
        if not note:
            raise KeyError(f"Note with title '{title}' not found.")
        return f"Note '{title}': {note}"

    def __show_all_contacts(self):
        return str(self.address_book_manager)

    def __show_all_notes(self):
        return str(self.notes_manager)
    
    def get_help(self) -> str:
        return get_help_message()

    class Response:
        def __init__(self, message, is_error=False, should_exit=False):
            self.message = message
            self.is_error = is_error
            self.should_exit = should_exit

    def execute_command(self, cmd_name: str, args: list[str]) -> Response:
        """
        Execute a command with the given arguments.
        
        This method validates the command exists, checks argument count,
        and executes the command function with proper error handling.
        
        Args:
            cmd_name (str): The name of the command to execute
            rest_of_input (str): The remaining input string after the command name
            
        Returns:
            Response: Response object containing the result or error message
        """
        if cmd_name not in self.commands:
            return CommandsHandler.Response("Unknown command", is_error=True)
        elif cmd_name in ["hi", "hello"]:
            return CommandsHandler.Response("How can I help you?")
        elif cmd_name in ["exit", "close"]:
            return CommandsHandler.Response("Goodbye!", should_exit=True)

        command = self.commands[cmd_name]
        expected_args_count = command.function.__code__.co_argcount - 1  # exclude 'self'
        if len(args) != expected_args_count:
            return CommandsHandler.Response("Arguments error: " +
                                            f"Expected {expected_args_count} arguments, got {len(args)}.\n" +
                                            get_help_message(cmd_name)
                                            , is_error=True)

        try:
            result = command.function(self, *args)
            return CommandsHandler.Response(result)
        except ValueError as ve:
            return CommandsHandler.Response(f"Value error: {ve}", is_error=True)
        except KeyError as ke:
            return CommandsHandler.Response(f"Key error: {ke}", is_error=True)
        except Exception as e:
            return CommandsHandler.Response(f"Error: {e}", is_error=True)
