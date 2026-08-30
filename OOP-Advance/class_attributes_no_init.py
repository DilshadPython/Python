"""Dynamic Class Attributes Without Constructor Demonstration Module.

This module demonstrates dynamic instance attribute assignment on basic objects created without
an explicit `__init__` constructor. It illustrates how Python dynamically populates instance dicts
and calculates attribute operations.
"""

from typing import Any


class DynamicUser:
    """Empty class demonstrating dynamic attribute attachment."""
    pass


if __name__ == "__main__":
    print("=== Dynamic Class Attributes Without Constructor ===")

    user1 = DynamicUser()
    user2 = DynamicUser()

    # Dynamically assign attributes to user1
    user1.first_name = "Alex"
    user1.last_name = "Morgan"
    user1.payment = 3000.0
    user1.email = f"{user1.first_name.lower()}.{user1.last_name.lower()}@mail.com"

    # Dynamically assign attributes to user2
    user2.first_name = "Jack"
    user2.last_name = "Johnson"
    user2.payment = 4000.0
    user2.email = f"{user2.first_name.lower()}.{user2.last_name.lower()}@mail.com"

    pay_raise = 1.1

    print("User 1:", user1.first_name, user1.last_name)
    print("User 1 Email:", user1.email)
    print("User 1 Base Payment:", user1.payment)
    print("User 1 Payment with Raise:", user1.payment * pay_raise)
    print()

    print("User 2:", user2.first_name, user2.last_name)
    print("User 2 Email:", user2.email)
    print("User 2 Base Payment:", user2.payment)
    print("User 2 Payment with Raise:", user2.payment * pay_raise)
