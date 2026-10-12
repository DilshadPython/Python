"""
Advanced Object-Oriented Programming: Magic & Dunder Methods Operator Overloading.

This module demonstrates operator overloading and object protocol integration via special double-underscore
(dunder) methods (`__repr__`, `__str__`, `__len__`, `__add__`, `__eq__`).
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Union

Numeric = Union[int, float]


class Vector2D:
    """Represents a 2D Cartesian vector with mathematical operator overloading."""

    def __init__(self, x: Numeric, y: Numeric) -> None:
        """Initialize 2D vector coordinates."""
        self.x: Numeric = x
        self.y: Numeric = y

    def __repr__(self) -> str:
        """Official string representation for debugging and reproduction."""
        return f"Vector2D(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"({self.x}, {self.y})"

    def __len__(self) -> int:
        """Return vector dimension count (always 2 for Vector2D)."""
        return 2

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """Overload addition (+) operator for vector addition."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        """Overload subtraction (-) operator for vector subtraction."""
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        """Overload equality (==) operator."""
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y
