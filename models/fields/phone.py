from field import Field

class Phone(Field):
    def __init__(self, value):
        # todo validate, raise exeption
        super().__init__(value)
        