"""
Demonstrates lambda functions for division operations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Union

# Lambda function dividing a number by 8
divide_by_eight: Callable[[Union[int, float]], float] = lambda num: num / 8.0

# Lambda function dividing two arbitrary numbers with zero check fallback
divide_two_numbers: Callable[[Union[int, float], Union[int, float]], float] = (
    lambda a, b: a / b if b != 0 else float('nan')
)


def calculate_division(num: Union[int, float] = 64) -> float:
    """Calculate and return num / 8 using lambda function."""
    return divide_by_eight(num)


if __name__ == '__main__':
    n = 64
    print(f"{n} / 8 = {divide_by_eight(n)}")
    print(f"20 / 4 = {divide_two_numbers(20, 4)}")
