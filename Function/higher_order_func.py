"""
Demonstrates higher-order function concept using `map()`.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List

def square(num: int) -> int:
    """Return square of an integer."""
    return num * num

def apply_square(numbers: List[int]) -> List[int]:
    """Map square function over a list of integers."""
    return list(map(square, numbers))

if __name__ == '__main__':
    nums = [1, 2, 3, 5, 7, 9, 4]
    print("Input:", nums)
    print("Mapped Squares:", apply_square(nums))
