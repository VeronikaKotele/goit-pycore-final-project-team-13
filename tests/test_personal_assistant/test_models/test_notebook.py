from .interfaces import CacheableDict

class Notebook(CacheableDict):
    """
    A notebook for storing and managing notes with automatic persistence.
    
    This class extends CacheableDict to provide a specialized storage container
    for notes. Notes are automatically persisted to 'notes_state.pkl' file.
    """
    
    def __init__(self):
        CacheableDict.__init__(self, "notes_state.pkl")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
