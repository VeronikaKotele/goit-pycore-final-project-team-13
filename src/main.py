"""
Personal Assistant Bot - Main Module

This module provides the main entry point for a personal assistant bot that manages
contacts and notes. The bot provides an interactive command-line interface for users
to perform various operations on their contacts and notes.

The bot supports commands for:
- Managing contacts (adding phones, birthdays, addresses)
- Managing notes (creating, updating, deleting notes)
- Viewing contact and note information
"""

from personal_assistant import CommandsHandler

def parse_input(user_input):
    """
    Parse user input into command and arguments.
    
    Takes a user input string and separates it into a command and its arguments.
    The command is converted to lowercase for case-insensitive matching.
    """
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args

def main():
    """
    Main interactive loop of the Personal Assistant bot.
    The loop continues until the user enters an exit command, processing each
    command through the CommandsHandler and displaying appropriate responses.
    """

    commands_handler = CommandsHandler()
    print("Welcome! I am your assistant bot. You can manage your contacts and notes here.")
    print(commands_handler.show_all_commands())

    while True:
        user_input = input("Enter a command: ").lower().strip()
        cmd_name, args = parse_input(user_input)

        if cmd_name in ["hi", "hello"]:
            print("How can I help you?")
            continue
        elif cmd_name in ["exit", "close"]:
            print("Goodbye!")
            break

        response = commands_handler.execute_command(cmd_name, args)
        if response.is_error:
            print(f"Error: {response.message}")
        else:
            print(response.message)


if __name__ == "__main__":
    main()
