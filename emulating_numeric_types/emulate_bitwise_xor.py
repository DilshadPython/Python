"""
Python Data Model: Emulating Bitwise XOR (`__xor__`, `__rxor__`, `__ixor__`)

This module demonstrates overloading the bitwise XOR operator `^` for a custom
`BitField` class.

Magic Methods:
- `__xor__(self, other)`: Implements `self ^ other`.
- `__rxor__(self, other)`: Implements `other ^ self` (reflected bitwise XOR).
- `__ixor__(self, other)`: Implements `self ^= other` (in-place bitwise XOR).
"""
from typing import Union


class BitField:
    """Represents a bitfield supporting exclusive-OR operations."""

    def __init__(self, value: int) -> None:
        self.value = int(value)

    def __xor__(self, other: Union["BitField", int]) -> "BitField":
        """Handles `self ^ other`."""
        if isinstance(other, BitField):
            return BitField(self.value ^ other.value)
        if isinstance(other, int):
            return BitField(self.value ^ other)
        return NotImplemented

    def __rxor__(self, other: int) -> "BitField":
        """Handles `other ^ self`."""
        if isinstance(other, int):
            return BitField(other ^ self.value)
        return NotImplemented

    def __ixor__(self, other: Union["BitField", int]) -> "BitField":
        """Handles `self ^= other` in-place."""
        if isinstance(other, BitField):
            self.value ^= other.value
            return self
        if isinstance(other, int):
            self.value ^= other
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"BitField(bin={bin(self.value)}, dec={self.value})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BitField):
            return False
        return self.value == other.value


def main() -> None:
    """Demonstrates bitwise XOR (^) operator overloading."""
    b1 = BitField(0b1100)  # 12
    b2 = BitField(0b1010)  # 10

    # 1. Forward Bitwise XOR
    xor_res = b1 ^ b2
    print(f"Forward Bitwise XOR ({b1} ^ {b2}): {xor_res}")

    # 2. Reflected Bitwise XOR
    ref_xor = 0b1111 ^ b1
    print(f"Reflected Bitwise XOR (0b1111 ^ {b1}): {ref_xor}")

    # 3. In-place Bitwise XOR
    b1 ^= b2
    print(f"In-place Bitwise XOR (b1 ^= b2): {b1}")


if __name__ == "__main__":
    main()
