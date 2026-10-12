"""
Unit test suite verifying Advanced Object-Oriented Programming (02-Advanced).
"""
# "import module" loads datetime and unittest from standard library framework.
import datetime
import unittest

# "from module import name" imports advanced method classes into test scope.
from class_methods_factory import Staff
from property_encapsulation import Monitor
from static_utility_methods import WorkCalendar


class TestOOPAdvanced(unittest.TestCase):
    """Test suite covering class methods, static methods, and property encapsulation."""

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


if __name__ == "__main__":
    unittest.main()
