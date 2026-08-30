"""Unit Test Suite for Inheritance Module.

This module provides unittest coverage for single inheritance, method overriding,
super(), type checks, team management, and datetime extensions.
"""

import unittest
from animal_hierarchy import Animal, Cat, Pigeon
from company_hierarchy import CompanyEmployee, Staff, Manager
from date_time_extension import CustomDate


class TestInheritance(unittest.TestCase):
    """Unit tests for inheritance modules."""

    def test_animal_hierarchy(self) -> None:
        """Verify Animal, Cat, and Pigeon inheritance and method overriding."""
        cat = Cat()
        pigeon = Pigeon()
        self.assertFalse(cat.can_fly())
        self.assertTrue(pigeon.can_fly())
        self.assertTrue(isinstance(cat, Animal))
        self.assertTrue(issubclass(Cat, Animal))

    def test_company_hierarchy(self) -> None:
        """Verify CompanyEmployee, Staff, and Manager inheritance and team operations."""
        stf = Staff("Joe", "Philips", 7000.0, "Java")
        mgr = Manager("Georgina", "Holland", 12000.0)

        self.assertEqual(stf.primary_skill, "Java")
        stf.apply_pay_raise()
        self.assertEqual(stf.salary, 7490.0)

        mgr.add_employee(stf)
        self.assertEqual(mgr.get_team_names(), ["Joe Philips"])
        mgr.remove_employee(stf)
        self.assertEqual(mgr.get_team_names(), [])

    def test_custom_date_extension(self) -> None:
        """Verify CustomDate get_tomorrow() calculation."""
        date_obj = CustomDate(2026, 8, 30)
        tomorrow = date_obj.get_tomorrow()
        self.assertEqual(tomorrow.day, 31)
        self.assertEqual(tomorrow.month, 8)


if __name__ == "__main__":
    unittest.main()
