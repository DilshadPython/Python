"""Explicit Getter and Setter Methods Demonstration Module.

This module demonstrates traditional object-oriented encapsulation using explicit getter
(`get_val`) and setter (`set_val`) instance methods to manage object internal state.
"""

from typing import Any


class Monitor:
    """Class encapsulating attribute state using explicit getter and setter methods."""

    def __init__(self, value: Any = None) -> None:
        """Initialize Monitor with optional initial value."""
        self._value: Any = value

    def set_val(self, val: Any) -> None:
        """Set internal monitor value.

        Args:
            val: Value to assign.
        """
        self._value = val

    def get_val(self) -> Any:
        """Get internal monitor value.

        Returns:
            Current value.
        """
        return self._value


if __name__ == "__main__":
    print("=== Explicit Getter & Setter Demonstration ===")
    obj1 = Monitor()
    obj2 = Monitor()

    obj1.set_val(22)
    obj2.set_val(55)

    print("Object 1 Value:", obj1.get_val())
    print("Object 2 Value:", obj2.get_val())
