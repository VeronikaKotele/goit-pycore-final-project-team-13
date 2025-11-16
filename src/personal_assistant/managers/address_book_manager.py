from personal_assistant.models import AddressBook, AddressBookRecord, Phone, Birthday, HomeAddress
import re
from datetime import datetime


class AddressBookManager:
    def __init__(self):
        self.__address_book = AddressBook()
        self.__address_book.try_load_data_from_cache()

    def add_record(self, name: str) -> AddressBookRecord:
        record = AddressBookRecord(name)
        self.__address_book[name] = record
        return record

    def find(self, name: str) -> AddressBookRecord | None:
        return self.__address_book.get(name)

    def delete(self, name: str) -> AddressBookRecord:
        deleted = self.__address_book.pop(name, None)
        if not deleted:
            raise KeyError(f"No record found for {name}.")
        return deleted

    def add_phone(self, name: str, phone: Phone) -> AddressBookRecord:
        record = self.__address_book.get(name)
        if record:
            record.add_phone(phone)
            return record
        raise KeyError(f"No record found for {name}.")

    def remove_phone(self, name: str, phone: Phone) -> AddressBookRecord:
        record = self.__address_book.get(name)
        if record:
            record.remove_phone(phone)
            return record
        raise KeyError(f"No record found for {name}.")

    def add_birthday(self, name: str, birthday: Birthday) -> AddressBookRecord:
        record = self.__address_book.get(name)
        if record:
            record.add_birthday(birthday)
            return record
        raise KeyError(f"No record found for {name}.")

    def add_address(self, name: str, address: HomeAddress) -> AddressBookRecord:
        record = self.__address_book.get(name)
        if record:
            record.add_address(address)
            return record
        raise KeyError(f"No record found for {name}.")

    def get_all_records(self) -> list[AddressBookRecord]:
        return list(self.__address_book.values())

    def get_upcoming_birthdays(self, days = 7):
        today = datetime.now().date()
        upcoming = []
        for record in self.__address_book.values():
            next_date = record.get_next_birthday()
            if not next_date:
                continue

            delta = (next_date - today).days
            if 0 <= delta <= days:
                years_reached = next_date.year - record.birthday.value.year
                upcoming.append({
                    "name": record.name,
                    "next_date": next_date,
                    "years_reached": years_reached
                })
        return upcoming
    
    def save_data(self):
        self.__address_book.save_data_to_cache()
