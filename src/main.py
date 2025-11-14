from personal_assistant.commands import commands

def parse_input(user_input):
    """
    Parses the user's input string into a command and a list of arguments.
    """
    
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args   

def load_data(filename):
    return object()  # placeholder for loading logic

def save_data(filename, data):
    return object()  # placeholder for saving logic

def main():
    """
    Main interactive part of the Assistant bot.
    """

    book = load_data("addressbook.pkl")
    notes = load_data("notes.pkl")

    print("Welcome! I am your assistant bot.")

    if book:
        print("Address book successfully loaded.")
    else:
        print("A new address book has been created.")

    if notes:
        print("Notes loaded.")
    else:
        print("A new notebook created.")
        
    while True:
        user_input = input("Enter a command: ").lower().strip()
        cmd_name, args = parse_input(user_input)
 
        if cmd_name in ["exit", "close"]:
            save_data("addressbook.pkl", book)
            save_data("notes.pkl", notes)
            print("Goodbye!")
            break
        
        elif cmd_name == "hello":
            print("How can I help you?")

        elif cmd_name not in commands.keys():
            print("Unknown command. Please try again.")
            continue

        # execute command
        command = commands[cmd_name]
        try:
            expected_args = command.get("arguments", 0)
            if len(args) != expected_args:
                print(f"Expected {expected_args} arguments, got {len(args)}.")
                continue

            command.get("command")(args, book)

        except ValueError as ve:
            print(f"Value error: {ve}")
        except KeyError:
            print("Contact not found.")
        except IndexError:
            print(f"Not enough arguments. Format: <command> [arguments].")
        except Exception as e:
            print(f"Error executing command '{cmd_name}': {e}")

    # todo: cleanup resources


if __name__ == "__main__":
    main()