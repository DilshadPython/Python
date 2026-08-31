"""
Unit test suite verifying Object-Oriented Design Patterns (03-Design-Patterns).
"""
# "import module" loads math and unittest from standard library framework.
import math
import unittest

# "from module import name" imports design pattern classes into test scope.
from abstract_base_classes import Circle, Rectangle, Shape
from builtin_subclassing import LoggingDict, OneBasedList
from magic_dunder_methods import Vector2D
from range_version_evolution import compare_range_memory_efficiency, demonstrate_range_features, inspect_range_attributes


class TestOOPDesignPatterns(unittest.TestCase):
    """Test suite covering ABC interface contracts, dunder methods, built-in subclassing, and range evolution."""

    def test_abstract_base_classes(self):
        """Verify Shape abstract base class and derived Circle/Rectangle calculations."""
        with self.assertRaises(TypeError):
            Shape()

        c = Circle(5.0)
        self.assertAlmostEqual(c.area(), math.pi * 25.0, places=5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 5.0, places=5)

        r = Rectangle(4.0, 6.0)
        self.assertEqual(r.area(), 24.0)
        self.assertEqual(r.perimeter(), 20.0)

    def test_builtin_subclassing(self):
        """Verify LoggingDict and OneBasedList behavior."""
        d = LoggingDict()
        d["key"] = "value"
        self.assertEqual(d["key"], "value")

        lst = OneBasedList(["a", "b", "c"])
        self.assertEqual(lst[1], "a")
        self.assertEqual(lst[2], "b")
        self.assertEqual(lst[3], "c")

        with self.assertRaises(IndexError):
            _ = lst[0]

    def test_magic_dunder_vector_operations(self):
        """Verify Vector2D dunder operators for addition, equality, and representation."""
        v1 = Vector2D(2, 3)
        v2 = Vector2D(4, 5)
        v3 = v1 + v2

        self.assertEqual(v3, Vector2D(6, 8))
        self.assertEqual(repr(v1), "Vector2D(x=2, y=3)")
        self.assertEqual(str(v1), "(2, 3)")
        self.assertEqual(len(v1), 2)

    def test_range_version_evolution(self):
        """Verify range attributes, containment testing, and O(1) memory efficiency."""
        attrs = inspect_range_attributes()
        self.assertIn("start", attrs)
        self.assertIn("stop", attrs)
        self.assertIn("step", attrs)

        start, stop, step, contains_50 = demonstrate_range_features()
        self.assertEqual(start, 10)
        self.assertEqual(stop, 100)
        self.assertEqual(step, 5)
        self.assertTrue(contains_50)

        range_bytes, list_bytes = compare_range_memory_efficiency()
        self.assertLess(range_bytes, list_bytes)


if __name__ == "__main__":
    unittest.main()
