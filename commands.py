from managers.address_book_manager import AddressBookManager
from managers.notes_manager import NotesManager
from models.contacts.address import HomeAddress
from models.contacts.phone import Phone
from models.contacts.birthday import Birthday

class CommandsHandler:
    def __init__(self):
        self.contacts_manager = AddressBookManager()
        self.notes_manager = NotesManager()

    def __add_phone(self, name, phone) -> str:
        self.contacts_manager.add_phone(name, Phone(phone))
        return f"Phone {phone} added for contact {name}."

    def __remove_phone(self, name, phone) -> str:
        self.contacts_manager.remove_phone(name, Phone(phone))
        return f"Phone {phone} removed from contact {name}."

    def __add_birthday(self, name, birthday) -> str:
        self.contacts_manager.add_birthday(name, Birthday(birthday))
        return f"Birthday {birthday} added for contact {name}."

    def __add_address(self, name, address) -> str:
        self.contacts_manager.add_address(name, HomeAddress(address))
        return f"Address {address} added for contact {name}."

    def __upcoming_birthdays(self, days) -> str:
        birthdays = self.contacts_manager.get_upcoming_birthdays(int(days))
        if not birthdays:
            return "No upcoming birthdays."
        return "Upcoming birthdays:\n" + "\n".join(birthdays)

    def __show_contact(self, name) -> str:
        contact = self.contacts_manager.find(name)
        if not contact:
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

    def __show_note(self, title) -> str:
        note = self.notes_manager.find(title)
        if not note:
            raise KeyError(f"Note with title '{title}' not found.")
        return f"Note '{title}': {note}"

    def __show_all(self):
        return f"Contacts:\n{self.contacts_manager}\n\nNotes:\n{self.notes_manager}"


    class Response:
        def __init__(self, message: str, is_error: bool = False):
            self.message = message
            self.is_error = is_error


    class Command:
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
        return "\n".join(f"{name} {', '.join(command.arguments)}: {command.description}" for name, command in self.commands.items())
