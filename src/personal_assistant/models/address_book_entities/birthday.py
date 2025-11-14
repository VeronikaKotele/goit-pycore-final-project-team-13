"""
Birthday Module

This module provides the Birthday class for representing and managing birthday
dates in the address book system. The class validates date formats and ensures
that birthdays are in the past or present.

The class uses the DD.MM.YYYY format for date input and validation.
"""

from datetime import datetime

class Birthday:
    """
    Represents a birthday date for a contact.
    
    This class validates and stores birthday dates, ensuring they are in the
    correct format (DD.MM.YYYY) and not in the future.
    
    Attributes:
        value (datetime): The birthday date as a datetime object
    """
    
    def __init__(self, value: str):
        """
        Initialize a Birthday object with date validation.
        
        Args:
            value (str): The birthday date in DD.MM.YYYY format
            
        Raises:
            ValueError: If the date format is invalid or if date parsing fails
        """
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
            if date <= datetime.now():
                self.value = date
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        """
        Return the string representation of the birthday.
        
        Returns:
            str: The birthday date formatted as DD.MM.YYYY
        """
        return self.value.strftime("%d.%m.%Y")
