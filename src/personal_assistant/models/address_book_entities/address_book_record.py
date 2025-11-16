from .phone import Phone
from .birthday import Birthday
from .address import HomeAddress
from .email import Email
from datetime import datetime, date

class AddressBookRecord:
    def __init__(self, name: str):
        self.name = name
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    def add_phone(self, phone: Phone):
        if phone in self.phones:
            raise ValueError(f"Phone number {phone} already exists for contact {self.name}.")
        self.phones.append(phone)

    def add_birthday(self, date: Birthday):
        self.birthday = date

    def add_address(self, address: HomeAddress):
        self.address = address

    def remove_phone(self, old_phone: Phone):
        try:
            self.phones.remove(old_phone)
        except ValueError:
            raise KeyError(f"Phone number {old_phone} does not exist for contact {self.name}.")

    def add_email(self, email: Email):
        self.email = email

    def get_next_birthday(self) -> date | None:
        if not self.birthday:
            return None
        today = datetime.now().date()
        current_year_birthday = self.birthday.value.replace(year=today.year).date()
        if current_year_birthday < today:
            next_birthday = current_year_birthday.replace(year=today.year + 1)
        else:
            next_birthday = current_year_birthday
        return next_birthday

    def __str__(self):
        phones_str = ", Phones: [" + ", ".join(str(phone) for phone in self.phones) + "]" if self.phones else ""
        birthday_str = ", Birthday: " + str(self.birthday) if self.birthday else ""
        address_str = ", Address: " + str(self.address) if self.address else ""
        email_str = ", Email: " + str(self.email) if self.email else ""
        return f"Name: {self.name}{phones_str}{birthday_str}{address_str}{email_str}"