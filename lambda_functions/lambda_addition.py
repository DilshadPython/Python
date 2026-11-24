"""
Demonstrates lambda functions for addition operations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Union

# Lambda function adding a constant value (8) to a given number
add_eight: Callable[[Union[int, float]], Union[int, float]] = lambda num: num + 8

# Lambda function adding two arbitrary numbers
add_two_numbers: Callable[[Union[int, float], Union[int, float]], Union[int, float]] = lambda x, y: x + y


def calculate_addition(num: Union[int, float] = 10) -> Union[int, float]:
    """Calculate and return num + 8 using lambda function."""
    return add_eight(num)


if __name__ == '__main__':
    n = 10
    print(f"{n} + 8 = {add_eight(n)}")
    print(f"9 + 77 = {add_two_numbers(9, 77)}")
