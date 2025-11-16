import re

class Phone:
    def __init__(self, value):
        input_phone_pattern = re.compile(r'^\+?\d{7,15}$') # optionally starts with + and has 7 to 15 digits
        if not input_phone_pattern.match(value):
            raise ValueError(f"Invalid phone number format: {value}")

        if not value.startswith("+"):
            if len(value) == 10 and value.startswith("0"):
                value = "+38" + value
            elif len(value) == 9 and not value.startswith("0"):
                value = "+380" + value

        self.value = value

    def __str__(self):
        return str(self.value)
