from colorama import Fore, Style, init

init(autoreset=True)

COMMANDS = {
    "hello": {
        "desc": "Greets the user.",
        "example": "hello"
    },
    "add": {
        "desc": "Add a new contact (name, phone, email, birthday, address).",
        "example": "add John 1234567890 john@email.com 01.01.1990 SomeStreet"
    },
    "upcoming-birthday": {
        "desc": "Show contacts with birthdays in the next N days.",
        "example": "upcoming-birthday 7"
    },
    "search": {
        "desc": "Search for a contact by name.",
        "example": "search John"
    },
    "edit": {
        "desc": "Edit a contact's phone/email/address.",
        "example": "edit John 1234567890 0987654321"
    },
    "delete": {
        "desc": "Delete a contact.",
        "example": "delete John"
    },
    "all": {
        "desc": "Show all contacts.",
        "example": "all"
    },
    "add-note": {
        "desc": "Add a new note.",
        "example": "add-note Buy milk"
    },
    "search-note": {
        "desc": "Search notes by keyword.",
        "example": "search-note milk"
    },
    "edit-note": {
        "desc": "Edit an existing note.",
        "example": "edit-note 1 Buy bread instead"
    },
    "delete-note": {
        "desc": "Delete a note.",
        "example": "delete-note 1"
    },
    "save": {
        "desc": "Save all data to disk.",
        "example": "save"
    },
    "exit / close": {
        "desc": "Exit the assistant and save data.",
        "example": "exit"
    }
}


def show_help():
    """
    Prints the command palette with colors:
    - Command name in green
    - Description in orange
    - Example usage in yellow
    """
    print("\n📖 Command Palette:")
    for cmd, info in COMMANDS.items():
        print(
            f"{Fore.GREEN}{cmd:<15}{Style.RESET_ALL} - "
            f"{Fore.LIGHTRED_EX}{info['desc']:<60}{Style.RESET_ALL} "
            f"{Fore.YELLOW}Example: {info['example']}{Style.RESET_ALL}"
        )
    print()


show_help()