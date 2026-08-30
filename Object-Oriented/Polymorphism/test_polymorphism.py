"""Unit Test Suite for Polymorphism Module.

This module provides unittest coverage for polymorphic method invocation across Animal subclasses.
"""

import unittest
from polymorphic_animals import Animal, Dog, Cat, express_all_affections


class TestPolymorphism(unittest.TestCase):
    """Unit tests for polymorphic behavior."""

    def test_polymorphic_affections(self) -> None:
        """Verify show_affection() produces distinct results for Dog vs Cat."""
        dog = Dog("Raffi")
        cat = Cat("Smikey")
        self.assertEqual(dog.show_affection(), "Raffi wags tail.")
        self.assertEqual(cat.show_affection(), "Smikey purrs.")

        messages = express_all_affections([dog, cat])
        self.assertEqual(messages, ["Raffi wags tail.", "Smikey purrs."])


if __name__ == "__main__":
    unittest.main()
