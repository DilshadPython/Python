"""
Demonstrates built-in abs() function for integer, float, and complex types.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple


def calculate_abs_values(n1: float, n2: float, n3: float, n_complex: complex) -> Tuple[float, float, float, float]:
    """Return absolute values for numeric and complex inputs as a tuple."""
    return abs(n1), abs(n2), abs(n3), abs(n_complex)


if __name__ == '__main__':
    v1, v2, v3, v4 = calculate_abs_values(-2.45, -33, 12.68, 2 + 3j)
    print(f"Abs values: {v1}, {v2}, {v3}, {v4}")
