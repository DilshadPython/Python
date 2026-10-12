"""
Unit Test Suite for __name__ Fundamentals Module.

Tests execution context retrieval, string formatting, square sequence generation,
and main entry point function execution.
"""

from pathlib import Path
import sys
import unittest

# Ensure current directory is in Python path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from main_entry_point_idiom import calculate_square_sequence, main
from name_attribute_basics import format_greeting, get_execution_context


class TestNameMainFundamentals(unittest.TestCase):
    """Test cases for __name__ attribute basics and main entry points."""

    def test_get_execution_context(self) -> None:
        """Verify execution context dictionary format."""
        context = get_execution_context()
        self.assertIn("module_name", context)
        self.assertIn("execution_mode", context)
        self.assertIn("python_version", context)

    def test_format_greeting(self) -> None:
        """Verify greeting string generation."""
        greeting = format_greeting("Alice")
        self.assertIn("Alice", greeting)
        self.assertIn("Executing module", greeting)

    def test_calculate_square_sequence(self) -> None:
        """Verify square sequence math calculation."""
        squares = calculate_square_sequence(5)
        self.assertListEqual(squares, [0, 1, 4, 9, 16])

    def test_main_function_return(self) -> None:
        """Verify main entry point returns status code 0."""
        code = main()
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
