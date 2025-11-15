from datetime import datetime

class Birthday:
    def __init__(self, value: str):
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        if date > datetime.now():
            raise ValueError("Birthday cannot be in the future")

        self.value = date

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
