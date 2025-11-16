import unittest
import sys
import os
from datetime import date
from unittest.mock import patch

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from personal_assistant.managers import AddressBookManager
from personal_assistant.models import Phone, Birthday, HomeAddress


class TestAddressBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = AddressBookManager()
        self.john_record = self.manager.add_record("John Doe")

    def tearDown(self):
        if os.path.exists("addressbook_state.pkl"):
            os.remove("addressbook_state.pkl")

    def test_find_existing_record(self):
        """Test finding an existing record."""
        result = self.manager.find("John Doe")
        self.assertEqual(result.name, "John Doe")

    def test_find_non_existing_record(self):
        """Test finding a non-existing record returns None."""
        result = self.manager.find("Non Existent")
        self.assertIsNone(result)

    def test_delete_existing_record(self):
        """Test deleting an existing record."""
        deleted_record = self.manager.delete("John Doe")
        self.assertEqual(deleted_record.name, "John Doe")
        self.assertIsNone(self.manager.find("John Doe"))

    def test_delete_non_existing_record(self):
        """Test deleting a non-existing record raises KeyError."""
        with self.assertRaises(KeyError) as context:
            self.manager.delete("Non Existent")
        self.assertIn("No record found for Non Existent", str(context.exception))

    def test_add_phone_to_existing_record(self):
        """Test adding a phone to an existing record."""
        phone = Phone("9876543210")
        result = self.manager.add_phone("John Doe", phone)
        self.assertEqual(result.name, "John Doe")
        self.assertIn(phone, result.phones)

    def test_add_phone_to_non_existing_record(self):
        """Test adding a phone to a non-existing record raises KeyError."""
        with self.assertRaises(KeyError) as context:
            self.manager.add_phone("Non Existent", Phone("1234567890"))
        self.assertIn("No record found for Non Existent", str(context.exception))

    def test_add_new_phone_to_existing_record(self):
        """Test adding a phone to an existing record."""
        phone1 = Phone("1234567890")
        self.manager.add_phone("John Doe", phone1)
        phone2 = Phone("9876543210")
        result = self.manager.add_phone("John Doe", phone2)
        self.assertEqual(result.name, "John Doe")
        self.assertIn(phone1, result.phones)
        self.assertIn(phone2, result.phones)

    def test_remove_phone_from_existing_record(self):
        """Test removing a phone from an existing record."""
        phone = Phone("1234567890")
        self.manager.add_phone("John Doe", phone)
        self.manager.remove_phone("John Doe", phone)
        record = self.manager.find("John Doe")
        self.assertNotIn(phone, record.phones)

    def test_remove_phone_from_non_existing_record(self):
        """Test removing a phone from a non-existing record raises KeyError."""
        with self.assertRaises(KeyError) as context:
            self.manager.remove_phone("Non Existent", Phone("1234567890"))
        self.assertIn("No record found for Non Existent", str(context.exception))

    def test_remove_non_existing_phone(self):
        """Test removing a phone from a non-existing record raises KeyError."""
        self.manager.add_phone("John Doe", Phone("1234567890"))
        with self.assertRaises(KeyError) as context:
            self.manager.remove_phone("John Doe", Phone("9876543210"))
        self.assertIn('Phone number 9876543210 does not exist for contact John Doe.', str(context.exception))

    def test_add_birthday(self):
        """Test adding a birthday to an existing record."""
        birthday = Birthday("01.01.1990")
        result = self.manager.add_birthday("John Doe", birthday)
        self.assertEqual(result.name, "John Doe")
        self.assertEqual(result.birthday, birthday)

    def test_add_address(self):
        """Test adding an address to an existing record."""
        address = HomeAddress("123 Main St")
        result = self.manager.add_address("John Doe", address)
        self.assertEqual(result.name, "John Doe")
        self.assertEqual(result.address, address)

    def test_get_upcoming_birthdays_with_results(self):
        """Test getting upcoming birthdays with mocked date."""
        fixed_date = date(2024, 1, 1)  # January 1, 2024

        # Add a birthday that will be "upcoming" relative to our fixed date
        # January 3, 1990 - so next birthday would be January 3, 2024 (2 days from fixed date)
        self.manager.add_birthday("John Doe", Birthday("03.01.1990"))
        
        with patch('personal_assistant.managers.address_book_manager.datetime') as mock_datetime:
            mock_datetime.now.return_value.date.return_value = fixed_date
            
            # Mock the get_next_birthday method for John's record
            john_record = self.manager.find("John Doe")
            next_birthday_date = date(2024, 1, 3)  # 2 days from fixed date
            
            with patch.object(john_record, 'get_next_birthday', return_value=next_birthday_date):
                upcoming = self.manager.get_upcoming_birthdays(7)
                self.assertEqual(len(upcoming), 1)
                self.assertEqual(upcoming[0]["name"], "John Doe")
                self.assertEqual(upcoming[0]["next_date"], next_birthday_date)

    def test_get_upcoming_birthdays_no_results(self):
        """Test getting upcoming birthdays with no results."""
        fixed_date = date(2024, 1, 1)  # January 1, 2024
        
        with patch('personal_assistant.managers.address_book_manager.datetime') as mock_datetime:
            mock_datetime.now.return_value.date.return_value = fixed_date
            
            # Add a birthday that won't be upcoming (more than 7 days away)
            self.manager.add_birthday("John Doe", Birthday("15.01.1990"))
            
            # Mock get_next_birthday to return a date outside the 7-day window
            john_record = self.manager.find("John Doe")
            future_birthday_date = date(2024, 1, 15)  # 14 days from fixed date
            
            with patch.object(john_record, 'get_next_birthday', return_value=future_birthday_date):
                upcoming = self.manager.get_upcoming_birthdays(7)
                self.assertEqual(len(upcoming), 0)
    
    def test_get_upcoming_birthdays_multiple_scenarios(self):
        """Test various birthday scenarios with mocked dates."""
        fixed_date = date(2024, 6, 15)  # June 15, 2024
        
        with patch('personal_assistant.managers.address_book_manager.datetime') as mock_datetime:
            mock_datetime.now.return_value.date.return_value = fixed_date
            
            # Add multiple people with different birthdays
            linda_record = self.manager.add_record("Linda Brown")
            self.manager.add_birthday("Linda Brown", Birthday("16.06.1990"))  # Tomorrow
            jane_record = self.manager.add_record("Jane Smith")
            self.manager.add_birthday("Jane Smith", Birthday("20.06.1985"))  # In 5 days
            bob_record = self.manager.add_record("Bob Wilson")
            self.manager.add_birthday("Bob Wilson", Birthday("25.06.1995"))  # In 10 days (outside window)
            
            # Mock each record's get_next_birthday method
            linda_next = date(2024, 6, 16)  # Tomorrow (1 day away)
            jane_next = date(2024, 6, 20)   # 5 days away
            bob_next = date(2024, 6, 25)    # 10 days away
            
            with patch.object(linda_record, 'get_next_birthday', return_value=linda_next), \
                 patch.object(jane_record, 'get_next_birthday', return_value=jane_next), \
                 patch.object(bob_record, 'get_next_birthday', return_value=bob_next):
                
                # Test with 7-day window - should find Linda and Jane, but not Bob
                upcoming = self.manager.get_upcoming_birthdays(7)
                self.assertEqual(len(upcoming), 2)
                names = [entry["name"] for entry in upcoming]
                self.assertIn("Linda Brown", names)
                self.assertIn("Jane Smith", names)
                self.assertNotIn("Bob Wilson", names)
                
                # Test with 15-day window - should find all three
                upcoming_15 = self.manager.get_upcoming_birthdays(15)
                self.assertEqual(len(upcoming_15), 3)
    
    def test_get_upcoming_birthdays_today(self):
        """Test birthday that occurs today."""
        fixed_date = date(2024, 3, 10)  # March 10, 2024
        
        with patch('personal_assistant.managers.address_book_manager.datetime') as mock_datetime:
            mock_datetime.now.return_value.date.return_value = fixed_date
            
            # Add someone with birthday today
            birthday_record = self.manager.add_record("Birthday Person")
            self.manager.add_birthday("Birthday Person", Birthday("10.03.1990"))
            
            # Mock get_next_birthday to return today's date
            with patch.object(birthday_record, 'get_next_birthday', return_value=fixed_date):
                upcoming = self.manager.get_upcoming_birthdays(7)
                self.assertEqual(len(upcoming), 1)
                self.assertEqual(upcoming[0]["name"], "Birthday Person")
                self.assertEqual(upcoming[0]["next_date"], fixed_date)

    def test_add_duplicate_phone_raises_error(self):
        """Test adding duplicate phone raises ValueError."""
        phone = Phone("1234567890")
        self.manager.add_phone("John Doe", phone)
        
        # Adding the same phone again should raise ValueError
        with self.assertRaises(ValueError) as context:
            self.manager.add_phone("John Doe", phone)
        self.assertIn("already exists", str(context.exception))

    def test_update_birthday_overwrites_previous(self):
        """Test that adding a new birthday overwrites the previous one."""
        birthday1 = Birthday("01.01.1990")
        birthday2 = Birthday("02.02.1991")
        
        record = self.manager.add_birthday("John Doe", birthday1)
        self.assertEqual(record.birthday, birthday1)
        
        record = self.manager.add_birthday("John Doe", birthday2)
        self.assertEqual(record.birthday, birthday2)

    def test_update_address_overwrites_previous(self):
        """Test that adding a new address overwrites the previous one."""
        address1 = HomeAddress("123 Main St")
        address2 = HomeAddress("456 Oak Ave")
        
        record = self.manager.add_address("John Doe", address1)
        self.assertEqual(record.address, address1)
        
        record = self.manager.add_address("John Doe", address2)
        self.assertEqual(record.address, address2)

    def test_all_manager_methods_exist(self):
        """Test that all expected methods exist on the manager."""
        expected_methods = [
            'find', 'delete', 'add_phone', 'remove_phone', 
            'add_birthday', 'add_address', 'get_upcoming_birthdays'
        ]
        
        for method_name in expected_methods:
            self.assertTrue(hasattr(self.manager, method_name), 
                          f"Manager should have {method_name} method")

    def test_delete_record_returns_deleted_record(self):
        """Test that delete returns the deleted record."""
        deleted = self.manager.delete("John Doe")
        self.assertEqual(deleted.name, "John Doe")

    def test_operations_on_same_record_instance(self):
        """Test that operations on the same record name work on the same instance."""
        phone = Phone("1234567890")
        birthday = Birthday("01.01.1990")
        address = HomeAddress("123 Main St")
        
        phone_result = self.manager.add_phone("John Doe", phone)
        birthday_result = self.manager.add_birthday("John Doe", birthday)
        address_result = self.manager.add_address("John Doe", address)
        
        # All operations should return the same record instance
        self.assertEqual(phone_result, birthday_result)
        self.assertEqual(birthday_result, address_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)