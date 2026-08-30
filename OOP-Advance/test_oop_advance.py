"""Master Unit Test Suite for OOP-Advance Root Modules.

This module provides comprehensive unittest coverage for class initialization,
class method factories, static utility methods, property getters/setters,
dynamic attributes, and range evolution.
"""

import datetime
import unittest

from class_definition_init import User
from class_method_factory import Staff
from class_attributes_no_init import DynamicUser
from encapsulation_attributes import Monitor
from utility_static_method import Staff as UtilityStaff
from classic_vs_new_style_class import ClassicStyle, ExplicitNewStyle
from staff_management import Staff as ManagementStaff
from range_version_evolution import inspect_range_attributes, demonstrate_range_features, compare_range_memory_efficiency


class TestOOPAdvanceRoot(unittest.TestCase):
    """Unit tests for root level OOP-Advance modules."""

    def test_user_initialization(self) -> None:
        """Verify User class constructor and email calculation."""
        u = User("John", "Doe", 3300.0)
        self.assertEqual(u.full_name(), "John Doe")
        self.assertEqual(u.email, "john.doe@mail.com")
        self.assertEqual(u.payment, 3300.0)

    def test_class_method_factory(self) -> None:
        """Verify Staff class method factory and class attribute update."""
        initial_rate = Staff.increase_pay_rate
        Staff.set_increase_pay(1.09)
        self.assertEqual(Staff.increase_pay_rate, 1.09)

        staff = Staff.from_string("George-Bill-2750")
        self.assertEqual(staff.full_name(), "George Bill")
        self.assertEqual(staff.salary, 2750.0)
        Staff.set_increase_pay(initial_rate)

    def test_dynamic_user_attributes(self) -> None:
        """Verify dynamic attribute assignment without init."""
        user = DynamicUser()
        user.first_name = "Alex"
        user.last_name = "Morgan"
        self.assertEqual(user.first_name, "Alex")
        self.assertEqual(user.last_name, "Morgan")

    def test_encapsulation_and_property(self) -> None:
        """Verify protected, private mangled, and @property encapsulation."""
        mon = Monitor(18)
        self.assertEqual(mon._attribute_val, 18)
        self.assertEqual(mon.value, 18)

        mon.value = 301
        self.assertEqual(mon.value, 301)

        del mon.value
        self.assertEqual(mon.value, 0)
        self.assertEqual(mon._Monitor__mangled_name, "Private Class Data")

    def test_static_utility_method(self) -> None:
        """Verify static method date checking."""
        monday = datetime.date(2023, 5, 15)
        sunday = datetime.date(2023, 5, 14)
        self.assertTrue(UtilityStaff.is_workday(monday))
        self.assertFalse(UtilityStaff.is_workday(sunday))

    def test_classic_vs_new_style_class(self) -> None:
        """Verify object superclass inheritance."""
        c = ClassicStyle()
        n = ExplicitNewStyle()
        self.assertTrue(isinstance(c, object))
        self.assertTrue(isinstance(n, object))

    def test_staff_management(self) -> None:
        """Verify staff instance counter and payment increase."""
        count_before = ManagementStaff.number_of_staff
        s = ManagementStaff("Tom", "George", 2800.0)
        self.assertEqual(ManagementStaff.number_of_staff, count_before + 1)
        s.increase_payment()
        self.assertEqual(s.payment, 3080.0)

    def test_range_evolution(self) -> None:
        """Verify range attributes and memory efficiency functions."""
        attrs = inspect_range_attributes()
        self.assertIn("start", attrs)
        self.assertIn("stop", attrs)
        self.assertIn("step", attrs)

        start, stop, step, contains_50 = demonstrate_range_features()
        self.assertEqual(start, 10)
        self.assertEqual(stop, 100)
        self.assertEqual(step, 5)
        self.assertTrue(contains_50)

        range_bytes, list_bytes = compare_range_memory_efficiency(100)
        self.assertLess(range_bytes, list_bytes)


if __name__ == "__main__":
    unittest.main()
