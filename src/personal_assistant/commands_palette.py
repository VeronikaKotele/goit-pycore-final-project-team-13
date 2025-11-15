from colorama import Fore, Style, init

init(autoreset=True)

COMMANDS = {
    "hello": {
        "desc": "Greets the user.",
    },
    "help": {
        "desc": "Show this command palette.",
    },
    "add-phone": {
        "desc": "Add a phone number to a contact).",
        "example": "add-phone John 1234567890"
    },
    "add-birthday": {
        "desc": "Add a birthday to a contact.",
        "example": "add-birthday John 01.01.1990"
    },
    "add-address": {
        "desc": "Add an address to a contact.",
        "example": "add-address John 123 Main St"
    },
    "remove-phone": {
        "desc": "Remove a phone number from a contact.",
        "example": "remove-phone John 1234567890"
    },
    "upcoming-birthday": {
        "desc": "Show contacts with birthdays in the next N days.",
        "example": "upcoming-birthday 7"
    },
    "search": {
        "desc": "Search for a contact by name.",
        "example": "search John"
    },
    "delete": {
        "desc": "Delete a contact.",
        "example": "delete John"
    },
    "all": {
        "desc": "Show all contacts.",
    },
    "add-note": {
        "desc": "Add a new note.",
        "example": "add-note 'shopping_list': 'Buy milk'"
    },
    "search-note": {
        "desc": "Search notes by title.",
        "example": "search-note 'shopping_list'"
    },
    "update-note": {
        "desc": "Edit an existing note - override by title.",
        "example": "update-note 'shopping_list': 'Buy bread instead'"
    },
    "delete-note": {
        "desc": "Delete a note.",
        "example": "delete-note 'shopping_list'"
    },
    "all-notes": {
        "desc": "Show all notes.",
    },
    "exit": {
        "desc": "Exit the assistant and save data.",
    },
    "close": {
        "desc": "Exit the assistant and save data.",
    }
}


def get_help_message(command_name:str=None):
    """
    Prints the command palette with colors:
    - Command name in green
    - Description in orange
    - Example usage in yellow
    """
    message = "\n📖 Command Palette:"
    for cmd, info in COMMANDS.items():
        if (command_name and cmd != command_name):
            continue
        message += (
            f"{Fore.GREEN}{cmd:<15}{Style.RESET_ALL} - "
            f"{Fore.LIGHTRED_EX}{info['desc']:<60}{Style.RESET_ALL} "
            f"{Fore.YELLOW}Example: {info['example']}{Style.RESET_ALL}\n"
        )
    return message