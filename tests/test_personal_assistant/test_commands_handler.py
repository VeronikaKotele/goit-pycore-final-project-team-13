import unittest
from personal_assistant import CommandsHandler

class TestCommandsHandler(unittest.TestCase):
    def test_get_help(self):
        handler = CommandsHandler()
        help_message = handler.get_help()
        self.assertIn("Available commands:", help_message)
        self.assertIn("add-phone", help_message)
        self.assertIn("remove-phone", help_message)

    def test_add_phone(self, name, phone):
        pass

    def test_remove_phone(self, name, phone):
        pass
    def test_add_birthday(self, name, birthday):
        pass

    def test_add_address(self, name, **args):
        pass

    def test_upcoming_birthdays(self, days):
        pass
    def test_show_contact(self, name):
        pass
    
    def test_delete_contact(self, name):
        pass
        

    def test_add_note(self, **args):
        pass

    def test_update_note(self, title, content):
        pass
    def test_delete_note(self, title):
        pass
    def test_show_note(self, title):
        pass
    def test_show_all_contacts(self):
        pass
    def test_show_all_notes(self):
        pass
    def get_help(self):
        pass

    def test_execute_command(self, cmd_name: str, args: list[str]):
        pass