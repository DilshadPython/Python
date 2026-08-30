"""Class Definition Basics Demonstration Module.

This module demonstrates fundamental Object-Oriented Programming (OOP) concepts in Python:
class definitions, object instantiation, constructor initialization (__init__), instance attributes,
instance methods, and reflection/introspection using dir() and __dict__.
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Any


class Employee:
    """Class representing an employee in an organization."""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """Initialize an Employee instance with personal details.

        Args:
            first_name: First name of the employee.
            last_name: Last name of the employee.
            age: Age in years.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def get_details(self) -> str:
        """Return a formatted string representation of employee details.

        Returns:
            Formatted string containing first name, last name, and age.
        """
        return f"{self.first_name} {self.last_name}, Age: {self.age}"


class Car:
    """Class representing a vehicle object."""
    brand: str = "Audi"
    model: str = "A4"


def inspect_object_attributes(obj: Any) -> List[str]:
    """Inspect public methods and attributes of a class or instance object using dir().

    Args:
        obj: Class object or instance.

    Returns:
        List of non-dunder attribute names available on the target object.
    """
    return [attr for attr in dir(obj) if not attr.startswith("__")]


if __name__ == "__main__":
    print("=== Basic Class & Object Instantiation ===")
    emp1 = Employee("John", "Doe", 44)
    emp2 = Employee("Tom", "Smith", 54)

    print("Employee 1 Details:", emp1.get_details())
    print("Employee 1 Email:", emp1.email)
    print("Employee 2 Details:", emp2.get_details())
    print("Employee 2 Email:", emp2.email)

    print("\n=== Object Reflection & Introspection ===")
    my_car = Car()
    print("Car Class Attributes:", inspect_object_attributes(Car))
    print("Car Instance Attributes:", inspect_object_attributes(my_car))
