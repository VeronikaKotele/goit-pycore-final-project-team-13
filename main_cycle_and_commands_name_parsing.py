from collections import UserDict
import datetime
import pickle


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
    except Exception as e:
        print(f"Помилка при завантаженні даних: {e}. Створюється нова адресна книга.")
        return AddressBook()
     

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

    book = load_data()
    print("Вітаю! Я персональний помічник.")

    if book.data:
        print("Адресна книга успішно завантажена.")
    else:
        print("Створено нову адресну книгу.")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            save_data(book)
            print("Дані збережено. До побачення!")
            break

        
        elif command == "hello":
            print("Чим можу допомогти?")

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
            print(add_note(args, book))

# 7. Проводити пошук за нотатками;
        elif command == "search-note":
            print(search_note(args, book))

# 8. Редагувати та видаляти нотатки;
        elif command == "edit-note":
            print(edit_note(args, book))

        elif command == "delete-note":
            print(delete_note(args, book))

# Not sure that we need this command, added just because it was in the hw
        elif command == "all":
            print(all_contacts(args, book))

        elif command == "save":
            save_data(book)
            print("Дані збережено.")

        else:
            print("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()