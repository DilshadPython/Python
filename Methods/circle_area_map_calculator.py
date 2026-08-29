"""
Demonstrates mapping a function over a sequence using built-in map().
"""
# "from module import name" imports specific type hint symbols directly into local scope.
import math
from typing import List


def calculate_circle_area(radius: float) -> float:
    """Calculate and return area of circle given radius: A = π * r^2."""
    return math.pi * (radius ** 2)


def calculate_areas_for_radii(radii: List[float]) -> List[float]:
    """Map circle area calculation over a list of radius values."""
    return list(map(calculate_circle_area, radii))


if __name__ == '__main__':
    sample_radii: List[float] = [6.5, 3.1, 0.7, 0.51, 22.3]
    areas = calculate_areas_for_radii(sample_radii)
    print("Calculated Circle Areas:", [round(a, 4) for a in areas])
