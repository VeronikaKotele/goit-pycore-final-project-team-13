from fields.name import Name


class Note:
    def __init__(self, name: str, text: str):
        self.name = Name(name)
        self.text = text