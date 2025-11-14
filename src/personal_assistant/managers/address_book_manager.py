from personal_assistant.models import AddressBook, AddressBookRecord, Phone, Birthday, HomeAddress
from personal_assistant.cacheable_dict import CacheableDict
import re
from datetime import datetime


class AddressBookManager:
    def __init__(self):
        self.__address_book = CacheableDict("address_book_cache.pkl")

    def validate_phone(self, phone: str) -> bool:
        pattern = r'^\+?\d[\d\-\s\(\)]{7,20}$'
        return re.fullmatch(pattern, phone) is not None

    def validate_email(self, email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.fullmatch(pattern, email) is not None
    
    def add_record(self, record: AddressBookRecord) -> str:
        # Validate phone(s) if present
        for phone in record.phones:
            if not self.validate_phone(phone.value):
                return f"Invalid phone number: {phone.value}"

        # Validate email if present
        if record.email and not self.validate_email(record.email.value):
            return f"Invalid email: {record.email.value}"

        self.__address_book.add_record(record)
        self.__storage.save_state(self.__address_book)
        return f"Record for {record.name.value} added successfully."
    
    def find(self, name: str):
        record = self.__address_book.find(name)
        return record if record else f"No record found for {name}."

    def delete(self, name: str):
        deleted = self.__address_book.delete(name)
        if deleted:
            self.__storage.save_state(self.__address_book)
            return f"Record for {name} deleted."
        return f"No record found for {name}."

    def add_phone(self, name: str, phone: Phone):
        if not self.validate_phone(phone.value):
            return f"Invalid phone number: {phone.value}"

        record = self.__address_book.find(name)
        if record:
            record.add_phone(phone)
            self.__storage.save_state(self.__address_book)
            return f"Phone {phone.value} added to {name}."
        return f"No record found for {name}."

    def remove_phone(self, name: str, phone: Phone):
        record = self.__address_book.find(name)
        if record:
            record.remove_phone(phone)
            self.__storage.save_state(self.__address_book)
            return f"Phone {phone.value} removed from {name}."
        return f"No record found for {name}."

    def add_birthday(self, name: str, birthday: Birthday):
        record = self.__address_book.find(name)
        if record:
            record.add_birthday(birthday)
            self.__storage.save_state(self.__address_book)
            return f"Birthday {birthday.value} added to {name}."
        return f"No record found for {name}."

    def add_address(self, name: str, address: HomeAddress):
        record = self.__address_book.find(name)
        if record:
            record.add_address(address)
            self.__storage.save_state(self.__address_book)
            return f"Address added to {name}."
        return f"No record found for {name}."

    def get_upcoming_birthdays(self, next_days = 7):
        today = datetime.today().date()
        upcoming = []

        for record in self.__address_book.all_records():
            if record.birthday:
                bday_this_year = record.birthday.value.replace(year=today.year)
                delta = (bday_this_year - today).days
                if 0 <= delta <= next_days:
                    upcoming.append(record)

        return upcoming if upcoming else f"No birthdays in the next {next_days} days."