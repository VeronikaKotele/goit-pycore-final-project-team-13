from models.cacheable_dict import CacheableDict

class Notebook(CacheableDict):
    def __init__(self):
        CacheableDict.__init__(self, "notes_state.pkl")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
