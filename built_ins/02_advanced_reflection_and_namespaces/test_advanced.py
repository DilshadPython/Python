"""
Unit Test Suite for Advanced Reflection and Namespaces Module.

Tests type introspection with dir(), namespace dictionary summaries, Newton's method square root,
and DynamicAttributeContainer getattr/hasattr behavior.
"""

import unittest
from advanced_reflection_and_namespaces import (
    DynamicAttributeContainer,
    get_current_namespace_summary,
    inspect_type_methods,
    newton_square_root,
)


class TestAdvancedReflection(unittest.TestCase):
    """Test cases for reflection, introspection, and Newton's method."""

    def test_inspect_type_methods(self) -> None:
        """Verify dir() public method extraction for dict and str types."""
        dict_methods = inspect_type_methods(dict)
        self.assertIn("keys", dict_methods)
        self.assertIn("values", dict_methods)
        self.assertIn("items", dict_methods)
        self.assertFalse(any(m.startswith("__") for m in dict_methods))

        str_methods = inspect_type_methods(str)
        self.assertIn("upper", str_methods)
        self.assertIn("split", str_methods)
        self.assertIn("strip", str_methods)

    def test_get_current_namespace_summary(self) -> None:
        """Verify namespace dictionary summary output."""
        sample_scope = {"alpha": 100, "beta": "text", "gamma": [1, 2, 3], "__dunder": 42}
        summary = get_current_namespace_summary(sample_scope)

        self.assertEqual(summary.get("alpha"), "int")
        self.assertEqual(summary.get("beta"), "str")
        self.assertEqual(summary.get("gamma"), "list")
        self.assertNotIn("__dunder", summary)

    def test_newton_square_root_valid(self) -> None:
        """Verify Newton's method square root accuracy against math.sqrt."""
        self.assertEqual(newton_square_root(0.0), 0.0)
        self.assertAlmostEqual(newton_square_root(25.0), 5.0, places=4)
        self.assertAlmostEqual(newton_square_root(2.0), 1.41421356, places=4)

    def test_newton_square_root_negative(self) -> None:
        """Verify ValueError is raised when passing negative number to newton_square_root."""
        with self.assertRaises(ValueError):
            newton_square_root(-9.0)

    def test_dynamic_attribute_container(self) -> None:
        """Verify dynamic attribute creation, hasattr check, and safe_get retrieval."""
        container = DynamicAttributeContainer(name="Python", version=3.13)
        self.assertEqual(container.safe_get("name"), "Python")
        self.assertEqual(container.safe_get("version"), 3.13)
        self.assertIsNone(container.safe_get("nonexistent"))
        self.assertEqual(container.safe_get("nonexistent", default="fallback"), "fallback")


if __name__ == "__main__":
    unittest.main()
