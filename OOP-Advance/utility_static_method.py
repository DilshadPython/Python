"""Static Utility Method Demonstration Module.

This module demonstrates using the `@staticmethod` decorator to define utility functions
grouped logically inside a class namespace without accessing or modifying instance (`self`)
or class (`cls`) state.
"""

# "import module" loads datetime module from standard library into namespace.
import datetime
# "from typing import ..." imports Type and TypeVar annotations directly into local scope.
from typing import Type, TypeVar

TStaff = TypeVar("TStaff", bound="Staff")


class Staff:
    """Class representing staff members with instance, class, and static methods."""

    number_of_staff: int = 0
    increase_pay_rate: float = 1.06

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize Staff instance."""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = salary
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@mail.com"

        Staff.number_of_staff += 1

    def full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_string(cls: Type[TStaff], staff_str: str) -> TStaff:
        """Factory constructor parsing hyphenated string."""
        first, last, salary_str = staff_str.split("-")
        return cls(first, last, float(salary_str))

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        """Static utility method checking if a date falls on a weekday (Monday-Friday).

        Args:
            day: datetime.date object to check.

        Returns:
            True if weekday (Monday=0 to Friday=4), False if weekend (Saturday=5, Sunday=6).
        """
        # weekday(): Monday is 0, Sunday is 6
        return day.weekday() < 5


if __name__ == "__main__":
    print("=== Static Utility Method Demonstration ===")

    staff_obj = Staff.from_string("George-Bill-2750")
    print("Parsed Staff:", staff_obj.full_name())

    monday = datetime.date(2023, 5, 15)  # Monday
    sunday = datetime.date(2023, 5, 14)  # Sunday

    print("\n--- Workday Verification via Static Method ---")
    print(f"Is {monday} (Monday) a workday?:", Staff.is_workday(monday))
    print(f"Is {sunday} (Sunday) a workday?:", Staff.is_workday(sunday))
