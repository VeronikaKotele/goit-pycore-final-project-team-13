def add_contact(args, contacts):
    pass

def change_phone(args, contacts):
    pass

def show_phone(args, contacts):
    pass

def add_birthday(args, contacts):
    pass

def show_birthday(args, contacts):
    name = args[0]
    record = contacts[name]
    return record.birthday

def upcoming_birthdays(args, contacts):
    pass

def show_all(args, contacts):
    pass

commands = {
    "add": { "command": add_contact, "arguments": 2 },
    "change": { "command": change_phone, "arguments": 3 },
    "phone": { "command": show_phone, "arguments": 1 },
    "all": { "command": show_all, "arguments": 0 },
    "add-birthday": { "command": add_birthday, "arguments": 2 },
    "show-birthday": { "command": show_birthday, "arguments": 1 },
    "birthdays": { "command": upcoming_birthdays, "arguments": 0 }
}