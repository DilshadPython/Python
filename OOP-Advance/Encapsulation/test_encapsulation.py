"""Unit Test Suite for Encapsulation Sub-directory Modules.

This module provides unittest coverage for explicit getters/setters and property accessors.
"""

import unittest
from getter_setter_methods import Monitor as MethodMonitor
from property_encapsulation import Monitor as PropertyMonitor


class TestEncapsulation(unittest.TestCase):
    """Unit tests for encapsulation modules."""

    def test_explicit_getter_setter(self) -> None:
        """Verify explicit set_val and get_val methods."""
        m = MethodMonitor()
        m.set_val(42)
        self.assertEqual(m.get_val(), 42)

    def test_property_accessor_and_deleter(self) -> None:
        """Verify @property getter, setter, and deleter behavior."""
        m = PropertyMonitor(100)
        self.assertEqual(m.var, 100)

        m.var = 250
        self.assertEqual(m.var, 250)

        del m.var
        self.assertEqual(m.var, 0)


if __name__ == "__main__":
    unittest.main()
