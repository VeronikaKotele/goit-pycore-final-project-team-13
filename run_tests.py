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
    
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParseInput)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with proper code
    sys.exit(0 if result.wasSuccessful() else 1)