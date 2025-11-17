class Note:
    def __init__(self, title: str, content: str, tags: list[str] = None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        tags_str = f" (tags: {', '.join(self.tags)})" if self.tags else ""
        return f"{self.title}: {self.content}{tags_str}"