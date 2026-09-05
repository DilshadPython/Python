"""
Python Data Model: Emulating Floor Division (`__floordiv__`, `__rfloordiv__`, `__ifloordiv__`)

This module demonstrates overloading the floor division operator `//` for a custom
`Vector2D` type.

Magic Methods:
- `__floordiv__(self, other)`: Implements `self // other`.
- `__rfloordiv__(self, other)`: Implements `other // self` (reflected floor division).
- `__ifloordiv__(self, other)`: Implements `self //= other` (in-place floor division).
"""
from typing import Union


class Vector2D:
    """A 2D vector supporting integer floor division."""

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __floordiv__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `self // scalar`."""
        if isinstance(other, (int, float)):
            if float(other) == 0.0:
                raise ZeroDivisionError("Vector floor division by zero")
            return Vector2D(self.x // other, self.y // other)
        return NotImplemented

    def __rfloordiv__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `scalar // self`."""
        if isinstance(other, (int, float)):
            if self.x == 0.0 or self.y == 0.0:
                raise ZeroDivisionError("Scalar floor division by vector component with zero value")
            return Vector2D(other // self.x, other // self.y)
        return NotImplemented

    def __ifloordiv__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `self //= scalar` in-place."""
        if isinstance(other, (int, float)):
            if float(other) == 0.0:
                raise ZeroDivisionError("In-place vector floor division by zero")
            self.x //= float(other)
            self.y //= float(other)
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y


def main() -> None:
    """Demonstrates floor division (//) operator overloading."""
    v1 = Vector2D(17.0, 25.0)

    # 1. Forward Floor Division
    fdiv_v = v1 // 4
    print(f"Forward Floor Division ({v1} // 4): {fdiv_v}")

    # 2. Reflected Floor Division
    ref_fdiv = 100.0 // v1
    print(f"Reflected Floor Division (100.0 // {v1}): {ref_fdiv}")

    # 3. In-place Floor Division
    v1 //= 3
    print(f"In-place Floor Division (v1 //= 3): {v1}")


if __name__ == "__main__":
    main()
