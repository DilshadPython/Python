"""
Python Data Model: Emulating Divmod (`__divmod__`, `__rdivmod__`)

This module demonstrates overloading the `divmod(a, b)` built-in function for a
custom `SmartQuantity` class.

Magic Methods:
- `__divmod__(self, other)`: Implements `divmod(self, other)` returning tuple `(self // other, self % other)`.
- `__rdivmod__(self, other)`: Implements `divmod(other, self)` reflected execution.
"""
from typing import Union, Tuple


class SmartQuantity:
    """Represents a numeric quantity supporting the `divmod()` built-in."""

    def __init__(self, value: int) -> None:
        self.value = int(value)

    def __divmod__(self, other: Union["SmartQuantity", int]) -> Tuple["SmartQuantity", "SmartQuantity"]:
        """Handles `divmod(self, other)`."""
        if isinstance(other, SmartQuantity):
            q, r = divmod(self.value, other.value)
            return (SmartQuantity(q), SmartQuantity(r))
        if isinstance(other, int):
            q, r = divmod(self.value, other)
            return (SmartQuantity(q), SmartQuantity(r))
        return NotImplemented

    def __rdivmod__(self, other: int) -> Tuple["SmartQuantity", "SmartQuantity"]:
        """Handles `divmod(other, self)`."""
        if isinstance(other, int):
            q, r = divmod(other, self.value)
            return (SmartQuantity(q), SmartQuantity(r))
        return NotImplemented

    def __repr__(self) -> str:
        return f"SmartQuantity({self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SmartQuantity):
            return False
        return self.value == other.value


def main() -> None:
    """Demonstrates divmod() function overloading."""
    q1 = SmartQuantity(23)
    q2 = SmartQuantity(5)

    # 1. Forward divmod()
    quotient, remainder = divmod(q1, q2)
    print(f"Forward divmod({q1}, {q2}): Quotient={quotient}, Remainder={remainder}")

    # 2. Reflected divmod()
    ref_q, ref_r = divmod(100, q2)
    print(f"Reflected divmod(100, {q2}): Quotient={ref_q}, Remainder={ref_r}")


if __name__ == "__main__":
    main()
