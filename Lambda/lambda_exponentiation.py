"""
Demonstrates lambda functions for power/exponentiation operations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable, Union

# Lambda function raising a base number to power of 9
power_of_nine: Callable[[Union[int, float]], Union[int, float]] = lambda num: num ** 9

# Lambda function raising base to arbitrary power
power_base_exp: Callable[[Union[int, float], int], Union[int, float]] = lambda base, exp: base ** exp


def calculate_power(num: Union[int, float] = 2) -> Union[int, float]:
    """Calculate and return num ** 9 using lambda function."""
    return power_of_nine(num)


if __name__ == '__main__':
    n = 2
    print(f"{n} ** 9 = {power_of_nine(n)}")
    print(f"3 ** 4 = {power_base_exp(3, 4)}")
