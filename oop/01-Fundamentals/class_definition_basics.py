"""
Object-Oriented Programming Fundamentals: Class Definition & Instantiation.

This module introduces core OOP concepts: defining classes, constructing instance attributes
via the `__init__` method, defining instance methods using `self`, and comparing procedural
data structures against object-oriented encapsulation.
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Optional


class User:
    """
    Represents a user entity encapsulating profile state and instance methods.
    """

    def __init__(self, first_name: str, last_name: str, payment: float) -> None:
        """
        Initialize User instance with name and payment balance.

        Args:
            first_name (str): User's first name.
            last_name (str): User's last name.
            payment (float): User's initial payment balance.
        """
        if not first_name.strip() or not last_name.strip():
            raise ValueError("First and last names cannot be empty.")
        if payment < 0:
            raise ValueError("Payment balance cannot be negative.")

        self.first_name: str = first_name.strip()
        self.last_name: str = last_name.strip()
        self.payment: float = float(payment)

    @property
    def email(self) -> str:
        """Dynamically generate email address based on first and last name."""
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

    def full_name(self) -> str:
        """
        Return the formatted full name of the user.

        Returns:
            str: Space-separated first and last name.
        """
        return f"{self.first_name} {self.last_name}"

    def apply_discount(self, rate: float) -> float:
        """
        Apply a discount rate multiplier to the user's payment balance.

        Args:
            rate (float): Multiplier rate (e.g. 0.90 for 10% discount).

        Returns:
            float: Updated payment balance.
        """
        if rate <= 0 or rate > 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        self.payment = round(self.payment * rate, 2)
        return self.payment


def procedural_representation(first_name: str, last_name: str, payment: float) -> dict:
    """Legacy procedural dictionary representation of user data."""
    return {
        "first_name": first_name,
        "last_name": last_name,
        "payment": payment,
        "email": f"{first_name.lower()}.{last_name.lower()}@company.com",
    }
