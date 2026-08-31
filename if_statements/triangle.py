"""Triangle Side Classification and Geometry Validation.

Classifies a triangle based on side lengths:
- Equilateral: All three sides are equal.
- Isosceles: Exactly two sides are equal.
- Scalene: All three sides are distinct.

Also validates the Triangle Inequality Theorem:
The sum of any two sides must be strictly greater than the third side.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing imports for annotating
      list collections and side length tuples.
"""

from typing import List, Tuple


def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    """Validate whether three side lengths can form a valid geometric triangle."""
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return False
    return (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a)


def classify_triangle(side_a: float, side_b: float, side_c: float) -> str:
    """Determine the type of triangle formed by three side lengths."""
    if not is_valid_triangle(side_a, side_b, side_c):
        raise ValueError("Invalid side lengths: Does not satisfy the Triangle Inequality Theorem.")

    if side_a == side_b == side_c:
        return "Equilateral Triangle"
    elif side_a != side_b and side_b != side_c and side_a != side_c:
        return "Scalene Triangle"
    else:
        return "Isosceles Triangle"


def demo_triangle() -> None:
    """Run triangle classification demonstration."""
    sample_triangles: List[Tuple[float, float, float]] = [
        (5.0, 5.0, 5.0),   # Equilateral
        (5.0, 5.0, 8.0),   # Isosceles
        (3.0, 4.0, 5.0),   # Scalene
    ]

    for a, b, c in sample_triangles:
        triangle_type = classify_triangle(a, b, c)
        print(f"Sides ({a}, {b}, {c}) -> {triangle_type}")


if __name__ == "__main__":
    demo_triangle()
