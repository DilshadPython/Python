"""
Python Data Model: Emulating Modulo (`__mod__`, `__rmod__`, `__imod__`)

This module demonstrates overloading the modulo operator `%` for a custom
`TimeOffset` class.

Magic Methods:
- `__mod__(self, other)`: Implements `self % other`.
- `__rmod__(self, other)`: Implements `other % self` (reflected modulo).
- `__imod__(self, other)`: Implements `self %= other` (in-place modulo).
"""
from typing import Union


class TimeOffset:
    """Represents a time duration in seconds with modulo wrap-around logic."""

    def __init__(self, seconds: int) -> None:
        self.seconds = int(seconds)

    def __mod__(self, other: Union["TimeOffset", int]) -> "TimeOffset":
        """Handles `self % other`."""
        if isinstance(other, TimeOffset):
            if other.seconds == 0:
                raise ZeroDivisionError("Modulo by zero seconds")
            return TimeOffset(self.seconds % other.seconds)
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Modulo by zero integer")
            return TimeOffset(self.seconds % other)
        return NotImplemented

    def __rmod__(self, other: int) -> "TimeOffset":
        """Handles `other % self`."""
        if isinstance(other, int):
            if self.seconds == 0:
                raise ZeroDivisionError("Reflected modulo by zero seconds")
            return TimeOffset(other % self.seconds)
        return NotImplemented

    def __imod__(self, other: Union["TimeOffset", int]) -> "TimeOffset":
        """Handles `self %= other` in-place."""
        if isinstance(other, TimeOffset):
            if other.seconds == 0:
                raise ZeroDivisionError("In-place modulo by zero seconds")
            self.seconds %= other.seconds
            return self
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("In-place modulo by zero integer")
            self.seconds %= other
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"TimeOffset({self.seconds}s)"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TimeOffset):
            return False
        return self.seconds == other.seconds


def main() -> None:
    """Demonstrates modulo (%) operator overloading."""
    t1 = TimeOffset(3665)  # 1 hr, 1 min, 5 sec
    t2 = TimeOffset(60)    # 60 seconds

    # 1. Forward Modulo
    remainder = t1 % t2
    print(f"Forward Modulo ({t1} % {t2}): {remainder}")

    # 2. Reflected Modulo
    ref_rem = 100 % t2
    print(f"Reflected Modulo (100 % {t2}): {ref_rem}")

    # 3. In-place Modulo
    t1 %= 3600
    print(f"In-place Modulo (t1 %= 3600): {t1}")


if __name__ == "__main__":
    main()
