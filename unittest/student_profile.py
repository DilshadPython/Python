"""
Defines the Student class encapsulating student attributes, properties, and tuition methods.
"""
# "from module import name" imports specific type annotations directly into local scope.
from typing import Optional


class Student:
    """
    Encapsulates student profile data, email generation, and loan calculation.
    """
    DEFAULT_LOAN_DISCOUNT: float = 0.93

    def __init__(self, first_name: str, last_name: str, tuition_balance: float) -> None:
        """
        Initialize Student instance with name and tuition balance.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            tuition_balance (float): Total tuition amount owed.
        """
        if not first_name.strip() or not last_name.strip():
            raise ValueError("First and last names cannot be empty.")
        if tuition_balance < 0:
            raise ValueError("Tuition balance cannot be negative.")

        self.first_name: str = first_name.strip()
        self.last_name: str = last_name.strip()
        self.tuition_balance: float = float(tuition_balance)

    @property
    def email(self) -> str:
        """Dynamically construct and return student email address."""
        return f"{self.first_name.lower()}.{self.last_name.lower()}@university.edu"

    @property
    def full_name(self) -> str:
        """Dynamically construct and return student full name."""
        return f"{self.first_name} {self.last_name}"

    def apply_loan_discount(self, discount_factor: Optional[float] = None) -> float:
        """
        Apply financial loan discount factor to tuition balance.

        Args:
            discount_factor (Optional[float]): Discount multiplier (defaults to DEFAULT_LOAN_DISCOUNT).

        Returns:
            float: Updated tuition balance.
        """
        factor = discount_factor if discount_factor is not None else self.DEFAULT_LOAN_DISCOUNT
        if factor <= 0:
            raise ValueError("Discount factor must be positive.")
        self.tuition_balance = round(self.tuition_balance * factor, 2)
        return self.tuition_balance
