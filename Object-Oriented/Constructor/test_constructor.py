"""Unit Test Suite for Constructor Module.

This module provides unittest coverage for class constructors, argument passing,
and defensive type validation inside `__init__`.
"""

import unittest
from animal_sounds import Animal
from number_counter import NumberCounter


class TestConstructor(unittest.TestCase):
    """Unit tests verifying constructor initialization and defensive parsing."""

    def test_animal_sounds(self) -> None:
        """Verify Animal __init__ initialization and make_sound()."""
        dog = Animal("Dog", "barking")
        self.assertIn("barking", dog.make_sound())

    def test_number_counter_defaults_and_validation(self) -> None:
        """Verify NumberCounter default constructor, initial value passing, and fallback."""
        c1 = NumberCounter()
        self.assertEqual(c1.get_value(), 0)

        c2 = NumberCounter(5)
        c2.increment(3)
        self.assertEqual(c2.get_value(), 8)

        c3 = NumberCounter("invalid_str")
        self.assertEqual(c3.get_value(), 0)


if __name__ == "__main__":
    unittest.main()
