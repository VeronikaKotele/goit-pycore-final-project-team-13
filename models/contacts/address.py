class HomeAddress:
    def __init__(self, value: str):
        try:
            # todo: validate address format
            self.value = value
        except ValueError:
            raise ValueError("Invalid format for address.")

    def __str__(self):
        return self.value