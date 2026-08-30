"""Unit Test Suite for Magic-Method Module.

This module provides unittest coverage for built-in and custom object magic dunder methods.
"""

import unittest
from builtin_dunder_emulation import demonstrate_builtin_dunders
from account_dunder_methods import CustomAccount


class TestMagicMethod(unittest.TestCase):
    """Unit tests for magic dunder methods."""

    def test_builtin_dunders(self) -> None:
        """Verify built-in dunder operation dictionary."""
        res = demonstrate_builtin_dunders()
        self.assertEqual(res["int_add"], 50)
        self.assertEqual(res["str_add"], "AB")
        self.assertEqual(res["str_len"], 11)

    def test_custom_account_dunders(self) -> None:
        """Verify CustomAccount __repr__, __str__, __add__, __len__, and __eq__."""
        acc1 = CustomAccount("Math", "George", 60500.0)
        acc2 = CustomAccount("Tom", "Alan", 82500.0)
        acc3 = CustomAccount("Math", "George", 60500.0)

        self.assertIn("CustomAccount('Math'", repr(acc1))
        self.assertIn("Math George", str(acc1))
        self.assertEqual(acc1 + acc2, 143000.0)
        self.assertEqual(len(acc1), 11)  # "Math George" has 11 chars
        self.assertEqual(acc1, acc3)
        self.assertNotEqual(acc1, acc2)


if __name__ == "__main__":
    unittest.main()
