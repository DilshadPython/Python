"""
Object-Oriented Programming Fundamentals: Class vs. Instance Attributes.

This module demonstrates the critical distinction between class variables (shared across all
instances of a class) and instance variables (unique to each individual instance object).
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import ClassVar


class Employee:
    """
    Represents an employee entity demonstrating class-level counters and raise rates.
    """
    # Class attributes shared across all instances
    company_name: ClassVar[str] = "TechCorp Global"
    total_employees: ClassVar[int] = 0
    default_raise_rate: ClassVar[float] = 1.05

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """
        Initialize Employee instance attributes and update shared employee count.

        Args:
            first_name (str): Employee first name.
            last_name (str): Employee last name.
            salary (float): Annual base salary.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = float(salary)

        # Increment shared class variable counter
        Employee.total_employees += 1

    def full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    def apply_salary_raise(self) -> float:
        """
        Apply salary raise multiplier using instance override or class default.

        Returns:
            float: Updated annual salary balance.
        """
        # Look up instance attribute first, fallback to class attribute
        rate = getattr(self, "raise_rate", self.default_raise_rate)
        self.salary = round(self.salary * rate, 2)
        return self.salary
