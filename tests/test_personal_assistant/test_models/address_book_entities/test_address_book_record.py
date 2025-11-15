import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src'))

from personal_assistant.models import AddressBookRecord, Phone, Birthday, HomeAddress, Email

class TestAddressBookRecord(unittest.TestCase):
    def setUp(self):
        self.record = AddressBookRecord("John Doe")

    def test_add_phone(self):
        phone = Phone("1234567890")
        self.record.add_phone(phone)
        self.assertIn(phone, self.record.phones)

    def test_add_duplicate_phone_raises(self):
        phone = Phone("1234567890")
        self.record.add_phone(phone)
        with self.assertRaises(ValueError):
            self.record.add_phone(phone)

    def test_add_birthday(self):
        birthday = Birthday("01.01.1990")
        self.record.add_birthday(birthday)
        self.assertEqual(self.record.birthday, birthday)

    def test_edit_phone(self):
        old_phone = Phone("1234567890")
        new_phone = Phone("0987654321")
        self.record.add_phone(old_phone)
        self.record.edit_phone(old_phone, new_phone)
        self.assertIn(new_phone, self.record.phones)
        self.assertNotIn(old_phone, self.record.phones)

    def test_edit_nonexistent_phone_raises(self):
        old_phone = Phone("1234567890")
        new_phone = Phone("0987654321")
        with self.assertRaises(ValueError):
            self.record.edit_phone(old_phone, new_phone)

    def test_add_email(self):
        email = Email("john.doe@example.com")
        self.record.add_email(email)
        self.assertEqual(email, self.record.email)

    def test_add_home_address(self):
        address = HomeAddress("123 Main St")
        self.record.add_address(address)
        self.assertEqual(self.record.address, address)

    def test_str_representation(self):
        phone = Phone("1234567890")
        birthday = Birthday("31.01.1990")
        address = HomeAddress("123 Main St")
        email = Email("john.doe@example.com")
        self.record.add_phone(phone)
        self.record.add_birthday(birthday)
        self.record.add_address(address)
        self.record.add_email(email)
        expected_str = "Name: John Doe, Phones: [1234567890], Birthday: 31.01.1990, Address: 123 Main St, Email: john.doe@example.com"
        self.assertEqual(str(self.record), expected_str)

if __name__ == '__main__':
    unittest.main(verbosity=2)