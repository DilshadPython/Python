"""Unit Test Suite for the Object-Oriented Programming (OOP) Tutorial Module.

This module provides comprehensive unittest coverage for all OOP components:
class definition basics, class vs instance attributes, instance/class/static methods,
property getters/setters/deleters, class inheritance, method resolution order (MRO),
magic dunder methods, operator overloading, and procedural vs OOP comparisons.
"""

# import standard unittest module for assertions and test runner
import datetime
import unittest

# import classes and functions from target modules
from class_definition_basics import Employee, Car, inspect_object_attributes
from class_and_instance_attributes import EmployeeAccount
from instance_class_static_methods import EmployeeService
from property_getters_setters import EmployeeProfile
from class_inheritance_and_mro import Employee as BaseEmployee, Developer, Manager
from magic_dunder_methods import EmployeeRecord, ListNumber
from ice_cream_machine import IceCreamMachine
from procedural_vs_oop import run_procedural_example, CustomerCounter, compare_paradigms


class TestClassDefinitionBasics(unittest.TestCase):
    """Unit tests for basic class creation and attribute inspection."""

    def test_employee_instantiation(self) -> None:
        """Verify employee attribute assignment and get_details()."""
        emp = Employee("John", "Doe", 44)
        self.assertEqual(emp.first_name, "John")
        self.assertEqual(emp.last_name, "Doe")
        self.assertEqual(emp.age, 44)
        self.assertEqual(emp.email, "john.doe@company.com")
        self.assertEqual(emp.get_details(), "John Doe, Age: 44")

    def test_inspect_object_attributes(self) -> None:
        """Verify dir() introspection returning public attributes."""
        attrs = inspect_object_attributes(Car)
        self.assertIn("brand", attrs)
        self.assertIn("model", attrs)


class TestClassAndInstanceAttributes(unittest.TestCase):
    """Unit tests for class attributes vs instance attributes and variable shadowing."""

    def test_class_counter_and_shadowing(self) -> None:
        """Verify total_employee_count incrementing and instance raise_rate shadowing."""
        initial_count = EmployeeAccount.total_employee_count
        emp1 = EmployeeAccount("Alice", "Smith", 50000.0)
        self.assertEqual(EmployeeAccount.total_employee_count, initial_count + 1)

        # Default pay raise (1.05)
        emp1.apply_pay_raise()
        self.assertEqual(emp1.salary, 52500.0)

        # Custom instance raise rate shadowing class attribute
        emp1.raise_rate = 1.10
        emp1.apply_pay_raise()
        self.assertEqual(emp1.salary, 57750.0)


class TestInstanceClassStaticMethods(unittest.TestCase):
    """Unit tests for instance methods, @classmethod, alternative constructors, and @staticmethod."""

    def test_instance_and_class_methods(self) -> None:
        """Verify instance method self reference and class method modifying class state."""
        emp = EmployeeService("John", "Doe", 47000.0)
        msg, self_ref = emp.instance_method()
        self.assertEqual(msg, "Instance method called")
        self.assertIs(self_ref, emp)

        # Class method modifying class attribute
        EmployeeService.set_raise_rate(1.08)
        self.assertEqual(EmployeeService.default_raise_rate, 1.08)

    def test_alternative_constructor_from_string(self) -> None:
        """Verify from_string() alternative constructor parsing hyphenated input."""
        emp = EmployeeService.from_string("Julia-Smith-62000")
        self.assertEqual(emp.first_name, "Julia")
        self.assertEqual(emp.last_name, "Smith")
        self.assertEqual(emp.salary, 62000.0)

    def test_static_method_is_workday(self) -> None:
        """Verify static method date validation."""
        friday = datetime.date(2024, 9, 13)
        saturday = datetime.date(2024, 9, 14)
        self.assertTrue(EmployeeService.is_workday(friday))
        self.assertFalse(EmployeeService.is_workday(saturday))


class TestPropertyGettersSetters(unittest.TestCase):
    """Unit tests for @property, @setter, and @deleter encapsulation."""

    def test_property_lifecycle(self) -> None:
        """Verify property getter, setter assignment, and deleter reset."""
        emp = EmployeeProfile("John", "Doe")
        self.assertEqual(emp.full_name, "John Doe")
        self.assertEqual(emp.email, "john.doe@company.com")

        # Property Setter
        emp.full_name = "George Alan"
        self.assertEqual(emp.first_name, "George")
        self.assertEqual(emp.last_name, "Alan")
        self.assertEqual(emp.full_name, "George Alan")

        # Property Deleter
        del emp.full_name
        self.assertIsNone(emp.first_name)
        self.assertIsNone(emp.last_name)
        self.assertEqual(emp.full_name, "Name Deleted")
        self.assertEqual(emp.email, "")


class TestClassInheritanceAndMRO(unittest.TestCase):
    """Unit tests for single inheritance, super(), method overriding, and MRO."""

    def test_inheritance_and_team_management(self) -> None:
        """Verify Developer and Manager subclasses, team lists, isinstance, and issubclass."""
        dev1 = Developer("John", "Doe", "Berlin", 45000.0, "Python")
        dev2 = Developer("Tom", "Smith", "Paris", 54000.0, "Java")
        mgr = Manager("Elmot", "David", "Cologne", 85300.0, [dev1])

        self.assertEqual(len(mgr.employees), 1)
        mgr.add_employee(dev2)
        self.assertEqual(len(mgr.employees), 2)
        mgr.remove_employee(dev1)
        self.assertEqual(len(mgr.employees), 1)

        # Type checks
        self.assertTrue(isinstance(mgr, BaseEmployee))
        self.assertTrue(issubclass(Developer, BaseEmployee))
        self.assertFalse(issubclass(Manager, Developer))

        # MRO check
        mro_names = [cls.__name__ for cls in Developer.__mro__]
        self.assertEqual(mro_names, ["Developer", "Employee", "object"])


class TestMagicDunderMethods(unittest.TestCase):
    """Unit tests for magic dunder methods (__repr__, __str__, __add__, __len__, __eq__)."""

    def test_dunder_methods(self) -> None:
        """Verify __repr__, __str__, __add__, __len__, and __eq__."""
        emp1 = EmployeeRecord("John", "Doe", "Berlin", 45000.0)
        emp2 = EmployeeRecord("Tom", "Smith", "Paris", 54000.0)

        self.assertIn("EmployeeRecord('John'", repr(emp1))
        self.assertIn("John Doe", str(emp1))
        self.assertEqual(emp1 + emp2, 99000.0)
        self.assertEqual(len(emp1), 8)  # len("John Doe") = 8

    def test_list_number_addition(self) -> None:
        """Verify ListNumber elementwise addition overloading __add__."""
        lst1 = ListNumber([1, 2, 3])
        lst2 = ListNumber([10, 20, 30])
        res = lst1 + lst2
        self.assertEqual(res.numbers, [11, 22, 33])


class TestIceCreamMachine(unittest.TestCase):
    """Unit tests for IceCreamMachine domain modeling."""

    def test_scoop_combinations(self) -> None:
        """Verify generating flavor and topping pairs."""
        machine = IceCreamMachine(["vanilla", "chocolate"], ["fudge", "caramel"])
        scoops = machine.generate_scoops()
        self.assertEqual(len(scoops), 4)
        self.assertIn(("vanilla", "fudge"), scoops)


class TestProceduralVsOOP(unittest.TestCase):
    """Unit tests for procedural vs OOP comparative functions."""

    def test_compare_paradigms(self) -> None:
        """Verify procedural arithmetic and CustomerCounter OOP encapsulation."""
        self.assertEqual(run_procedural_example(), 5)
        counter = CustomerCounter(initial_count=2)
        counter.increment(3)
        self.assertEqual(counter.count, 5)

        comp = compare_paradigms()
        self.assertEqual(comp["procedural"]["result"], 5)
        self.assertEqual(comp["object_oriented"]["result"], 5)


if __name__ == "__main__":
    unittest.main()
