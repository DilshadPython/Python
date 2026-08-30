"""Class Definition and Initialization Demonstration Module.

This module demonstrates fundamental Object-Oriented Programming (OOP) concepts:
defining classes, initializing instance attributes via constructor (__init__),
formatting instance details, and invoking methods via instance and class namespaces.
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Optional


class User:
    """Class representing a user entity with personal details and payment information."""

    def __init__(self, first_name: str, last_name: str, payment: float) -> None:
        """Initialize User instance attributes.

        Args:
            first_name: User's first name.
            last_name: User's last name.
            payment: Payment amount.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.payment: float = payment
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@mail.com"

    def full_name(self) -> str:
        """Return formatted full name of the user.

        Returns:
            String containing space-separated first and last names.
        """
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    print("=== Class Definition & Initialization Demonstration ===")

    user1 = User("Alice", "Johnson", 3300.0)
    user2 = User("Jo", "Sam", 3550.0)
    user3 = User("Claire", "Smith", 3700.0)

    print("User 1 Full Name:", user1.full_name())
    print("User 1 Email:", user1.email)
    print("User 1 Payment:", user1.payment)
    print()

    print("User 2 Full Name (Instance Method Call):", user2.full_name())
    print("User 2 Full Name (Class Method Invocation):", User.full_name(user2))
    print()

    print("User 3 Full Name (Instance Method Call):", user3.full_name())
    print("User 3 Full Name (Class Method Invocation):", User.full_name(user3))
