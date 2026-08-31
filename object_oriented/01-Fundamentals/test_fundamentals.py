"""
Unit test suite verifying Object-Oriented Fundamentals (01-Fundamentals).
"""
# "import module" loads unittest from standard library framework.
import unittest

# "from module import name" imports fundamentals classes into test scope.
from basic_inheritance import Developer, Person
from class_and_instance_attributes import Employee
from class_definition_basics import User, procedural_representation


class TestOOPFundamentals(unittest.TestCase):
    """Test suite covering basic class instantiation, attributes, and inheritance."""

    def test_user_initialization_and_properties(self):
        """Verify User instance constructor and email property."""
        u = User("John", "Doe", 1000.0)
        self.assertEqual(u.full_name(), "John Doe")
        self.assertEqual(u.email, "john.doe@company.com")
        self.assertEqual(u.payment, 1000.0)

        u.apply_discount(0.90)
        self.assertEqual(u.payment, 900.0)

    def test_user_invalid_inputs(self):
        """Verify ValueError is raised on invalid user names or negative payment."""
        with self.assertRaises(ValueError):
            User("", "Doe", 100.0)
        with self.assertRaises(ValueError):
            User("John", "Doe", -50.0)

    def test_procedural_vs_oop(self):
        """Verify procedural helper output matches User entity behavior."""
        p = procedural_representation("Alice", "Smith", 500.0)
        self.assertEqual(p["first_name"], "Alice")
        self.assertEqual(p["email"], "alice.smith@company.com")

    def test_employee_class_and_instance_attributes(self):
        """Verify Employee class attributes and salary raise calculations."""
        initial_count = Employee.total_employees
        emp1 = Employee("Mark", "Zuck", 5000.0)
        emp2 = Employee("Bill", "Gates", 6000.0)

        self.assertEqual(Employee.total_employees, initial_count + 2)
        self.assertEqual(emp1.apply_salary_raise(), 5250.0)

        # Override raise rate on instance level
        emp2.raise_rate = 1.10
        self.assertEqual(emp2.apply_salary_raise(), 6600.0)

    def test_inheritance_and_super_delegation(self):
        """Verify Developer subclassing Person via super()."""
        dev = Developer("Guido", "van Rossum", 67, "Python")
        self.assertTrue(isinstance(dev, Person))
        self.assertTrue(isinstance(dev, Developer))
        self.assertEqual(dev.full_name(), "Guido van Rossum")
        self.assertEqual(dev.developer_summary(), "Guido van Rossum (67) - Primary Tech: Python")


if __name__ == "__main__":
    unittest.main()
