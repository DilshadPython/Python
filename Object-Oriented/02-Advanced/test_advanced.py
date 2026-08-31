"""
Unit test suite verifying Advanced Object-Oriented Programming (02-Advanced).
"""
# "import module" loads datetime and unittest from standard library framework.
import datetime
import math
import unittest

# "from module import name" imports advanced OOP classes into test scope.
from abstract_base_classes import Circle, Rectangle, Shape
from builtin_subclassing import LoggingDict, OneBasedList
from class_methods_factory import Staff
from magic_dunder_methods import Vector2D
from property_encapsulation import Monitor
from range_version_evolution import compare_range_memory_efficiency, demonstrate_range_features, inspect_range_attributes
from static_utility_methods import WorkCalendar


class TestOOPAdvanced(unittest.TestCase):
    """Test suite covering class methods, static methods, properties, ABCs, dunder methods, and range evolution."""

    def test_class_method_factory(self):
        """Verify Staff class method factory and salary raise rate modification."""
        initial_rate = Staff.increase_pay_rate
        Staff.set_increase_pay(1.10)
        self.assertEqual(Staff.increase_pay_rate, 1.10)

        s = Staff.from_string("George-Bill-3000")
        self.assertEqual(s.full_name(), "George Bill")
        self.assertEqual(s.salary, 3000.0)

        Staff.set_increase_pay(initial_rate)

    def test_static_utility_methods(self):
        """Verify WorkCalendar static date utility methods."""
        monday = datetime.date(2023, 5, 15)
        sunday = datetime.date(2023, 5, 14)
        self.assertTrue(WorkCalendar.is_workday(monday))
        self.assertFalse(WorkCalendar.is_workday(sunday))

        workdays = WorkCalendar.calculate_workdays_between(
            datetime.date(2023, 5, 15), datetime.date(2023, 5, 19)
        )
        self.assertEqual(workdays, 5)

    def test_property_encapsulation(self):
        """Verify Monitor @property accessors and deletion logic."""
        m = Monitor(50)
        self.assertEqual(m.value, 50)
        self.assertEqual(m.private_data, "Private Class Data")

        m.value = 100
        self.assertEqual(m.value, 100)

        with self.assertRaises(ValueError):
            m.value = -10

        del m.value
        self.assertEqual(m.value, 0)

    def test_abstract_base_classes(self):
        """Verify Shape abstract base class and derived Circle/Rectangle calculations."""
        # Instantiating Shape directly should raise TypeError
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

