"""
Demonstrates filtering sequences using higher-order functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List


def even_func(num: int) -> bool:
    """Return True if number is even, False otherwise."""
    return num % 2 == 0


def get_even_numbers(numbers: List[int]) -> List[int]:
    """Filter and return only even numbers from input sequence."""
    return list(filter(even_func, numbers))


if __name__ == "__main__":
    nums = list(range(1, 12))
    print(nums)
    print(get_even_numbers(nums))