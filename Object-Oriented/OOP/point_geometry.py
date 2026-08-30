"""Point Geometry Vector Module.

This module demonstrates 2D point vector arithmetic and comparison operator overloading:
addition (`+`), subtraction (`-`), dot product multiplication (`*`), and magnitude (`abs()`).
"""

import math
from typing import Tuple


class Point:
    """Class representing a 2D vector Point (x, y)."""

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """Initialize Point instance with x and y coordinates."""
        self.x: float = float(x)
        self.y: float = float(y)

    @property
    def coordinates(self) -> Tuple[float, float]:
        """Return point coordinates tuple (x, y)."""
        return (self.x, self.y)

    def magnitude(self) -> float:
        """Calculate and return Euclidean distance (magnitude) from origin (0, 0)."""
        return math.hypot(self.x, self.y)

    def __add__(self, other: "Point") -> "Point":
        """Vector addition: Point(x1 + x2, y1 + y2)."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Point") -> "Point":
        """Vector subtraction: Point(x1 - x2, y1 - y2)."""
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: "Point") -> float:
        """Vector dot product: (x1 * x2) + (y1 * y2)."""
        if isinstance(other, Point):
            return (self.x * other.x) + (self.y * other.y)
        return NotImplemented

    def __abs__(self) -> float:
        """Return magnitude using abs(point)."""
        return self.magnitude()

    def __eq__(self, other: object) -> bool:
        """Check coordinate equality."""
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        """Developer string representation."""
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    print("=== Point Geometry Demonstration ===")
    p1 = Point(4, 5)
    p2 = Point(7, 9)
    p3 = Point(1, 4)
    p4 = Point(7, 3)

    print("p1 + p3:", p1 + p3)
    print("p2 - p4:", p2 - p4)
    print("p3 * p4 (Dot product):", p3 * p4)
    print("abs(p1) (Magnitude):", abs(p1))
