"""Staff Management and Instance Attribute Introspection Module.

This module demonstrates class attribute tracking (`number_of_staff`), instance state modification,
and namespace introspection via `__dict__`.
"""

from typing import Dict, Any


class Staff:
    """Class tracking total staff instances and managing salary pay raises."""

    number_of_staff: int = 0
    default_pay_raise: float = 1.1

    def __init__(self, first_name: str, last_name: str, payment: float) -> None:
        """Initialize Staff instance.

        Args:
            first_name: First name.
            last_name: Last name.
            payment: Base payment amount.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.payment: float = payment
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@mail.com"

        Staff.number_of_staff += 1

    def full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    def increase_payment(self) -> None:
        """Apply pay raise multiplier to base payment."""
        self.payment = float(int(self.payment * self.default_pay_raise))


if __name__ == "__main__":
    print("=== Staff Management Demonstration ===")
    print("Staff count before instantiation:", Staff.number_of_staff)

    user1 = Staff("Tom", "George", 2800.0)
    user2 = Staff("Jane", "Tim", 3400.0)

    print("Staff count after instantiation:", Staff.number_of_staff)
    print("\n--- User 1 ---")
    print("Full Name:", user1.full_name())
    print("Email:", user1.email)
    print("Initial Payment:", user1.payment)
    user1.increase_payment()
    print("Payment after raise:", user1.payment)

    print("\n--- User 2 ---")
    print("Full Name:", user2.full_name())
    print("Email:", user2.email)
    print("Initial Payment:", user2.payment)
    user2.increase_payment()
    print("Payment after raise:", user2.payment)

    print("\n--- Introspection of Class and Instance Namespaces (__dict__) ---")
    print("Staff Class __dict__ keys:", list(Staff.__dict__.keys()))
    print("user1 Instance __dict__:", user1.__dict__)
