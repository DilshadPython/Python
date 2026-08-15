"""
Unit tests for example.py using Python's unittest framework.
How to run tests:
    python3 -m unittest discover -s 1.Print
    or
    python3 1.Print/test_example.py
"""

import os
import sys
import unittest

# Ensure current directory is accessible on Python module search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import example


class TestExample(unittest.TestCase):
    """
    Test suite for string formatting and manipulation routines.
    """

    def test_name_type(self):
        # Notice: self.assertIsInstance is the standard unittest method
        # for verifying that a variable is of the expected type (str).
        self.assertIsInstance(example.name, str)

        # [Legacy Assert Demonstration]
        # assert isinstance(example.name, str)

    def test_format_name_demo(self):
        # Test method chaining result: strip() + title()
        result = example.format_name_demo("   alice wonderland   ")
        self.assertEqual(result, "Alice Wonderland")

    def test_string_transformations(self):
        sample = "   hello world   "
        self.assertEqual(sample.strip(), "hello world")
        self.assertEqual(sample.strip().capitalize(), "Hello world")
        self.assertEqual(sample.strip().title(), "Hello World")


if __name__ == "__main__":
    unittest.main()
