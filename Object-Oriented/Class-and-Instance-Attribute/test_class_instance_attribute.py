"""Unit Test Suite for Class and Instance Attribute Module.

This module provides unittest coverage for class attribute lookups, instance shadowing,
and attribute deletion fallbacks.
"""

import unittest
from class_vs_instance_attributes import VehicleInventory
from attribute_encapsulation_and_deletion import LanguageEnvironment


class TestClassAndInstanceAttribute(unittest.TestCase):
    """Unit tests verifying class attribute defaults, instance shadowing, and deletion."""

    def test_vehicle_inventory(self) -> None:
        """Verify initial class attribute fallback and subsequent instance shadowing."""
        inv = VehicleInventory("Sedan")
        self.assertEqual(inv.stock_count, 0)
        
        inv.configure_inventory(25000.0, 5)
        self.assertEqual(inv.price, 25000.0)
        self.assertEqual(inv.stock_count, 5)
        self.assertEqual(VehicleInventory.stock_count, 0)

    def test_attribute_deletion_fallback(self) -> None:
        """Verify deleting instance attribute restores class attribute lookup."""
        env = LanguageEnvironment()
        self.assertEqual(env.language_name, "Python")

        env.language_name = "JavaScript"
        self.assertEqual(env.language_name, "JavaScript")
        self.assertEqual(LanguageEnvironment.language_name, "Python")

        del env.language_name
        self.assertEqual(env.language_name, "Python")


if __name__ == "__main__":
    unittest.main()
