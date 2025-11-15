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
        "desc": "Add a phone number to a contact.",
        "args": ["name", "phone"],
        "example": "add-phone John 1234567890"
    },
    "add-birthday": {
        "desc": "Add a birthday to a contact.",
        "args": ["name", "birthday"],
        "example": "add-birthday John 01.01.1990"
    },
    "add-address": {
        "desc": "Add an address to a contact.",
        "args": ["name", "address"],
        "example": "add-address John '123 Main St'"
    },
    "remove-phone": {
        "desc": "Remove a phone number from a contact.",
        "args": ["name", "phone"],
        "example": "remove-phone John 1234567890"
    },
    "upcoming-birthday": {
        "desc": "Show contacts with birthdays in the next N days.",
        "args": ["days(optional, default=7)"],
        "example": "upcoming-birthday 7"
    },
    "search": {
        "desc": "Search for a contact by name.",
        "args": ["name"],
        "example": "search John"
    },
    "delete": {
        "desc": "Delete a contact.",
        "args": ["name"],
        "example": "delete John"
    },
    "all": {
        "desc": "Show all contacts.",
    },
    "add-note": {
        "desc": "Add a new note.",
        "args": ["title", "content"],
        "example": "add-note 'shopping_list': 'Buy milk'"
    },
    "search-note": {
        "desc": "Search notes by title.",
        "args": ["title"],
        "example": "search-note 'shopping_list'"
    },
    "update-note": {
        "desc": "Edit an existing note - override by title.",
        "args": ["title", "content"],
        "example": "update-note 'shopping_list': 'Buy bread instead'"
    },
    "delete-note": {
        "desc": "Delete a note.",
        "args": ["title"],
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
        if command_name and cmd != command_name:
            continue

        message += (
            f"{Fore.BLUE}{cmd:<15} - "
            f"{Fore.WHITE}{info['desc']:<60}"
        )
        if 'args' in info:
            args_str = ", ".join(info['args'])
            message += f"{Fore.BLUE} Args: ({args_str})."
        if 'example' in info:
            message += (
            f"{Fore.LIGHTBLACK_EX} Example: {info['example']}\n"
        )
    return message