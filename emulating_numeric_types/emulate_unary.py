"""
Python Data Model: Emulating Unary Operators (`__neg__`, `__pos__`, `__abs__`, `__invert__`)

This module demonstrates overloading unary arithmetic and bitwise operators for a
custom `Point2D` class.

Magic Methods:
- `__neg__(self)`: Implements `-self` (negation).
- `__pos__(self)`: Implements `+self` (unary positive identity).
- `__abs__(self)`: Implements `abs(self)` (absolute magnitude).
- `__invert__(self)`: Implements `~self` (bitwise inversion).
"""
import math


class Point2D:
    """A 2D point supporting unary negation, magnitude, and inversion."""

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __neg__(self) -> "Point2D":
        """Handles `-self` (negation of both components)."""
        return Point2D(-self.x, -self.y)

    def __pos__(self) -> "Point2D":
        """Handles `+self` (returns copy)."""
        return Point2D(+self.x, +self.y)

    def __abs__(self) -> float:
        """Handles `abs(self)` returning Euclidean distance from origin."""
        return math.hypot(self.x, self.y)

    def __invert__(self) -> "Point2D":
        """Handles `~self` (inverts x and y as integer bitwise NOT)."""
        return Point2D(~int(self.x), ~int(self.y))

    def __repr__(self) -> str:
        return f"Point2D(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y


def main() -> None:
    """Demonstrates unary operators (-x, +x, abs(x), ~x) overloading."""
    pt = Point2D(3.0, -4.0)

    # 1. Unary Negation
    neg_pt = -pt
    print(f"Unary Negation (-{pt}): {neg_pt}")

    # 2. Unary Positive
    pos_pt = +pt
    print(f"Unary Positive (+{pt}): {pos_pt}")

    # 3. Absolute Magnitude (Euclidean norm)
    magnitude = abs(pt)
    print(f"Absolute Magnitude (abs({pt})): {magnitude}")

    # 4. Bitwise Inversion
    inverted = ~Point2D(5, 10)
    print(f"Bitwise Inversion (~Point2D(5, 10)): {inverted}")


if __name__ == "__main__":
    main()
