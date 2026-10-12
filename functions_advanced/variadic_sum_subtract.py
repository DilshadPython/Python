"""
Demonstrates variadic numeric aggregation (summation and subtraction) using *args.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def calculate_variadic_sum(*args: Union[int, float]) -> Union[int, float]:
    """
    Calculate and return the cumulative sum of all passed numeric arguments (*args).
    
    Args:
        *args (Union[int, float]): Arbitrary count of numeric arguments.
        
    Returns:
        Union[int, float]: Cumulative sum total.
    """
    total: Union[int, float] = 0
    for arg in args:
        total += arg
    return total


def calculate_variadic_subtraction(*numbers: Union[int, float]) -> Union[int, float]:
    """
    Calculate and return the cumulative subtraction of all passed numeric arguments.
    
    Args:
        *numbers (Union[int, float]): Arbitrary count of numeric arguments.
        
    Returns:
        Union[int, float]: Cumulative subtracted total starting from zero.
    """
    total: Union[int, float] = 0
    for x in numbers:
        total -= x
    return total


if __name__ == '__main__':
    print("Sum total:", calculate_variadic_sum(2, 3, 4, 8))
    print("Subtraction total:", calculate_variadic_subtraction(22, 3, -4, 8))
