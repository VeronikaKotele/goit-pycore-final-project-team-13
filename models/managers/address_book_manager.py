from collections import UserDict
from datetime import datetime, timedelta

class AddressBookManager(UserDict):
    def add_record(self, record):
        pass

    def find(self, name: str):
        pass
    
    def delete(self, name: str):
        pass

    def get_upcoming_birthdays(self, next_days = 7):
        pass