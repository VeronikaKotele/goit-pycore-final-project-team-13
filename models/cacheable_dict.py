import pickle
from collections import UserDict

class CacheableDict(UserDict):
    def __init__(self, filename):
        print("calling constructor for CacheableDict")
        self.__state_storage_filename = filename
        UserDict.__init__(self)
        try:
            with open(self.__state_storage_filename, "rb") as f:
                data = pickle.load(f)
                self.data.update(data)
        except FileNotFoundError:
            pass # do nothing

    def __del__(self):
        print("calling destructor for CacheableDict")
        with open(self.__state_storage_filename, "wb") as f:
            pickle.dump(self.data, f)
