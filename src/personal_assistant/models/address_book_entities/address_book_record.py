from .phone import Phone
from .birthday import Birthday
from .address import HomeAddress
from .email import Email

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

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        try:
            phone_index = self.phones.index(old_phone)
            self.phones[phone_index] = new_phone
        except ValueError:
            raise ValueError(f"Phone number {old_phone} does not exist for contact {self.name}.")

    def add_email(self, email: Email):
        self.email = email

    def __str__(self):
        phones_str = ", Phones: [" + ", ".join(str(phone) for phone in self.phones) + "]" if self.phones else ""
        birthday_str = ", Birthday: " + str(self.birthday) if self.birthday else ""
        address_str = ", Address: " + str(self.address) if self.address else ""
        email_str = ", Email: " + str(self.email) if self.email else ""
        return f"Name: {self.name}{phones_str}{birthday_str}{address_str}{email_str}"