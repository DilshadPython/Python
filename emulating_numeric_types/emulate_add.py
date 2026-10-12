"""
Python Data Model: Emulating Addition (`__add__`, `__radd__`, `__iadd__`)

This module demonstrates overloading the addition operator `+` for a custom
`Vector2D` class.

Magic Methods:
- `__add__(self, other)`: Implements `self + other`.
- `__radd__(self, other)`: Implements `other + self` (reflected addition).
- `__iadd__(self, other)`: Implements `self += other` (in-place addition).
"""
from typing import Union


class Vector2D:
    """A 2D mathematical vector supporting addition operations."""

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other: Union["Vector2D", float, int]) -> "Vector2D":
        """Handles `self + other`."""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector2D(self.x + other, self.y + other)
        return NotImplemented

    def __radd__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `other + self` when `other` is a scalar."""
        return self.__add__(other)

    def __iadd__(self, other: Union["Vector2D", float, int]) -> "Vector2D":
        """Handles `self += other` in-place."""
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
            return self
        if isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y


def main() -> None:
    """Demonstrates vector addition operator overloading."""
    v1 = Vector2D(3.0, 4.0)
    v2 = Vector2D(1.0, 2.0)

    # 1. Forward Addition
    v_sum = v1 + v2
    print(f"Forward Addition ({v1} + {v2}): {v_sum}")

    # 2. Reflected Addition with scalar
    v_scalar = 10.0 + v1
    print(f"Reflected Addition (10.0 + {v1}): {v_scalar}")

    # 3. In-place Addition
    v1 += v2
    print(f"In-place Addition (v1 += v2): {v1}")


if __name__ == "__main__":
    main()
