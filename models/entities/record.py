from fields.phone import Phone
from fields.name import Name
from fields.birthday import Birthday
from fields.address import Address
from models.managers.notes_manager import Notes

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None


    def add_phone(self, phone):
        phone = Phone(phone)
        if phone:
            self.phones.append(phone)

    def add_birthday(self, date):
        self.birthday = Birthday(date)  

    def add_address(self, address):
        self.address = Address(address)
    
    def edit_phone(self, old_phone, new_phone):
        if not Phone.validate(new_phone):
             raise ValueError("Incorrect number, must be 10 digits")

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone.value
              
        return None

    def __str__(self):
        birthday_str = f", birthday: {self.birthday.value}" if self.birthday and self.birthday.value else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}"
    



