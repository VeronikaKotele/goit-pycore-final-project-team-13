from colorama import Fore, init

init(autoreset=True)

class CommandsInfo:
    def __init__(self, name: str, desc: str, args: list[str]=None, example: str=None):
        self.name = name
        self.desc = desc
        self.args = args or []
        self.example = example
        self.function = None

COMMANDS = {
    "hello": CommandsInfo(
        name="hello", desc="Greets the user."
    ),
    "help": CommandsInfo(
        name="help", desc="Show this command palette."
    ),
    "add-contact": CommandsInfo(
        name="add-contact", desc="Add a new contact.",
        args=["name"],
        example="add-contact John"
    ),
    "add-phone": CommandsInfo(
        name="add-phone", desc="Add a phone number to a contact.",
        args=["name", "phone"],
        example="add-phone John 1234567890"
    ),
    "add-birthday": CommandsInfo(
        name="add-birthday", desc="Add a birthday to a contact.",
        args=["name", "birthday"],
        example="add-birthday John 01.01.1990"
    ),
    "add-address": CommandsInfo(
        name="add-address", desc="Add an address to a contact.",
        args=["name", "address"],
        example="add-address John '123 Main St'"
    ),
    "remove-phone": CommandsInfo(
        name="remove-phone", desc="Remove a phone number from a contact.",
        args=["name", "phone"],
        example="remove-phone John 1234567890"
    ),
    "birthdays": CommandsInfo(
        name="birthdays", desc="Show contacts with birthdays in the next N days.",
        args=["days(optional, default=7)"],
        example="birthdays 7"
    ),
    "search": CommandsInfo(
        name="search", desc="Search for a contact by name.",
        args=["name"],
        example="search John"
    ),
    "delete": CommandsInfo(
        name="delete", desc="Delete a contact.",
        args=["name"],
        example="delete John"
    ),
    "all": CommandsInfo(
        name="all", desc="Show all contacts.",
    ),
    "add-note": CommandsInfo(
        name="add-note", desc="Add a new note.",
        args=["title", "content"],
        example="add-note 'shopping_list': 'Buy milk'"
    ),
    "search-note": CommandsInfo(
        name="search-note", desc="Search notes by title.",
        args=["title"],
        example="search-note 'shopping_list'"
    ),
    "update-note": CommandsInfo(
        name="update-note", desc="Edit an existing note - override by title.",
        args=["title", "content"],
        example="update-note 'shopping_list': 'Buy bread instead'"
    ),
    "delete-note": CommandsInfo(
        name="delete-note", desc="Delete a note.",
        args=["title"],
        example="delete-note 'shopping_list'"
    ),
    "all-notes": CommandsInfo(
        name="all-notes", desc="Show all notes.",
    ),
    "exit": CommandsInfo(
        name="exit", desc="Exit the assistant and save data.",
    ),
    "close": CommandsInfo(
        name="close", desc="Exit the assistant and save data.",
    )
}


def get_help_message(command_name:str=None):
    """
    Prints the command palette with colors:
    - Command name in green
    - Description in orange
    - Example usage in yellow
    """
    message = "\n📖 Command Palette:\n"
    for cmd, info in COMMANDS.items():
        if command_name and cmd != command_name:
            continue

        message += f"{Fore.BLUE}{cmd}"

        if info.args:
            message += f"{Fore.BLUE} <{('> <'.join(info.args))}>"

        message += f" - {Fore.WHITE}{info.desc}"

        if info.example:
            message += f"{Fore.LIGHTBLACK_EX} Example: {info.example}"
        message += "\n"
    return message