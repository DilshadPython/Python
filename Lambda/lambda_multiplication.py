"""
Demonstrates lambda functions for multiplication operations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Union

# Lambda function multiplying a number by 82
multiply_by_82: Callable[[Union[int, float]], Union[int, float]] = lambda num: num * 82

# Lambda function multiplying two arbitrary numbers
multiply_two_numbers: Callable[[Union[int, float], Union[int, float]], Union[int, float]] = lambda a, b: a * b


def calculate_multiplication(num: Union[int, float] = 5) -> Union[int, float]:
    """Calculate and return num * 82 using lambda function."""
    return multiply_by_82(num)


if __name__ == '__main__':
    n = 5
    print(f"{n} * 82 = {multiply_by_82(n)}")
    print(f"7 * 9 = {multiply_two_numbers(7, 9)}")
