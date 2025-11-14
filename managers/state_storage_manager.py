"""
State Storage Manager Module

This module provides the StateStorageManager class for persistent storage
of application state using pickle serialization. It handles loading and
saving of cached state to maintain data between application sessions.

The manager provides automatic persistence through destructor-based saving
and lazy loading of state data.
"""

import pickle


class Cacheablegg:
    """
    State storage manager for persistent data caching.
    
    This class handles loading and saving of application state using pickle
    serialization. It provides automatic persistence through destructor-based
    saving and supports manual state updates.
    
    Attributes:
        __state_storage_filename (str): The filename for state persistence
        cached_state (object): The current cached state object
    """
    
    def __init__(self, filename):
        """
        Initialize the state storage manager.
        
        Args:
            filename (str): The filename to use for state persistence
        """
        self.__state_storage_filename = filename
        self.cached_state = self.try_load()

    def __del__(self):
        """
        Destructor that automatically saves the cached state.
        
        This ensures that state is persisted when the object is garbage collected.
        """
        print("calling destructor for StateStorageManager")
        self.save()

    def try_load(self) -> object | None:
        """
        Attempt to load cached state from the storage file.
        
        Returns:
            object or None: The loaded state object, or None if loading fails
        """
        try:
            with open(self.__state_storage_filename, "rb") as f:
                data = pickle.load(f)
                return data
        except FileNotFoundError:
            pass # keep default UserDict initialization with empty data
        return None

    def save(self):
        """
        Save the current cached state to the storage file.
        
        Uses pickle to serialize the cached_state object to the configured filename.
        """
        with open(self.__state_storage_filename, "wb") as f:
            pickle.dump(self.cached_state, f)

    def update_cache(self, new_state: object):
        """
        Update the cached state with a new state object.
        
        Args:
            new_state (object): The new state object to cache
        """
        self.cached_state = new_state
