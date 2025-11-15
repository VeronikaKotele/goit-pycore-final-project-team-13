from personal_assistant.models import Notebook

class NotesManager:
    def __init__(self):
        self.__notebook = Notebook()

    def __clearQuotes(self, text: str) -> str:
        return text.strip().strip("'\"")

    def add_note(self, **args):
        # Handle special case for commands with arguments containing colons (e.g., notes)
        # Join args back into a single string and split by the first colon
        joined_args = " ".join(args)
        if ":" in joined_args:
            title, content = joined_args.split(":", 1)
        else:
            raise ValueError("Invalid note format. Use: 'title': 'content'")

        # Clean up title and content by stripping whitespace and quotes
        title = self.__clearQuotes(title)
        content = self.__clearQuotes(content)

        note_exists = self.__notebook.get(title)
        if note_exists:
            raise ValueError(f"Note with title '{title}' already exists.")
        self.__notebook[title] = content

    def update(self, title: str, content: str):
        title = self.__clearQuotes(title)
        content = self.__clearQuotes(content)
        if title in self.__notebook:
            self.__notebook[title] = content
        else:
            raise KeyError(f"Note with title '{title}' not found.")

    def find(self, title: str):
        title = self.__clearQuotes(title)
        return self.__notebook.get(title) or None

    def delete(self, title: str):
        title = self.__clearQuotes(title)
        if title in self.__notebook:
            del self.__notebook[title]
        else:
            raise KeyError(f"Note with title '{title}' not found.")

    def __str__(self):
        return "\n".join(str(record) for record in self.__notebook.data.values())
