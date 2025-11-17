# Personal Assistant

A command-line personal assistant application for managing contacts and notes efficiently. Store, search, and organize your contacts with detailed information and keep track of important notes with tagging capabilities.

## Features

### Contact Management
- **Store Contacts**: Save contacts with names, addresses, phone numbers, emails, and birthdays
- **Birthday Reminders**: Display contacts with upcoming birthdays within a specified number of days
- **Input Validation**: Automatic validation of phone numbers and emails with user notifications
- **Search Functionality**: Quickly find contacts in your address book
- **Full CRUD Operations**: Create, read, update, and delete contact entries

### Notes Management
- **Create Notes**: Store text-based notes with rich information
- **Tag System**: Add keywords/tags to categorize and organize notes
- **Advanced Search**: Search and sort notes by content or tags
- **Note Organization**: Edit and delete notes as needed

### Additional Features
- **Smart Command Suggestions**: The bot analyzes input and suggests the closest matching command
- **Interactive CLI**: User-friendly command-line interface for all operations

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup
1. Clone the repository:
```bash
git clone https://github.com/VeronikaKotele/goit-pycore-final-project-team-13.git
cd goit-pycore-final-project-team-13
```

2. Install the package:
```bash
pip install -e .
```

For development installation with testing dependencies:
```bash
pip install -e ".[dev]"
```

## Usage

Run the personal assistant:
```bash
python src/main.py
```

The bot will start an interactive session where you can enter commands to manage your contacts and notes.

### Example Commands
- Add a contact with phone number
- Store birthday information
- Search for contacts
- Create and tag notes
- View upcoming birthdays

(Type `help` in the application for a full list of available commands)

## Running Tests

Run the test suite using pytest:
```bash
pytest
```

For coverage report:
```bash
pytest --cov=src
```

See `TESTING_GUIDE.md` for more detailed testing information.

## Project Structure

```
src/
├── main.py                          # Application entry point
└── personal_assistant/
    ├── commands_handler.py          # Command processing logic
    ├── commands_palette.py          # Available commands
    ├── managers/                    # Business logic managers
    │   ├── address_book_manager.py
    │   └── notes_manager.py
    └── models/                      # Data models
        ├── address_book.py
        ├── notebook.py
        └── address_book_entities/
```

## Development

### Team
- Team 13

### Contributing
This project was developed as part of the GoIT Python Core course.

## License

This project is created for educational purposes.
