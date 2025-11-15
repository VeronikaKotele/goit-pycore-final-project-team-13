"""
Test configuration for pytest.
This file is automatically discovered by pytest and runs before any tests.
"""
import sys
import os

# Add the src directory to Python path so we can import our modules
project_root = os.path.dirname(__file__)
src_path = os.path.join(project_root, '..', 'src')
sys.path.insert(0, os.path.abspath(src_path))

print(f"Added to Python path: {os.path.abspath(src_path)}")