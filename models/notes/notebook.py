from collections import UserDict

class Notebook(UserDict):
    def __setitem__(self, title: str, note: str):
        value = self.data.get(title)
        if value:
            pass # todo: define update behavior
        else:
            self.data[title] = note

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
    def update_item(self, title: str, note: str):
        """Combine information."""
        pass
