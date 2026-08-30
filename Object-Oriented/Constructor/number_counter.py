"""Number Counter Demonstration Module.

This module demonstrates constructor variations:
1. Parameterless constructors with default values.
2. Parameterized constructors accepting initial values.
3. Defensive type casting and validation inside `__init__`.
"""

from typing import Union


class NumberCounter:
    """Class showcasing constructor options and counter increments."""

    def __init__(self, initial_value: Union[int, str] = 0) -> None:
        """Initialize NumberCounter with defensive type validation.

        Args:
            initial_value: Initial starting integer or integer-castable string.
        """
        try:
            self.value: int = int(initial_value)
        except (ValueError, TypeError):
            self.value = 0

    def increment(self, amount: int = 1) -> None:
        """Increment the counter value.

        Args:
            amount: Amount to add.
        """
        self.value += amount

    def get_value(self) -> int:
        """Return current counter value."""
        return self.value


if __name__ == "__main__":
    print("=== Number Counter Constructor Demonstration ===")

    # 1. Parameterless / Default constructor
    c1 = NumberCounter()
    c1.increment()
    print("c1 Value:", c1.get_value())

    # 2. Parameterized constructor
    c2 = NumberCounter(3)
    c2.increment()
    c2.increment()
    print("c2 Value:", c2.get_value())

    # 3. String input handled defensively
    c3 = NumberCounter("Welcome")  # Invalid string defaults to 0
    print("c3 Value (from invalid string):", c3.get_value())
