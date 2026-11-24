"""
Unit Test Suite for Built-in Functions Fundamentals Module.

Tests abs() magnitude computation, truthiness evaluation with all() and any(),
collection stats using len()/sum()/min()/max(), and builtins reflection.
"""

import unittest
from builtin_functions_basics import (
    calculate_absolute_values,
    compute_collection_summary,
    evaluate_truthiness_conditions,
    get_lowercase_builtin_docstrings,
)


class TestBuiltinFundamentals(unittest.TestCase):
    """Test cases for core built-in functions."""

    def test_calculate_absolute_values(self) -> None:
        """Verify abs() magnitude for negative ints, floats, and complex numbers."""
        results = calculate_absolute_values([-8, -3.76, 3 - 4j])
        self.assertEqual(results[0], 8.0)
        self.assertEqual(results[1], 3.76)
        self.assertEqual(results[2], 5.0)  # sqrt(3^2 + 4^2) = 5.0

    def test_evaluate_truthiness_conditions(self) -> None:
        """Verify truthiness evaluation using built-in all() and any()."""
        all_pass = evaluate_truthiness_conditions([True, 1, "hello"])
        self.assertTrue(all_pass["all_true"])
        self.assertTrue(all_pass["any_true"])

        mixed = evaluate_truthiness_conditions([False, 0, "world"])
        self.assertFalse(mixed["all_true"])
        self.assertTrue(mixed["any_true"])

        all_fail = evaluate_truthiness_conditions([0, "", False, None])
        self.assertFalse(all_fail["all_true"])
        self.assertFalse(all_fail["any_true"])

    def test_compute_collection_summary(self) -> None:
        """Verify stats summary calculation with len(), sum(), min(), max()."""
        stats = compute_collection_summary([10, 20, 30, 40])
        self.assertEqual(stats["count"], 4.0)
        self.assertEqual(stats["total"], 100.0)
        self.assertEqual(stats["min"], 10.0)
        self.assertEqual(stats["max"], 40.0)
        self.assertEqual(stats["average"], 25.0)

    def test_compute_collection_summary_empty(self) -> None:
        """Verify ValueError is raised when summarizing empty collection."""
        with self.assertRaises(ValueError):
            compute_collection_summary([])

    def test_get_lowercase_builtin_docstrings(self) -> None:
        """Verify extraction of built-in function docstrings from builtins module."""
        docstrings = get_lowercase_builtin_docstrings()
        self.assertIn("abs", docstrings)
        self.assertIn("len", docstrings)
        self.assertIn("sum", docstrings)


if __name__ == "__main__":
    unittest.main()
