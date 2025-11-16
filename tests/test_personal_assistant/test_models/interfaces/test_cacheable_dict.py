import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src'))

from personal_assistant.models.interfaces import CacheableDict

class TestCacheableDict(unittest.TestCase):
    def setUp(self):
        self.pklfile = "test_cache.pkl"
        if os.path.exists("test_cache.pkl"):
            os.remove("test_cache.pkl")

    def tearDown(self):
        if os.path.exists("test_cache.pkl"):
            os.remove("test_cache.pkl")

    def test_creates_new_when_no_file(self):
        cacheable_dict = CacheableDict(self.pklfile)
        self.assertEqual(len(cacheable_dict), 0)

    def test_saves_to_file(self):
        cacheable_dict = CacheableDict(self.pklfile)
        cacheable_dict['key1'] = 'value1'
        del cacheable_dict
        assert os.path.exists(self.pklfile)

    def test_restore_data_from_file(self):
        old_dict = CacheableDict(self.pklfile)
        old_dict['key1'] = 'value1'
        del old_dict

        cacheable_dict = CacheableDict(self.pklfile)
        self.assertEqual(len(cacheable_dict), 1)
        self.assertEqual(cacheable_dict['key1'], 'value1')

if __name__ == '__main__':
    unittest.main(verbosity=2)