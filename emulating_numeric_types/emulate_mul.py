"""
Python Data Model: Emulating Multiplication (`__mul__`, `__rmul__`, `__imul__`)

This module demonstrates overloading the multiplication operator `*` for scaling
and dot-product operations.

Magic Methods:
- `__mul__(self, other)`: Implements `self * other`.
- `__rmul__(self, other)`: Implements `other * self` (reflected multiplication).
- `__imul__(self, other)`: Implements `self *= other` (in-place multiplication).
"""
from typing import Union


class Vector2D:
    """A 2D vector supporting scalar multiplication and dot product."""

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __mul__(self, other: Union["Vector2D", float, int]) -> Union["Vector2D", float]:
        """Handles scalar scaling (`self * scalar`) or dot product (`self * vector`)."""
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        if isinstance(other, Vector2D):
            # Dot product calculation
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `scalar * self` reflected multiplication."""
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __imul__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `self *= scalar` in-place scaling."""
        if isinstance(other, (int, float)):
            self.x *= float(other)
            self.y *= float(other)
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y


def main() -> None:
    """Demonstrates vector multiplication operator overloading."""
    v1 = Vector2D(2.0, 3.0)
    v2 = Vector2D(4.0, 5.0)

    # 1. Scalar Scaling
    scaled = v1 * 3
    print(f"Scalar Multiplication ({v1} * 3): {scaled}")

    # 2. Reflected Multiplication
    ref_scaled = 2.5 * v1
    print(f"Reflected Multiplication (2.5 * {v1}): {ref_scaled}")

    # 3. Vector Dot Product
    dot_prod = v1 * v2
    print(f"Dot Product ({v1} * {v2}): {dot_prod}")

    # 4. In-place Scaling
    v1 *= 4
    print(f"In-place Multiplication (v1 *= 4): {v1}")


if __name__ == "__main__":
    main()
