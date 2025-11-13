class StateStorageManager:
    def __init__(self, cache_filename):
        self.__cache_filename = cache_filename

    def try_load(self, load_object: object):
        return False # todo: implement loading logic

    def save(self, save_object: object):
        pass
