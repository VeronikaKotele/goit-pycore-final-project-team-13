"""
Email Module

This module provides the Email class for representing and managing email addresses
in the address book system. The class stores email address values and provides
string representation functionality.

Future enhancements should include email address validation to ensure proper
formatting and validity of email addresses.
"""

class Email:
    """
    Represents an email address for a contact.
    
    This class stores an email address value and provides string representation.
    Email address validation should be implemented to ensure proper formatting.
    
    Attributes:
        value: The email address value (currently accepts any type)
    """
    
    def __init__(self, value):
        """
        Initialize an Email object with an email address value.
        
        Args:
            value: The email address value
            
        Todo:
            Add validation and raise exception for invalid email addresses.
        """
        # todo validate, raise exeption
        self.value = value

    def __str__(self):
        """
        Return the string representation of the email address.
        
        Returns:
            str: The email address as a string
        """
        return str(self.value)
