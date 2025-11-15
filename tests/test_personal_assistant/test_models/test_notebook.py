import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from personal_assistant.models import Notebook

class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()

    def tearDown(self):
        if os.path.exists("notebook_state.pkl"):
            os.remove("notebook_state.pkl")

    def test_add_string(self):
        self.notebook["ToDo list"] = "Buy milk"
        self.assertIn("ToDo list", self.notebook.keys())
        self.assertEqual(self.notebook["ToDo list"], "Buy milk")

    def test_add_not_string_raises(self):
        with self.assertRaises(TypeError):
            self.notebook["ToDo list"] = 12345  # Not a string

if __name__ == '__main__':
    unittest.main(verbosity=2)