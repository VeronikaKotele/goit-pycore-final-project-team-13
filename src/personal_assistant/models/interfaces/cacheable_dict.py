import pickle
from collections import UserDict

class CacheableDict(UserDict):
    """
    A dictionary with automatic persistence capabilities.
    
    This class extends UserDict to provide automatic loading and saving of
    dictionary data using pickle serialization. Data is loaded from a file
    during initialization and automatically saved when the object is destroyed.
    
    Attributes:
        __state_storage_filename (str): The filename used for persistence
    """

    def __init__(self, filename):
        """
        Constructor that loads existing dictionary data from the specified file if it exists
        """
        self.__state_storage_filename = filename
        super().__init__()
        try:
            with open(self.__state_storage_filename, "rb") as f:
                data = pickle.load(f)
                self.data.update(data)
        except FileNotFoundError:
            pass # do nothing

    def save_data_to_cache(self):
        """
        Destructor that automatically saves the dictionary data.
        
        Uses pickle to serialize the current dictionary data to the storage file.
        This ensures data persistence when the object is garbage collected.
        """
        try:
            with open(self.__state_storage_filename, "wb") as f:
                pickle.dump(self.data, f)
        except Exception as e:
            print(f"ERROR saving cache data: {e}")
