import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src'))

from personal_assistant.models import Phone

class TestPhone(unittest.TestCase):
    def test_phone_creation_with_plus(self):
        phone = Phone("+380501234567")
        self.assertEqual(str(phone), "+380501234567")

    def test_phone_creation_without_plus(self):
        phone = Phone("0501234567")
        self.assertEqual(str(phone), "+380501234567")

    def test_phone_creation_short_number_starting_with_0(self):
        phone = Phone("01234567")
        self.assertEqual(str(phone), "01234567")

    def test_phone_creation_short_number_not_starting_with_0(self):
        phone = Phone("12345678")
        self.assertEqual(str(phone), "12345678")

    def test_phone_invalid_format(self):
        with self.assertRaises(ValueError):
            Phone("123-456-7890")

    def test_phone_too_short(self):
        with self.assertRaises(ValueError):
            Phone("12345")

    def test_phone_too_long(self):
        with self.assertRaises(ValueError):
            Phone("+12345678901234567")

if __name__ == '__main__':
    unittest.main(verbosity=2)