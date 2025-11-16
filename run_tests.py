#!/usr/bin/env python3
"""
Test runner script for parse_input tests.
This script sets up the proper Python path and runs the tests.
"""
import sys
import os
import unittest

# Add the src directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

# Import and run the test
if __name__ == '__main__':
    # Import the test module after setting up the path
    from tests.test_parse_input import TestParseInput
    from tests.test_personal_assistant.test_models.address_book_entities.test_phone import TestPhone
    from tests.test_personal_assistant.test_models.address_book_entities.test_email import TestEmail
    from tests.test_personal_assistant.test_models.address_book_entities.test_birthday import TestBirthday
    from tests.test_personal_assistant.test_models.address_book_entities.test_address_book_record import TestAddressBookRecord
    from tests.test_personal_assistant.test_models.interfaces.test_cacheable_dict import TestCacheableDict
    from tests.test_personal_assistant.test_models.test_address_book import TestAddressBook
    from tests.test_personal_assistant.test_models.test_notebook import TestNotebook
    from tests.test_personal_assistant.test_managers.test_address_book_manager import TestAddressBookManager
    from tests.test_personal_assistant.test_managers.test_notes_manager import TestNotesManager
    from tests.test_personal_assistant.test_commands_handler import TestCommandsHandler

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParseInput)

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPhone))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestEmail))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBirthday))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddressBookRecord))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCacheableDict))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddressBook))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestNotebook))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAddressBookManager))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestNotesManager))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCommandsHandler))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with proper code
    sys.exit(0 if result.wasSuccessful() else 1)