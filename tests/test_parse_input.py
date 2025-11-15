import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import parse_input

class TestParseInput(unittest.TestCase):
    
    # Standard cases
    def test_single_word(self):
        """Test parsing a single command word."""
        cmd, args = parse_input("hello")
        self.assertEqual(cmd, "hello")
        self.assertEqual(args, [])
    
    def test_command_with_single_argument(self):
        """Test parsing command with one argument."""
        cmd, args = parse_input("add John")
        self.assertEqual(cmd, "add")
        self.assertEqual(args, ["John"])
    
    def test_command_with_multiple_arguments(self):
        """Test parsing command with multiple arguments."""
        cmd, args = parse_input("add-phone John 1234567890")
        self.assertEqual(cmd, "add-phone")
        self.assertEqual(args, ["John", "1234567890"])
    
    def test_command_case_insensitive(self):
        """Test that commands are converted to lowercase."""
        cmd, args = parse_input("ADD-PHONE John 1234567890")
        self.assertEqual(cmd, "add-phone")
        self.assertEqual(args, ["John", "1234567890"])
    
    def test_mixed_case_command(self):
        """Test mixed case command conversion."""
        cmd, args = parse_input("AdD-PhOnE John 1234567890")
        self.assertEqual(cmd, "add-phone")
        self.assertEqual(args, ["John", "1234567890"])
    
    # Quoted string handling
    def test_quoted_single_argument(self):
        """Test parsing argument with quotes."""
        cmd, args = parse_input('add "John Doe"')
        self.assertEqual(cmd, "add")
        self.assertEqual(args, ["John Doe"])
    
    def test_quoted_multiple_arguments(self):
        """Test parsing multiple quoted arguments."""
        cmd, args = parse_input('add-address "John Doe" "123 Main Street" "New York"')
        self.assertEqual(cmd, "add-address")
        self.assertEqual(args, ["John Doe", "123 Main Street", "New York"])
    
    def test_mixed_quoted_and_unquoted(self):
        """Test mixing quoted and unquoted arguments."""
        cmd, args = parse_input('add-note "Important Note" urgent personal')
        self.assertEqual(cmd, "add-note")
        self.assertEqual(args, ["Important Note", "urgent", "personal"])
    
    def test_single_quotes(self):
        """Test parsing with single quotes."""
        cmd, args = parse_input("add-note 'Meeting tomorrow' urgent")
        self.assertEqual(cmd, "add-note")
        self.assertEqual(args, ["Meeting tomorrow", "urgent"])
    
    # Edge cases with whitespace
    def test_empty_string(self):
        """Test parsing empty string."""
        cmd, args = parse_input("")
        self.assertEqual(cmd, "")
        self.assertEqual(args, [])
    
    def test_whitespace_only(self):
        """Test parsing string with only whitespace."""
        cmd, args = parse_input("   ")
        self.assertEqual(cmd, "")
        self.assertEqual(args, [])
    
    def test_leading_trailing_whitespace(self):
        """Test parsing with leading and trailing whitespace."""
        cmd, args = parse_input("  add John  ")
        self.assertEqual(cmd, "add")
        self.assertEqual(args, ["John"])
    
    def test_multiple_spaces_between_args(self):
        """Test parsing with multiple spaces between arguments."""
        cmd, args = parse_input("add-phone    John     1234567890")
        self.assertEqual(cmd, "add-phone")
        self.assertEqual(args, ["John", "1234567890"])
    
    def test_tabs_and_spaces(self):
        """Test parsing with tabs and spaces."""
        cmd, args = parse_input("add-phone\tJohn\t\t1234567890")
        self.assertEqual(cmd, "add-phone")
        self.assertEqual(args, ["John", "1234567890"])
    
    # Special characters and edge cases
    def test_command_with_special_characters(self):
        """Test parsing command with hyphens and underscores."""
        cmd, args = parse_input("show_all-contacts")
        self.assertEqual(cmd, "show_all-contacts")
        self.assertEqual(args, [])
    
    def test_arguments_with_special_characters(self):
        """Test parsing arguments with special characters."""
        cmd, args = parse_input("add-email John john@example-site.com")
        self.assertEqual(cmd, "add-email")
        self.assertEqual(args, ["John", "john@example-site.com"])
    
    def test_arguments_with_numbers(self):
        """Test parsing arguments with numbers."""
        cmd, args = parse_input("add-phone John123 +1-234-567-8900")
        self.assertEqual(cmd, "add-phone")
        self.assertEqual(args, ["John123", "+1-234-567-8900"])
    
    def test_quoted_string_with_spaces_and_punctuation(self):
        """Test quoted string with spaces and punctuation."""
        cmd, args = parse_input('add-note "Call Dr. Smith at 3:00 PM!" urgent')
        self.assertEqual(cmd, "add-note")
        self.assertEqual(args, ["Call Dr. Smith at 3:00 PM!", "urgent"])
    
    def test_empty_quoted_string(self):
        """Test parsing empty quoted string."""
        cmd, args = parse_input('add-note "" personal')
        self.assertEqual(cmd, "add-note")
        self.assertEqual(args, ["", "personal"])
    
    def test_quoted_string_with_quotes_inside(self):
        """Test quoted string containing escaped quotes."""
        cmd, args = parse_input('add-note "She said \\"Hello!\\"" personal')
        self.assertEqual(cmd, "add-note")
        self.assertEqual(args, ['She said "Hello!"', "personal"])
    
    # Real-world usage scenarios
    def test_add_contact_full_info(self):
        """Test realistic add contact command."""
        cmd, args = parse_input('add-contact "John Doe" "555-123-4567" "john@email.com"')
        self.assertEqual(cmd, "add-contact")
        self.assertEqual(args, ["John Doe", "555-123-4567", "john@email.com"])
    
    def test_add_address_command(self):
        """Test realistic add address command."""
        cmd, args = parse_input('add-address "Jane Smith" "123 Oak Street" "Apartment 4B" "New York" "NY" "10001"')
        self.assertEqual(cmd, "add-address")
        self.assertEqual(args, ["Jane Smith", "123 Oak Street", "Apartment 4B", "New York", "NY", "10001"])
    
    def test_search_command(self):
        """Test search command with quoted search term."""
        cmd, args = parse_input('search "John D"')
        self.assertEqual(cmd, "search")
        self.assertEqual(args, ["John D"])
    
    def test_note_with_long_text(self):
        """Test adding note with long text."""
        long_text = "This is a very long note with multiple words and punctuation marks!"
        cmd, args = parse_input(f'add-note "{long_text}" work')
        self.assertEqual(cmd, "add-note")
        self.assertEqual(args, [long_text, "work"])
    
    # Error handling and malformed input
    def test_unclosed_quote(self):
        """Test handling of unclosed quote (should raise ValueError from shlex)."""
        with self.assertRaises(ValueError):
            parse_input('add-note "unclosed quote')
    
    def test_mismatched_quotes(self):
        """Test handling of mismatched quotes."""
        with self.assertRaises(ValueError):
            parse_input('add-note "mixed quote\'')
    
    def test_backslash_escaping(self):
        """Test backslash escaping in arguments."""
        cmd, args = parse_input(r'add-note "Path: C:\Users\John" personal')
        self.assertEqual(cmd, "add-note")
        self.assertEqual(args, [r"Path: C:\Users\John", "personal"])
    
    def test_unicode_characters(self):
        """Test parsing with unicode characters."""
        cmd, args = parse_input('add-contact "José María" "café@email.com"')
        self.assertEqual(cmd, "add-contact")
        self.assertEqual(args, ["José María", "café@email.com"])
    
    def test_very_long_command(self):
        """Test parsing very long command line."""
        long_args = ["arg" + str(i) for i in range(50)]
        input_str = "command " + " ".join(long_args)
        cmd, args = parse_input(input_str)
        self.assertEqual(cmd, "command")
        self.assertEqual(args, long_args)