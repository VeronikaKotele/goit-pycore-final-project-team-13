from commands import CommandsHandler

def parse_input(user_input):
    """
    Parses the user's input string into a command and a list of arguments.
    """

    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args

def main():
    """
    Main interactive part of the Assistant bot.
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
        if (response.is_error):
            print(f"Error: {response.message}")
        else:
            print(response.message)


if __name__ == "__main__":
    main()