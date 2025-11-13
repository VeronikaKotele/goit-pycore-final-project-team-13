from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name: str):
        if name in self.data:
            return self.data[name]
        else: 
            return None
    
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, next_days = 7):
        """
        Returns a list of users who have birthdays within the next N days
        """
        upcoming_birthdays = []
        current_date = datetime.today().date()

        for user in self.data.values():
            if not user.birthday:
                continue
            birthday_datetime = datetime.strptime(user.birthday.value, "%d.%m.%Y").date()
            birthday_datetime = birthday_datetime.replace(year=current_date.year)

            if birthday_datetime.day < current_date.day:
                birthday_datetime = birthday_datetime.replace(year=current_date.year + 1)
        
            time_difference = birthday_datetime - current_date

            if 0 <= time_difference.days <= next_days:
                if birthday_datetime.weekday() == 5:
                    birthday_datetime += timedelta(days = 2)
                elif birthday_datetime.weekday() == 6:
                    birthday_datetime += timedelta(days = 1)

                upcoming_birthdays.append({
                    "name": user.name.value,
                    "congratulation_date": birthday_datetime.strftime("%d-%m-%Y")
                })

        return upcoming_birthdays        