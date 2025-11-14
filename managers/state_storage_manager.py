import pickle


class Cacheablegg:
    def __init__(self, filename):
        self.__state_storage_filename = filename
        self.cached_state = self.try_load()

    def __del__(self):
        print("calling destructor for StateStorageManager")
        self.save()

    def try_load(self) -> object | None:
        try:
            with open(self.__state_storage_filename, "rb") as f:
                data = pickle.load(f)
                return data
        except FileNotFoundError:
            pass # keep default UserDict initialization with empty data
        return None

    def save(self):
        with open(self.__state_storage_filename, "wb") as f:
            pickle.dump(self.cached_state, f)

    def update_cache(self, new_state: object):
        self.cached_state = new_state
