class Phone:
    def __init__(self, value):
        # todo validate, raise exсeption
        self.value = value

    def __str__(self):
        return str(self.value)
