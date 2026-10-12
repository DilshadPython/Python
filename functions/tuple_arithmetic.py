"""
Demonstrates returning multiple arithmetic values (sum, diff) as a tuple.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple


def add_and_subtract_three(v: int, v1: int, v2: int) -> Tuple[int, int]:
    """Return sum and difference across three numbers as a tuple."""
    a = v + v1 + v2
    b = v - v1 - v2
    return a, b


if __name__ == '__main__':
    sum_val, diff_val = add_and_subtract_three(6, 8, 9)
    print(f"Sum: {sum_val}, Difference: {diff_val}")
