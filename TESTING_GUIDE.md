# Testing Best Practices for Python Projects

## Project Structure
```
project_root/
├── src/                          # Source code
│   ├── __init__.py               # Makes src a package
│   ├── main.py                   # Main module with parse_input function
│   └── personal_assistant/       # Main application package
│       ├── __init__.py
│       ├── commands_handler.py
│       └── ...
├── tests/                        # Test directory (outside src)
│   ├── __init__.py               # Makes tests a package
│   ├── conftest.py               # Test configuration
│   ├── test_*                    # Test files following original modiles structure
|   └── ...
├── setup.py                      # Package configuration
├── pytest.ini                    # Test runner configuration
└── run_tests.py                  # Custom test runner
```

## Import Setup

### 1. Test Configuration (`conftest.py`)
```python
import sys
import os

# Add the src directory to Python path
project_root = os.path.dirname(__file__)
src_path = os.path.join(project_root, '..', 'src')
sys.path.insert(0, os.path.abspath(src_path))
```

### 2. Test File Imports
```python
import unittest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import parse_input  # Import from your source modules
```

## Running Tests

### Option 1: Using the Custom Runner
```bash
python run_tests.py
```

### Option 2: Using unittest directly
```bash
python -m unittest tests.test_parse_input -v
```

### Option 3: Using pytest (if installed)
```bash
pip install pytest
pytest tests/ -v
```

## Best Practices

1. **Descriptive Test Names**: Each test method clearly describes what it tests
2. **Docstrings**: Every test has a docstring explaining its purpose
3. **Comprehensive Coverage**: Tests cover normal usage, edge cases, and error conditions
4. **Isolated Tests**: Each test is independent and can run alone
5. **Proper Assertions**: Using appropriate unittest assertion methods
6. **Error Testing**: Testing both success and failure scenarios

## Adding New Tests

When adding new tests, follow this pattern:

```python
def test_descriptive_name(self):
    """Brief description of what this test verifies."""
    # Arrange: Set up test data
    input_data = "test input"
    
    # Act: Call the function under test
    result = parse_input(input_data)
    
    # Assert: Verify the expected outcome
    self.assertEqual(result, expected_result)
```

## Test Categories to Consider

For any function, consider testing:

1. **Happy Path**: Normal, expected usage
2. **Edge Cases**: Boundary conditions, empty inputs, very large inputs
3. **Error Cases**: Invalid inputs that should raise exceptions
4. **Performance**: Very large or complex inputs
5. **Integration**: How the function works with other parts of the system
