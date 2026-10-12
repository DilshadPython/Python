"""
Python Data Model: Emulating True Division (`__truediv__`, `__rtruediv__`, `__itruediv__`)

This module demonstrates overloading the true division operator `/` for a custom
`Vector2D` type.

Magic Methods:
- `__truediv__(self, other)`: Implements `self / other`.
- `__rtruediv__(self, other)`: Implements `other / self` (reflected true division).
- `__itruediv__(self, other)`: Implements `self /= other` (in-place division).
"""
from typing import Union


class Vector2D:
    """A 2D vector supporting scalar division."""

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __truediv__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `self / scalar`."""
        if isinstance(other, (int, float)):
            if float(other) == 0.0:
                raise ZeroDivisionError("Vector division by zero")
            return Vector2D(self.x / other, self.y / other)
        return NotImplemented

    def __rtruediv__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `scalar / self`."""
        if isinstance(other, (int, float)):
            if self.x == 0.0 or self.y == 0.0:
                raise ZeroDivisionError("Scalar division by vector component with zero value")
            return Vector2D(other / self.x, other / self.y)
        return NotImplemented

    def __itruediv__(self, other: Union[float, int]) -> "Vector2D":
        """Handles `self /= scalar` in-place."""
        if isinstance(other, (int, float)):
            if float(other) == 0.0:
                raise ZeroDivisionError("In-place vector division by zero")
            self.x /= float(other)
            self.y /= float(other)
            return self
        return NotImplemented

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y


def main() -> None:
    """Demonstrates true division (/) operator overloading."""
    v1 = Vector2D(10.0, 20.0)

    # 1. Forward True Division
    div_v = v1 / 2
    print(f"Forward True Division ({v1} / 2): {div_v}")

    # 2. Reflected True Division
    ref_div = 100.0 / v1
    print(f"Reflected True Division (100.0 / {v1}): {ref_div}")

    # 3. In-place True Division
    v1 /= 5
    print(f"In-place True Division (v1 /= 5): {v1}")


if __name__ == "__main__":
    main()
