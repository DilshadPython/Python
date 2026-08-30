"""Unit Test Suite for Example-Test Module.

This module provides unittest coverage for MaxSizeList bounded size enforcement and item eviction.
"""

import unittest
from max_size_list import MaxSizeList


class TestExampleTest(unittest.TestCase):
    """Unit tests verifying MaxSizeList behavior."""

    def test_max_size_eviction(self) -> None:
        """Verify MaxSizeList caps elements to max capacity and evicts oldest items."""
        lst = MaxSizeList(2)
        lst.push("A")
        lst.push("B")
        self.assertEqual(lst.get_list(), ["A", "B"])

        # Pushing third element evicts "A"
        lst.push("C")
        self.assertEqual(lst.get_list(), ["B", "C"])


if __name__ == "__main__":
    unittest.main()
