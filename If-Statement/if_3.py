"""Basic Conditional Statements: Integer Value Equality.

Demonstrates testing numerical equality using '==' inside an if statement.

Import Notes:
    - 'from typing import Union': Demonstrates type-hinting for numeric input validation.
"""

from typing import Union


def check_integer_equality(first_val: int, second_val: int) -> bool:
    """Return True if integer 'first_val' equals integer 'second_val'."""
    if first_val == second_val:
        return True
    return False


def demo_if_3() -> None:
    """Execute integer equality demonstration."""
    num_x, num_y = 100, 100
    if check_integer_equality(num_x, num_y):
        print(f"{num_x} and {num_y} are equal.")


if __name__ == "__main__":
    demo_if_3()
