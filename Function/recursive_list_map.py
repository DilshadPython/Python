"""
Demonstrates map() higher-order function applied to custom functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List

def square(num: int) -> int:
    """Return the square of an integer."""
    return num * num

def map_squares(numbers: List[int]) -> List[int]:
    """Map square function over sequence of numbers."""
    return list(map(square, numbers))

if __name__ == '__main__':
    nums = list(range(1, 10))
    print("Mapped squares:", map_squares(nums))
