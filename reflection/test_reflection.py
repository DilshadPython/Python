"""
Unit Test Suite for Reflection & Introspection Operations across Developer Tiers (Beginner, Intermediate, Senior).

This module verifies:
1. Core `reflection.py` function logic.
2. Modular `ReflectionEngine` class operations (`sequence_reflection.py`).
3. Beginner level sequence reversal methods (`beginner_reflection.py`).
4. Intermediate object introspection and dynamic attribute reflection (`intermediate_reflection.py`).
5. Senior subclass reflection, dynamic `type()` class creation, and function wrapping (`senior_reflection.py`).
"""

from pathlib import Path
import sys
import unittest

# Support both package and local directory import paths
root = Path(__file__).parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from reflection import reflect
from sequence_reflection import ReflectionEngine
from beginner_reflection import reflect_recursive, reflect_via_slicing, reflect_via_reversed
from intermediate_reflection import StudentProfile, introspect_object_details, dynamically_update_attribute
from senior_reflection import BasePlugin, DataPlugin, discover_subclasses, create_dynamic_class


class TestReflection(unittest.TestCase):
    """Test suite verifying reflection operations across all modules and developer tiers."""

    def test_legacy_reflect(self) -> None:
        """Verify legacy reflect function on lists and strings."""
        self.assertEqual(reflect([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reflect("hello"), "olleh")
        self.assertEqual(reflect([]), [])

    def test_reflection_engine(self) -> None:
        """Verify ReflectionEngine sequence reversal, attribute inspection, and dynamic invocation."""
        self.assertEqual(ReflectionEngine.reflect_sequence([10, 20]), [20, 10])

        class Dummy:
            def __init__(self) -> None:
                self.x = 100

            def greet(self, name: str) -> str:
                return f"Hello {name}"

        d = Dummy()
        attrs = ReflectionEngine.inspect_object(d)
        self.assertIn("x", attrs)
        self.assertIn("greet", attrs)

        res = ReflectionEngine.invoke_dynamically(d, "greet", "Monika")
        self.assertEqual(res, "Hello Monika")

    def test_beginner_reflection(self) -> None:
        """Verify beginner recursive, slicing, and reversed sequence reversal."""
        data = [1, 2, 3, 4]
        self.assertEqual(reflect_recursive(data), [4, 3, 2, 1])
        self.assertEqual(reflect_via_slicing(data), [4, 3, 2, 1])
        self.assertEqual(reflect_via_reversed(data), [4, 3, 2, 1])

    def test_intermediate_reflection(self) -> None:
        """Verify intermediate object introspection and dynamic attribute updates."""
        student = StudentProfile("Alice", 20, ["Math"])
        details = introspect_object_details(student)

        self.assertEqual(details["class_name"], "StudentProfile")
        self.assertIn("name", details["attributes"])
        self.assertIn("get_summary", details["methods"])

        existed = dynamically_update_attribute(student, "age", 21)
        self.assertTrue(existed)
        self.assertEqual(student.age, 21)

    def test_senior_reflection(self) -> None:
        """Verify senior subclass reflection and dynamic class creation."""
        subclasses = discover_subclasses(BasePlugin)
        self.assertIn(DataPlugin, subclasses)

        DynamicCls = create_dynamic_class("TestCls", (object,), {"val": 42})
        inst = DynamicCls()
        self.assertEqual(inst.val, 42)


if __name__ == "__main__":
    unittest.main()
