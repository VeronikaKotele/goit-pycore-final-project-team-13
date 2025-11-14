"""
Notebook Module

This module provides the Notebook class, which is a specialized CacheableDict
for storing and managing notes. It provides automatic persistence of notes
and methods for displaying all notes in a formatted manner.

The notebook stores notes as key-value pairs where keys are note titles
and values are note contents.
"""

from .cacheable_dict import CacheableDict

class Notebook(CacheableDict):
    """
    A notebook for storing and managing notes with automatic persistence.
    
    This class extends CacheableDict to provide a specialized storage container
    for notes. Notes are automatically persisted to 'notes_state.pkl' file.
    """
    
    def __init__(self):
        """
        Initialize a Notebook with automatic persistence to 'notes_state.pkl'.
        """
        CacheableDict.__init__(self, "notes_state.pkl")

    def __str__(self):
        """
        Return a string representation of all notes in the notebook.
        
        Returns:
            str: A formatted string containing all note records, one per line
        """
        return "\n".join(str(record) for record in self.data.values())
