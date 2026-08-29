"""
Demonstrates lambda functions for subtraction operations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Union

# Lambda function subtracting 8 from a given number
subtract_eight: Callable[[Union[int, float]], Union[int, float]] = lambda num: num - 8

# Lambda function subtracting two arbitrary numbers
subtract_two_numbers: Callable[[Union[int, float], Union[int, float]], Union[int, float]] = lambda a, b: a - b


def calculate_subtraction(num: Union[int, float] = 20) -> Union[int, float]:
    """Calculate and return num - 8 using lambda function."""
    return subtract_eight(num)


if __name__ == '__main__':
    n = 20
    print(f"{n} - 8 = {subtract_eight(n)}")
    print(f"100 - 45 = {subtract_two_numbers(100, 45)}")
