"""Unit Test Suite for Static-Class-Methods-Decorator Module.

This module provides unittest coverage for instance methods, @classmethod counters,
and @staticmethod utility validators.
"""

import unittest
from method_decorators import InstanceCounter


class TestStaticClassMethods(unittest.TestCase):
    """Unit tests for method decorators."""

    def test_method_decorators(self) -> None:
        """Verify instance method, classmethod counter, and staticmethod filtering."""
        initial_count = InstanceCounter.get_count()
        obj1 = InstanceCounter(50)
        obj2 = InstanceCounter("not_int")

        self.assertEqual(obj1.get_val(), 50)
        self.assertEqual(obj2.get_val(), 0)  # Filtered to 0 by @staticmethod

        self.assertEqual(InstanceCounter.get_count(), initial_count + 2)


if __name__ == "__main__":
    unittest.main()
