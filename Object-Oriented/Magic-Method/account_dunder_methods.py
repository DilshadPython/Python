"""Account Dunder Methods Demonstration Module.

This module demonstrates custom object magic (dunder) methods:
`__repr__`, `__str__`, `__add__`, `__len__`, and `__eq__`.
"""

from typing import Union


class CustomAccount:
    """Class representing a financial account with custom magic dunder implementations."""

    extra_pay_rate: float = 1.17

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize CustomAccount instance."""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = float(salary)
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@account.com"

    def get_full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        """Return unambiguous developer string representation."""
        return f"CustomAccount('{self.first_name}', '{self.last_name}', {self.salary})"

    def __str__(self) -> str:
        """Return user-friendly string representation."""
        return f"{self.get_full_name()} <{self.email}>"

    def __add__(self, other: "CustomAccount") -> float:
        """Overload addition (+) to compute combined salary of two accounts.

        Args:
            other: Second CustomAccount instance.

        Returns:
            Sum of salaries.
        """
        if isinstance(other, CustomAccount):
            return self.salary + other.salary
        return NotImplemented

    def __len__(self) -> int:
        """Overload len() to return length of owner full name.

        Returns:
            Character length of full name.
        """
        return len(self.get_full_name())

    def __eq__(self, other: object) -> bool:
        """Overload equality (==) based on salary and name.

        Args:
            other: Object to compare against.

        Returns:
            True if attributes match, False otherwise.
        """
        if not isinstance(other, CustomAccount):
            return NotImplemented
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.salary == other.salary
        )


if __name__ == "__main__":
    print("=== Account Dunder Methods Demonstration ===")
    acc1 = CustomAccount("Math", "George", 60500.0)
    acc2 = CustomAccount("Tom", "Alan", 82500.0)

    print("str(acc1):", str(acc1))
    print("repr(acc1):", repr(acc1))
    print("Combined Salaries (acc1 + acc2):", acc1 + acc2)
    print("len(acc1) [name length]:", len(acc1))
    print("acc1 == acc2:", acc1 == acc2)
