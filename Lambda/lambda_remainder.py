"""
Demonstrates lambda functions for modulo/remainder operations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Union

# Lambda function computing remainder modulo 8
remainder_by_eight: Callable[[int], int] = lambda num: num % 8

# Lambda function computing modulo remainder of two arbitrary integers
remainder_two_integers: Callable[[int, int], int] = lambda a, b: a % b if b != 0 else 0


def calculate_remainder(num: int = 19) -> int:
    """Calculate and return num % 8 using lambda function."""
    return remainder_by_eight(num)


if __name__ == '__main__':
    n = 19
    print(f"{n} % 8 = {remainder_by_eight(n)}")
    print(f"25 % 7 = {remainder_two_integers(25, 7)}")
