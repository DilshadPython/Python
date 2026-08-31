"""
Unit tests for example.py and print definitions using Python's unittest framework.
How to run tests:
    python3 -m unittest discover -s 1.Print
    or
    python3 1.Print/test_example.py
"""

import os
import sys
import unittest
import io

# Ensure current directory is accessible on Python module search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import example
import python_version
import print_definition


class TestExample(unittest.TestCase):
    """
    Test suite for string formatting, manipulation routines, and print definitions.
    """

    def test_name_type(self):
        # Notice: self.assertIsInstance is the standard unittest method
        # for verifying that a variable is of the expected type (str).
        self.assertIsInstance(example.name, str)

    def test_format_name_demo(self):
        # Test method chaining result: strip() + title()
        result = example.format_name_demo("   alice wonderland   ")
        self.assertEqual(result, "Alice Wonderland")

    def test_string_transformations(self):
        sample = "   hello world   "
        self.assertEqual(sample.strip(), "hello world")
        self.assertEqual(sample.strip().capitalize(), "Hello world")
        self.assertEqual(sample.strip().title(), "Hello World")

    def test_print_version_groups(self):
        # Verify all 3 version groups are defined
        defs = python_version.PRINT_VERSION_DEFINITIONS
        self.assertIn("Python 2.7", defs)
        self.assertIn("Python 3.0 - 3.2", defs)
        self.assertIn("Python 3.3 - 3.13", defs)
        self.assertIn("flush=False", defs["Python 3.3 - 3.13"]["signature"])

    def test_print_definition_run(self):
        # Capture stdout when running print demos
        captured = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured
            print_definition.run_all_version_demos()
        finally:
            sys.stdout = old_stdout
        output = captured.getvalue()
        self.assertIn("Group 1: Python 2.7", output)
        self.assertIn("Group 2: Python 3.0 - 3.2", output)
        self.assertIn("Group 3: Python 3.3 - 3.13", output)


if __name__ == "__main__":
    unittest.main()
