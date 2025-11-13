import pickle

class StateStorageManager:
    def __init__(self, cache_filename):
        self.__cache_filename = cache_filename

    def try_load(self, load_object: object):
        try:
            with open(self.__cache_filename, "rb") as f:
                data = pickle.load(f)
                if data and isinstance(data, load_object.__class__):
                    load_object.__dict__.update(data.__dict__)
                    return True
        except FileNotFoundError:
            pass
        return False

    def save(self, save_object: object):
        with open(self.__cache_filename, "wb") as f:
            pickle.dump(save_object, f)
