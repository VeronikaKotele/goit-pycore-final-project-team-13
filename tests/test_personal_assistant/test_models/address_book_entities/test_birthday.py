import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src'))

from personal_assistant.models import Birthday

class TestBirthday(unittest.TestCase):
    def test_birthday_creation(self):
        bday = Birthday("30.10.2001")
        self.assertEqual(str(bday), "30.10.2001")

    def test_birthday_invalid_format(self):
        with self.assertRaises(ValueError):
            Birthday("01-01-1990")

    def test_birthday_invalid_format_order(self):
        with self.assertRaises(ValueError):
            Birthday("1990.01.01")

    def test_birthday_in_future(self):
        future_date = "01.01.3000"
        with self.assertRaises(ValueError):
            Birthday(future_date)

if __name__ == '__main__':
    unittest.main(verbosity=2)