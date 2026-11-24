"""Logical 'not' Operator (Boolean Inversion).

Demonstrates using the 'not' operator to invert a truth value:
- 'not True' evaluates to False
- 'not False' evaluates to True

Import Notes:
    - 'from typing import Union': Standard library typing import for annotations.
"""

from typing import Union


def check_registration_status(is_registered: bool) -> str:
    """Return a message indicating registration status using logical 'not'."""
    if not is_registered:
        return "User is NOT registered in the database."
    else:
        return "User IS registered in the database."


def demo_if_not() -> None:
    """Demonstrate logical NOT evaluation."""
    status_flag = True
    print(f"Status Flag: {status_flag} -> {check_registration_status(status_flag)}")

    status_flag = False
    print(f"Status Flag: {status_flag} -> {check_registration_status(status_flag)}")


if __name__ == "__main__":
    demo_if_not()
