"""
Mathematical Calculator Fundamentals Module.

This module demonstrates foundational mathematical calculations:
- Pythagorean theorem hypotenuse calculation: sqrt(a^2 + b^2)
- Difference of squares computation: (a^2 - b^2)
- Euclidean 2D distance calculation
- Floating-point precision rounding utilities

PEP 8 compliant, type-annotated, compatible with Python 2.7 - 3.13.
"""

import math
from typing import Dict, Tuple, Union


def compute_pythagorean_hypotenuse(first: float, second: float) -> float:
    """
    Computes hypotenuse length of a right triangle given two sides (a, b).

    Args:
        first (float): Length of first side (a).
        second (float): Length of second side (b).

    Returns:
        float: Hypotenuse c = sqrt(a^2 + b^2), rounded to 4 decimal places.
    """
    sum_of_squares = math.pow(first, 2) + math.pow(second, 2)
    return round(math.sqrt(sum_of_squares), 4)


def compute_difference_of_squares(first: float, second: float) -> float:
    """
    Computes difference of squares: (a^2 - b^2).

    Args:
        first (float): First term (a).
        second (float): Second term (b).

    Returns:
        float: Difference of squares result.
    """
    return round(math.pow(first, 2) - math.pow(second, 2), 4)


def compute_euclidean_distance(
    point1: Tuple[float, float], point2: Tuple[float, float]
) -> float:
    """
    Computes 2D Euclidean distance between two coordinate points (x1, y1) and (x2, y2).

    Args:
        point1 (Tuple[float, float]): (x1, y1) coordinates.
        point2 (Tuple[float, float]): (x2, y2) coordinates.

    Returns:
        float: Distance between point1 and point2.
    """
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return round(math.sqrt(dx * dx + dy * dy), 4)


if __name__ == "__main__":
    print("Pythagorean Hypotenuse (a=3, b=4):", compute_pythagorean_hypotenuse(3, 4))
    print("Difference of Squares (a=5, b=3) :", compute_difference_of_squares(5, 3))
    print("2D Distance ((0, 0) to (3, 4))  :", compute_euclidean_distance((0, 0), (3, 4)))
