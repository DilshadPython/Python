"""Instance, Class, and Static Methods Demonstration Module.

This module demonstrates the three types of methods in Python classes:
1. Instance Methods: Bound to an object instance (`self`). Can access/modify instance state and class state.
2. Class Methods (`@classmethod`): Bound to the class object (`cls`). Used as alternative constructors or to modify class state.
3. Static Methods (`@staticmethod`): Unbound utility functions grouped logically inside a class namespace.
"""

# "import datetime" imports standard module for calendar date calculations
import datetime
from typing import Tuple, Any


class EmployeeService:
    """Class showcasing instance methods, class methods, and static methods."""

    default_raise_rate: float = 1.05

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize an EmployeeService instance.

        Args:
            first_name: First name.
            last_name: Last name.
            salary: Base annual salary.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = salary
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def instance_method(self) -> Tuple[str, Any]:
        """Instance method: receives implicit instance argument (self).

        Returns:
            Tuple of message string and self reference.
        """
        return "Instance method called", self

    @classmethod
    def set_raise_rate(cls, rate: float) -> None:
        """Class method: receives implicit class argument (cls). Modifies class state.

        Args:
            rate: New default raise rate multiplier.
        """
        cls.default_raise_rate = rate

    @classmethod
    def from_string(cls, employee_str: str) -> "EmployeeService":
        """Alternative constructor class method parsing hyphenated string ('First-Last-Salary').

        Args:
            employee_str: Hyphen-separated string.

        Returns:
            Newly constructed EmployeeService instance.
        """
        first, last, salary_str = employee_str.split("-")
        return cls(first, last, float(salary_str))

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        """Static method: utility function checking if a date is a weekday (Monday-Friday).

        Args:
            day: datetime.date object.

        Returns:
            True if weekday (Monday=0 to Friday=4), False if weekend (Saturday=5, Sunday=6).
        """
        # weekday(): Monday is 0, Sunday is 6
        return day.weekday() < 5


if __name__ == "__main__":
    print("=== Instance, Class, and Static Methods Demonstration ===")

    # 1. Instance Method
    emp = EmployeeService("John", "Doe", 47000)
    msg, obj_ref = emp.instance_method()
    print("Instance Method Call:", msg)
    print("Self Reference matches emp instance:", obj_ref is emp)

    # 2. Class Method as Alternative Constructor
    emp_from_str = EmployeeService.from_string("Julia-Smith-62000")
    print("\nParsed Employee from String:", emp_from_str.first_name, emp_from_str.last_name, emp_from_str.salary)

    # 3. Class Method modifying class state
    print("Original default raise rate:", EmployeeService.default_raise_rate)
    EmployeeService.set_raise_rate(1.08)
    print("Updated default raise rate via classmethod:", EmployeeService.default_raise_rate)

    # 4. Static Method
    workday = datetime.date(2024, 9, 13)  # Friday
    weekend = datetime.date(2024, 9, 14)  # Saturday
    print("\nIs 2024-09-13 a workday?:", EmployeeService.is_workday(workday))
    print("Is 2024-09-14 a workday?:", EmployeeService.is_workday(weekend))
