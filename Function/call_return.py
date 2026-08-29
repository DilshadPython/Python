"""
Demonstrates function calls, return values, and mathematical exponents.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def calculate_exponent_square(n: Union[int, float]) -> Union[int, float]:
    """Return the square of a given number."""
    return n * n


def power(n: Union[int, float], exp: int) -> Union[int, float]:
    """Return n raised to the power of exp."""
    return n ** exp


if __name__ == '__main__':
    print("4 squared:", calculate_exponent_square(4))
    print("2 to power 3:", power(2, 3))
