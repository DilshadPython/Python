"""Unit Test Suite for Inheritance-built-in Sub-directory Modules.

This module provides unittest coverage for vector arithmetic overloading, dictionary subclassing,
one-based indexing lists, and container operators.
"""

import unittest
from vector_arithmetic_overloading import SumList
from dictionary_subclassing import People
from one_based_list import MyList


class TestInheritanceBuiltin(unittest.TestCase):
    """Unit tests for built-in inheritance modules."""

    def test_sum_list_arithmetic(self) -> None:
        """Verify SumList pairwise addition and subtraction."""
        l1 = SumList([10, 20, 30])
        l2 = SumList([1, 2, 3])

        added = l1 + l2
        subtracted = l1 - l2

        self.assertEqual(str(added), "[11, 22, 33]")
        self.assertEqual(str(subtracted), "[9, 18, 27]")

    def test_people_dict_subclass(self) -> None:
        """Verify People dictionary subclassing."""
        p = People()
        p["key"] = "val"
        self.assertEqual(p["key"], "val")
        self.assertTrue(isinstance(p, dict))

    def test_one_based_list(self) -> None:
        """Verify MyList 1-based index access and error handling."""
        m = MyList(["a", "b", "c"])
        self.assertEqual(m[1], "a")
        self.assertEqual(m[3], "c")

        m[1] = "z"
        self.assertEqual(m[1], "z")

        with self.assertRaises(IndexError):
            _ = m[0]


if __name__ == "__main__":
    unittest.main()
