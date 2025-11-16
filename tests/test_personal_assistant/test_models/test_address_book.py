import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from personal_assistant.models import AddressBook, AddressBookRecord

class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()

    def tearDown(self):
        if os.path.exists("addressbook_state.pkl"):
            os.remove("addressbook_state.pkl")

    def test_add_record(self):
        self.address_book["John Doe"] = AddressBookRecord("John Doe")
        self.assertIn("John Doe", self.address_book.keys())
        self.assertEqual(self.address_book["John Doe"], self.address_book["John Doe"])

    def test_add_invalid_record_raises(self):
        with self.assertRaises(TypeError):
            self.address_book["Jane Doe"] = "Not a Record"

if __name__ == '__main__':
    unittest.main(verbosity=2)