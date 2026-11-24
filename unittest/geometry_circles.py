"""
Provides geometric circle area calculations with strict input validation for unit testing.
"""
# "import module" loads the math module from standard library for pi constant.
import math
# "from module import name" imports Union type annotation directly into local scope.
from typing import Union

Numeric = Union[int, float]


def circle_area(radius: Numeric) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (Numeric): Radius of the circle (must be non-boolean real number >= 0).

    Returns:
        float: Calculated area of circle (pi * r^2).

    Raises:
        TypeError: If radius is a boolean, string, complex number, or non-numeric type.
        ValueError: If radius is less than zero.
    """
    # Explicitly check for bool since bool is a subclass of int in Python
    if isinstance(radius, bool) or not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a real integer or float number.")

    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    return math.pi * (radius ** 2)
