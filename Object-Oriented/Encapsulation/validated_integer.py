"""Validated Integer Demonstration Module.

This module demonstrates encapsulated integer values with defensive input parsing and safe increment methods.
"""

from typing import Any


class ValidatedInteger:
    """Class storing a validated integer state."""

    def __init__(self, initial_value: Any = 0) -> None:
        """Initialize ValidatedInteger with defensive parsing."""
        self._number: int = 0
        self.set_number(initial_value)

    def set_number(self, value: Any) -> bool:
        """Safely attempt to convert and store input value as integer.

        Args:
            value: Input value to cast.

        Returns:
            True if conversion succeeded, False otherwise.
        """
        try:
            self._number = int(value)
            return True
        except (ValueError, TypeError):
            return False

    def get_number(self) -> int:
        """Return current stored integer value."""
        return self._number

    def increment(self, amount: int = 1) -> None:
        """Increment integer value.

        Args:
            amount: Integer amount to add.
        """
        self._number += amount


if __name__ == "__main__":
    print("=== Validated Integer Demonstration ===")
    val_obj = ValidatedInteger()

    val_obj.set_number(19)
    print("Set 19:", val_obj.get_number())

    # Invalid string input leaves previous valid integer unchanged
    success = val_obj.set_number("Welcome")
    print(f"Set 'Welcome' success: {success} | Value remains:", val_obj.get_number())

    val_obj.set_number(88.06)
    print("Set float 88.06:", val_obj.get_number())

    val_obj.increment()
    print("Incremented Value:", val_obj.get_number())
