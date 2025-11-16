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
import shlex
from colorama import Fore, init

from personal_assistant import CommandsHandler

init(autoreset=True)
def parse_input(user_input):
    """
    Parse the user input into a command and its arguments.
    Splits the input string by spaces while respecting quoted substrings,
    allowing for multi-word arguments enclosed in quotes.
    Args:
        user_input (str): The raw input string from the user.
    Returns:
        tuple: A tuple containing the command name and arguments.
    """
    parts = shlex.split(user_input)
    cmd = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []

    return cmd, args

def main():
    """
    Main interactive loop of the Personal Assistant bot.
    The loop continues until the user enters an exit command, processing each
    command through the CommandsHandler and displaying appropriate responses.
    """

    commands_handler = CommandsHandler()
    print(f"{Fore.YELLOW}Welcome! I am your assistant bot. You can manage your contacts and notes here.")
    print(commands_handler.get_help())

    while True:
        user_input = input(f"{Fore.LIGHTBLACK_EX}Enter a command: {Fore.WHITE}")
        cmd, args = parse_input(user_input)
        if not cmd:
            print(f"{Fore.LIGHTBLACK_EX}Please enter a command or 'close' for exit.")
            continue

        response = commands_handler.execute_command(cmd, args)
        if response.is_error:
            print(f"{Fore.RED}Error: {response.message}")
        else:
            print(f"{Fore.GREEN}{response.message}")

        if response.should_exit:
            commands_handler.save_data()
            break

if __name__ == "__main__":
    main()
