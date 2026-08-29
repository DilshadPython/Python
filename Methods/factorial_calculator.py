"""
Demonstrates iterative factorial computation using Python functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def calculate_factorial(num: int) -> int:
    """
    Compute and return the factorial of a non-negative integer (num!).
    
    Args:
        num (int): Non-negative integer input.
        
    Returns:
        int: Calculated factorial value.
        
    Raises:
        ValueError: If num is negative.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result: int = 1
    for i in range(1, num + 1):
        result *= i
    return result


if __name__ == '__main__':
    number: int = 5
    print(f"{number}! equal to {calculate_factorial(number)}")
