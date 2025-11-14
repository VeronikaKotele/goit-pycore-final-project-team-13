from datetime import datetime

class Birthday:
    def __init__(self, value: str):
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
            if date <= datetime.now():
                self.value = date
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
