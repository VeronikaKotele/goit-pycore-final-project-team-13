import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src'))

from personal_assistant.models import Email

class TestEmail(unittest.TestCase):
    def test_email_creation_valid(self):
        email = Email("user@example.com")
        self.assertEqual(str(email), "user@example.com")

    def test_email_creation_valid_with_subdomain(self):
        email = Email("user@mail.example.com")
        self.assertEqual(str(email), "user@mail.example.com")

    def test_email_creation_valid_with_plus(self):
        email = Email("user+tag@example.com")
        self.assertEqual(str(email), "user+tag@example.com")

    def test_email_creation_valid_with_dots(self):
        email = Email("first.last@example.com")
        self.assertEqual(str(email), "first.last@example.com")

    def test_email_creation_valid_with_numbers(self):
        email = Email("user123@example456.com")
        self.assertEqual(str(email), "user123@example456.com")

    def test_email_creation_valid_long_tld(self):
        email = Email("user@example.co.uk")
        self.assertEqual(str(email), "user@example.co.uk")

    def test_email_creation_valid_with_hyphen_domain(self):
        email = Email("user@my-domain.com")
        self.assertEqual(str(email), "user@my-domain.com")

    def test_email_creation_valid_with_underscore(self):
        email = Email("user_name@example.com")
        self.assertEqual(str(email), "user_name@example.com")

    def test_email_creation_valid_with_percent(self):
        email = Email("user%test@example.com")
        self.assertEqual(str(email), "user%test@example.com")

    def test_email_creation_invalid_no_at(self):
        with self.assertRaises(ValueError):
            Email("userexample.com")

    def test_email_creation_invalid_no_domain(self):
        with self.assertRaises(ValueError):
            Email("user@.com")

    def test_email_creation_invalid_no_tld(self):
        with self.assertRaises(ValueError):
            Email("user@example")

    def test_email_creation_invalid_double_at(self):
        with self.assertRaises(ValueError):
            Email("user@@example.com")

    def test_email_creation_invalid_spaces(self):
        with self.assertRaises(ValueError):
            Email("user @example.com")

    def test_email_creation_invalid_tld_too_short(self):
        with self.assertRaises(ValueError):
            Email("user@example.c")

    def test_email_creation_invalid_no_local_part(self):
        with self.assertRaises(ValueError):
            Email("@example.com")

    def test_email_creation_invalid_special_chars(self):
        with self.assertRaises(ValueError):
            Email("user#name@example.com")

    def test_email_creation_invalid_empty_string(self):
        with self.assertRaises(ValueError):
            Email("")

    def test_email_creation_invalid_missing_domain_name(self):
        with self.assertRaises(ValueError):
            Email("user@.example.com")

if __name__ == '__main__':
    unittest.main(verbosity=2)