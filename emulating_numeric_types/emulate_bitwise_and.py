"""
Python Data Model: Emulating Bitwise AND (`__and__`, `__rand__`, `__iand__`)

This module demonstrates overloading the bitwise AND operator `&` for a custom
`BitMask` type.

Magic Methods:
- `__and__(self, other)`: Implements `self & other`.
- `__rand__(self, other)`: Implements `other & self` (reflected bitwise AND).
- `__iand__(self, other)`: Implements `self &= other` (in-place bitwise AND).
"""
from typing import Union


class BitMask:
    """Represents an integer bit mask with bitwise operation support."""

    def __init__(self, mask: int) -> None:
        self.mask = int(mask)

    def __and__(self, other: Union["BitMask", int]) -> "BitMask":
        """Handles `self & other`."""
        if isinstance(other, BitMask):
            return BitMask(self.mask & other.mask)
        if isinstance(other, int):
            return BitMask(self.mask & other)
        return NotImplemented

    def __rand__(self, other: int) -> "BitMask":
        """Handles `other & self`."""
        if isinstance(other, int):
            return BitMask(other & self.mask)
        return NotImplemented

    def __iand__(self, other: Union["BitMask", int]) -> "BitMask":
        """Handles `self &= other` in-place."""
        if isinstance(other, BitMask):
            self.mask &= other.mask
            return self
        if isinstance(other, int):
            self.mask &= other
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"BitMask(bin={bin(self.mask)}, dec={self.mask})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BitMask):
            return False
        return self.mask == other.mask


def main() -> None:
    """Demonstrates bitwise AND (&) operator overloading."""
    b1 = BitMask(0b1100)  # 12
    b2 = BitMask(0b1010)  # 10

    # 1. Forward Bitwise AND
    result = b1 & b2
    print(f"Forward Bitwise AND ({b1} & {b2}): {result}")

    # 2. Reflected Bitwise AND
    ref_and = 0b1111 & b1
    print(f"Reflected Bitwise AND (0b1111 & {b1}): {ref_and}")

    # 3. In-place Bitwise AND
    b1 &= b2
    print(f"In-place Bitwise AND (b1 &= b2): {b1}")


if __name__ == "__main__":
    main()
