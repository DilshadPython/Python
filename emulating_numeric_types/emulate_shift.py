"""
Python Data Model: Emulating Bitwise Shifts (`__lshift__`, `__rshift__`, `__ilshift__`, `__irshift__`)

This module demonstrates overloading left shift `<<` and right shift `>>` operators
for a custom `BitRegister` class.

Magic Methods:
- `__lshift__(self, other)`: Implements `self << other`.
- `__rshift__(self, other)`: Implements `self >> other`.
- `__ilshift__(self, other)`: Implements `self <<= other` (in-place left shift).
- `__irshift__(self, other)`: Implements `self >>= other` (in-place right shift).
"""
from typing import Union


class BitRegister:
    """Represents a bit register supporting left and right bit shifts."""

    def __init__(self, value: int) -> None:
        self.value = int(value)

    def __lshift__(self, count: int) -> "BitRegister":
        """Handles `self << count`."""
        if isinstance(count, int):
            return BitRegister(self.value << count)
        return NotImplemented

    def __rshift__(self, count: int) -> "BitRegister":
        """Handles `self >> count`."""
        if isinstance(count, int):
            return BitRegister(self.value >> count)
        return NotImplemented

    def __ilshift__(self, count: int) -> "BitRegister":
        """Handles `self <<= count` in-place."""
        if isinstance(count, int):
            self.value <<= count
            return self
        return NotImplemented

    def __irshift__(self, count: int) -> "BitRegister":
        """Handles `self >>= count` in-place."""
        if isinstance(count, int):
            self.value >>= count
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"BitRegister(bin={bin(self.value)}, dec={self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BitRegister):
            return False
        return self.value == other.value


def main() -> None:
    """Demonstrates bitwise shift (<<, >>) operator overloading."""
    reg = BitRegister(0b0001)  # 1

    # 1. Left Shift
    left_shifted = reg << 3
    print(f"Left Shift ({reg} << 3): {left_shifted}")

    # 2. Right Shift
    right_shifted = left_shifted >> 2
    print(f"Right Shift ({left_shifted} >> 2): {right_shifted}")

    # 3. In-place Left Shift
    reg <<= 4
    print(f"In-place Left Shift (reg <<= 4): {reg}")

    # 4. In-place Right Shift
    reg >>= 2
    print(f"In-place Right Shift (reg >>= 2): {reg}")


if __name__ == "__main__":
    main()
