"""
Demonstrates area calculation of a triangle given base and height.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union

def calculate_triangle_area(base: Union[int, float], height: Union[int, float]) -> float:
    """Calculate and return the area of a triangle (0.5 * base * height)."""
    return 0.5 * base * height

if __name__ == '__main__':
    print("Triangle area (b=10, h=5):", calculate_triangle_area(10, 5))
