from field import Field

class Email(Field):
    def __init__(self, value):
        # todo validate, raise exeption
        super().__init__(value)