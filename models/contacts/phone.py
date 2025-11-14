"""
Phone Module

This module provides the Phone class for representing and managing phone numbers
in the address book system. The class stores phone number values and provides
string representation functionality.

Future enhancements should include phone number validation to ensure proper
formatting and validity of phone numbers.
"""

class Phone:
    """
    Represents a phone number for a contact.
    
    This class stores a phone number value and provides string representation.
    Phone number validation should be implemented to ensure proper formatting.
    
    Attributes:
        value: The phone number value (currently accepts any type)
    """
    
    def __init__(self, value):
        """
        Initialize a Phone object with a phone number value.
        
        Args:
            value: The phone number value
            
        Todo:
            Add validation and raise exception for invalid phone numbers.
        """
        # todo validate, raise exeption
        self.value = value

    def __str__(self):
        """
        Return the string representation of the phone number.
        
        Returns:
            str: The phone number as a string
        """
        return str(self.value)
