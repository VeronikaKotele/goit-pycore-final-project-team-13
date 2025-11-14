from collections import UserDict

class Notebook(UserDict):
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
