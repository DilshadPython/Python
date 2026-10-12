"""
Advanced Object-Oriented Programming: Class Methods & Factory Constructors.

This module demonstrates using `@classmethod` decorators for mutating class-level variables
and implementing factory constructors that instantiate objects from parsed custom data formats.
"""
# "from typing import ..." imports Type and TypeVar annotations directly into local scope.
from typing import Type, TypeVar

TStaff = TypeVar("TStaff", bound="Staff")


class Staff:
    """Represents staff members with class-level salary increase management and string factory constructor."""

    number_of_staff: int = 0
    increase_pay_rate: float = 1.06

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize Staff instance attributes."""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = float(salary)
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@mail.com"

        Staff.number_of_staff += 1

    def full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    def apply_salary_raise(self) -> float:
        """Apply salary raise multiplier to salary."""
        self.salary = round(self.salary * self.increase_pay_rate, 2)
        return self.salary

    @classmethod
    def set_increase_pay(cls, rate: float) -> None:
        """
        Class method modifying class-level default raise rate.

        Args:
            rate (float): New salary increase multiplier (e.g., 1.09).
        """
        if rate <= 0:
            raise ValueError("Raise rate must be positive.")
        cls.increase_pay_rate = rate

    @classmethod
    def from_string(cls: Type[TStaff], staff_str: str) -> TStaff:
        """
        Factory class method instantiating Staff from a hyphenated string ('First-Last-Salary').

        Args:
            staff_str (str): Hyphen-separated string of staff data.

        Returns:
            TStaff: New instance of Staff.
        """
        first, last, salary_str = staff_str.split("-")
        return cls(first, last, float(salary_str))
