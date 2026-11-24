"""
Unit Test Suite for Python Unpacking Operators (*, **, _) across Developer Tiers (Beginner, Intermediate, Senior).

This module verifies:
1. Positional sequence unpacking (`sequence_unpacking.py`).
2. Dictionary keyword unpacking (`dictionary_unpacking.py`).
3. Beginner level tuple assignment and wildcard discard (`beginner_unpacking.py`).
4. Intermediate level extended unpacking and varargs (`intermediate_unpacking.py`).
5. Senior level structural pattern matching, TypedDict Unpack, and AST parsing (`senior_unpacking.py`).
"""

import sys
from pathlib import Path
import unittest

# Support both package and local directory import paths
root = Path(__file__).parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from sequence_unpacking import calculate_volume_inches, unpack_sequence_dimensions
from dictionary_unpacking import unpack_dictionary_dimensions, merge_dictionaries
from beginner_unpacking import demonstrate_tuple_assignment, demonstrate_wildcard_discard, demonstrate_basic_list_unpacking
from intermediate_unpacking import demonstrate_extended_iterable_unpacking, demonstrate_varargs_kwargs_delegation, demonstrate_dictionary_merge_unpacking
from senior_unpacking import demonstrate_pattern_matching_unpacking, calculate_volume_typed_unpack, inspect_unpacking_ast


class TestPythonUnpacking(unittest.TestCase):
    """Test suite verifying unpacking operators across all modules."""

    def test_sequence_unpacking(self) -> None:
        """Verify positional sequence unpacking calculate_volume_inches."""
        dims = [75.0, 40.0, 25.0]
        vol = unpack_sequence_dimensions(dims)
        self.assertAlmostEqual(vol, 4576.7775, places=4)

        with self.assertRaises(ValueError):
            unpack_sequence_dimensions([10.0, 20.0])

    def test_dictionary_unpacking(self) -> None:
        """Verify dictionary keyword unpacking and dictionary merging."""
        dims_dict = {"length": 15.0, "width": 10.0, "height": 8.0}
        vol = unpack_dictionary_dimensions(dims_dict)
        self.assertAlmostEqual(vol, 73.2284, places=4)

        merged = merge_dictionaries({"a": 1}, {"b": 2})
        self.assertEqual(merged, {"a": 1, "b": 2})

    def test_beginner_unpacking(self) -> None:
        """Verify beginner tuple assignment, wildcard discard, and list unpacking."""
        fname, lname = demonstrate_tuple_assignment("Dilshad Abdulla")
        self.assertEqual(fname, "Dilshad")
        self.assertEqual(lname, "Abdulla")

        fname_only = demonstrate_wildcard_discard("Dilshad Abdulla")
        self.assertEqual(fname_only, "Dilshad")

        a, b, c = demonstrate_basic_list_unpacking([10, 20, 30])
        self.assertEqual((a, b, c), (10, 20, 30))

    def test_intermediate_unpacking(self) -> None:
        """Verify intermediate extended iterable unpacking and varargs."""
        head, mid, tail = demonstrate_extended_iterable_unpacking([1, 2, 3, 4, 5])
        self.assertEqual(head, 1)
        self.assertEqual(mid, [2, 3, 4])
        self.assertEqual(tail, 5)

        captured = demonstrate_varargs_kwargs_delegation(10, "test", key="val")
        self.assertEqual(captured["positional_count"], 2)
        self.assertEqual(captured["keyword_kwargs"], {"key": "val"})

        merged = demonstrate_dictionary_merge_unpacking({"a": 1}, {"a": 99, "b": 2})
        self.assertEqual(merged["a"], 99)

    def test_senior_unpacking(self) -> None:
        """Verify senior pattern matching, TypedDict Unpack, and AST parsing."""
        res = demonstrate_pattern_matching_unpacking([10, 20, 30, 40])
        self.assertIn("Matched List Pattern", res)

        vol = calculate_volume_typed_unpack(length=15.0, width=10.0, height=8.0)
        self.assertAlmostEqual(vol, 73.2284, places=4)

        targets = inspect_unpacking_ast("a, *b, c = seq")
        self.assertEqual(targets, ["a", "*b", "c"])


if __name__ == "__main__":
    unittest.main()
