"""
Python Data Model: Emulating Bitwise OR (`__or__`, `__ror__`, `__ior__`)

This module demonstrates overloading the bitwise OR operator `|` for a custom
`BitFlags` type.

Magic Methods:
- `__or__(self, other)`: Implements `self | other`.
- `__ror__(self, other)`: Implements `other | self` (reflected bitwise OR).
- `__ior__(self, other)`: Implements `self |= other` (in-place bitwise OR).
"""
from typing import Union


class BitFlags:
    """Represents a set of binary feature flags supporting bitwise OR."""

    def __init__(self, flags: int) -> None:
        self.flags = int(flags)

    def __or__(self, other: Union["BitFlags", int]) -> "BitFlags":
        """Handles `self | other`."""
        if isinstance(other, BitFlags):
            return BitFlags(self.flags | other.flags)
        if isinstance(other, int):
            return BitFlags(self.flags | other)
        return NotImplemented

    def __ror__(self, other: int) -> "BitFlags":
        """Handles `other | self`."""
        if isinstance(other, int):
            return BitFlags(other | self.flags)
        return NotImplemented

    def __ior__(self, other: Union["BitFlags", int]) -> "BitFlags":
        """Handles `self |= other` in-place."""
        if isinstance(other, BitFlags):
            self.flags |= other.flags
            return self
        if isinstance(other, int):
            self.flags |= other
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"BitFlags(bin={bin(self.flags)}, dec={self.flags})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BitFlags):
            return False
        return self.flags == other.flags


def main() -> None:
    """Demonstrates bitwise OR (|) operator overloading."""
    f1 = BitFlags(0b0100)  # 4
    f2 = BitFlags(0b0010)  # 2

    # 1. Forward Bitwise OR
    combined = f1 | f2
    print(f"Forward Bitwise OR ({f1} | {f2}): {combined}")

    # 2. Reflected Bitwise OR
    ref_or = 0b0001 | f1
    print(f"Reflected Bitwise OR (0b0001 | {f1}): {ref_or}")

    # 3. In-place Bitwise OR
    f1 |= f2
    print(f"In-place Bitwise OR (f1 |= f2): {f1}")


if __name__ == "__main__":
    main()
