from pathlib import Path
import pickle



def get_storage_path(filename):
    home = Path.home()
    storage_dir = home / "AssistantBot"
    storage_dir.mkdir(exist_ok=True)
    return storage_dir / filename

def save_data(book, filename="addressbook.pkl"):
    path = get_storage_path(filename)
    try:
        with open(path, "wb") as f:
            pickle.dump(book, f)
    except Exception as e:
        print(f"Error: Can not save {filename}: {e}")


def load_data(filename="addressbook.pkl"):
    path = get_storage_path(filename)
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
    except Exception as e:
        print(f"Error occured when loading data: {e}. Creating a new book")
        return AddressBook()
    

def save_notes(notes, filename="notes.pkl"):
    path = get_storage_path(filename)
    with open(path, "wb") as f:
        pickle.dump(notes, f)

def load_notes(filename="notes.pkl"):
    path = get_storage_path(filename)
    try:
        with open(path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NoteBook()
    except Exception as e:
        print(f"Error occured when loading notes: {e}. Creating a new notebook.")
        return NoteBook()
     

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

    book = load_data("addressbook.pkl")
    notes = load_data("notes.pkl")

    print("Welcome! I am your assistant bot.")

    if book.data:
        print("Address book successfully loaded.")
    else:
        print("A new address book has been created.")

    if notes.data:
        print("Notes loaded.")
    else:
        print("A new notebook created.")
        
    while True:
        user_input = input("Enter a command: ").lower().strip()
        command, args = parse_input(user_input)
 
        try:
            if command in ["exit", "close"]:
                save_data(book)
                save_notes(notes)
                print("Data saved. Goodbye!")
                break

            
            elif command == "hello":
                print("How can I help you?")

    # 1. Зберігати контакти з іменами, адресами, номерами телефонів, email та днями народження до книги контактів;
            elif command == "add":
                print(add_contact(args, book))

    # 2. Виводити список контактів, у яких день народження через задану кількість днів від поточної дати;
            elif command == "upcoming-birthday":
                print(upcoming_birthdays(args, book))

    # 4. Здійснювати пошук контактів серед контактів книги;
            elif command =="search":
                print(search_contact(args, book))

    # 5. Редагувати та видаляти записи з книги контактів;
            elif command == "edit":
                print(change_phone_number(args, book))

            elif command == "delete":
                print(delete_contact(args, book))

    # 6. Зберігати нотатки з текстовою інформацією;            
            elif command == "add-note":
                print(add_note(args, notes))

    # 7. Проводити пошук за нотатками;
            elif command == "search-note":
                print(search_note(args, notes))

    # 8. Редагувати та видаляти нотатки;
            elif command == "edit-note":
                print(edit_note(args, notes))

            elif command == "delete-note":
                print(delete_note(args, notes))

    # Not sure that we need this command, added just because it was in the hw
            elif command == "all":
                print(all_contacts(args, book))

            elif command == "save":
                save_data(book)
                print("Data saved.")

            else:
                print("Unknown command. Please try again.")
        
        except ValueError as ve:
            print(f"Value error: {ve}")
        except KeyError:
            print("Contact not found.")
        except IndexError:
            print("Not enough arguments. Format: <command> [arguments].")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()