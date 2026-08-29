"""
Demonstrates functions returning boolean truth values.
"""
# Import explanation:
# 'from typing import Union' imports type annotation helpers from standard library typing module.
# Union[int, float] allows parameters that accept either integer or floating-point values.
from typing import Union


def is_even(number: int) -> bool:
    """Check if an integer is even."""
    return number % 2 == 0


def is_positive(number: Union[int, float]) -> bool:
    """Check if a number is strictly positive (> 0)."""
    return number > 0


if __name__ == "__main__":
    print(f"Is 10 even? {is_even(10)}")
    print(f"Is -5 positive? {is_positive(-5)}")
