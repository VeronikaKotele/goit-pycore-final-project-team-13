"""
Summary: How to mock today's date for consistent test results in get_upcoming_birthdays tests

The updated tests in test_address_book_manager.py now follow the recommended mocking approach:

## ✅ Updated Pattern (Now Used):

```python
def test_get_upcoming_birthdays_with_results(self):
    fixed_date = date(2024, 1, 1)  # January 1, 2024
    
    # Add birthday data
    self.manager.add_birthday("John Doe", Birthday("03.01.1990"))
    
    # Mock datetime.now() in the AddressBookManager
    with patch('personal_assistant.managers.address_book_manager.datetime') as mock_datetime:
        mock_datetime.now.return_value.date.return_value = fixed_date
        
        # Mock each record's get_next_birthday method
        john_record = self.manager.find("John Doe")
        next_birthday_date = date(2024, 1, 3)  # 2 days from fixed date
        
        with patch.object(john_record, 'get_next_birthday', return_value=next_birthday_date):
            upcoming = self.manager.get_upcoming_birthdays(7)
            # Assert results...
```

## Key Changes Made:

1. **Proper datetime patching**: 
   - Target: `'personal_assistant.managers.address_book_manager.datetime'`
   - Pattern: `mock_datetime.now.return_value.date.return_value = fixed_date`

2. **Individual record mocking**:
   - Each record's `get_next_birthday()` method is mocked separately
   - Uses `patch.object(record, 'get_next_birthday', return_value=date_value)`

3. **Multiple records handled**:
   - Multiple `patch.object()` calls in context managers
   - Each record gets its own specific next birthday date

4. **Removed helper method**:
   - Direct patching is clearer and more explicit
   - Each test shows exactly what it's mocking

## Tests Updated:

✅ `test_get_upcoming_birthdays_with_results` - Single record with upcoming birthday
✅ `test_get_upcoming_birthdays_no_results` - Record with birthday outside window  
✅ `test_get_upcoming_birthdays_multiple_scenarios` - Multiple records with different dates
✅ `test_get_upcoming_birthdays_today` - Birthday occurring on the test date

## Benefits:

- **Deterministic**: Tests always run with the same "today" date
- **Flexible**: Each test can set its own scenario dates
- **Clear**: Explicit mocking shows exactly what each test is testing
- **Maintainable**: Easy to understand and modify

## Usage Pattern:

1. Set your fixed test date: `fixed_date = date(2024, 1, 1)`
2. Patch the datetime module: `patch('personal_assistant.managers.address_book_manager.datetime')`
3. Configure the mock: `mock_datetime.now.return_value.date.return_value = fixed_date`
4. Mock each record's get_next_birthday: `patch.object(record, 'get_next_birthday', return_value=expected_date)`
5. Run your test logic
6. Assert expected results

This approach ensures tests are consistent, repeatable, and don't depend on the actual current date!
"""