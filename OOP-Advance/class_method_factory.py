"""Class Method Factory and Class Attribute Management Module.

This module demonstrates using `@classmethod` decorators for two core OOP design patterns:
1. Class State Modification: Mutating class-level variables shared across all instances.
2. Factory Constructors: Parsing custom formatted data (e.g., hyphenated strings) to instantiate objects.
"""

# "from typing import ..." imports Type and TypeVar annotations directly into local scope.
from typing import Type, TypeVar

# TypeVar bound to Staff class for accurate classmethod return type hints
TStaff = TypeVar("TStaff", bound="Staff")


class Staff:
    """Class representing staff members with class-level counter and raise management."""

    number_of_staff: int = 0
    increase_pay_rate: float = 1.06

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize Staff instance.

        Args:
            first_name: Staff member's first name.
            last_name: Staff member's last name.
            salary: Annual base salary.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = salary
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@mail.com"

        Staff.number_of_staff += 1

    def full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    def show_email(self) -> str:
        """Return email address."""
        return self.email

    def increase_salary(self) -> None:
        """Apply pay raise multiplier to salary."""
        self.salary = float(int(self.salary * self.increase_pay_rate))

    @classmethod
    def set_increase_pay(cls, rate: float) -> None:
        """Class method to update default raise rate across all instances.

        Args:
            rate: New salary increase multiplier (e.g., 1.09).
        """
        cls.increase_pay_rate = rate

    @classmethod
    def from_string(cls: Type[TStaff], staff_str: str) -> TStaff:
        """Factory class method instantiating Staff from a hyphenated string ('First-Last-Salary').

        Args:
            staff_str: Hyphen-separated string representation of staff data.

        Returns:
            New instance of Staff.
        """
        first, last, salary_str = staff_str.split("-")
        return cls(first, last, float(salary_str))


if __name__ == "__main__":
    print("=== Class Method Factory & Class State Demonstration ===")
    staff1 = Staff("John", "Doe", 4100.0)
    staff2 = Staff("Jack", "Wall", 3900.0)

    print("Default Class Pay Increase Rate:", Staff.increase_pay_rate)
    Staff.set_increase_pay(1.09)
    print("Updated Class Pay Increase Rate:", Staff.increase_pay_rate)

    print("\n--- Factory Constructor Demonstration ---")
    staff_from_str = Staff.from_string("George-Bill-2750")
    print("Parsed Staff Name:", staff_from_str.full_name())
    print("Parsed Staff Email:", staff_from_str.show_email())
    print("Parsed Staff Salary:", staff_from_str.salary)
