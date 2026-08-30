"""Unit Test Suite for Encapsulation Module.

This module provides unittest coverage for book encapsulation, property setters/getters,
and integer type validation.
"""

import unittest
from book_instance import Book
from house_price_encapsulation import House
from validated_integer import ValidatedInteger


class TestEncapsulation(unittest.TestCase):
    """Unit tests for encapsulation features."""

    def test_book_instance(self) -> None:
        """Verify Book initialization and summary string."""
        b = Book("Data Science", 20.0, "Martin Schulter")
        self.assertIn("Data Science", b.get_summary())

    def test_house_price_encapsulation(self) -> None:
        """Verify House property getter and setter validation."""
        h = House(100000)
        self.assertEqual(h.price, 100000.0)
        h.price = 150000.0
        self.assertEqual(h.price, 150000.0)
        with self.assertRaises(ValueError):
            h.price = -500.0

    def test_validated_integer(self) -> None:
        """Verify ValidatedInteger safe parsing and increment."""
        v = ValidatedInteger(10)
        self.assertEqual(v.get_number(), 10)
        self.assertFalse(v.set_number("invalid"))
        self.assertEqual(v.get_number(), 10)
        v.increment(5)
        self.assertEqual(v.get_number(), 15)


if __name__ == "__main__":
    unittest.main()
