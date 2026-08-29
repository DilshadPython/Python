"""
Demonstrates `functools.reduce()` for accumulating sequence results.
"""
# "import module" imports the full standard library "functools" module into local scope.
import functools
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List

def add(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y

def sum_sequence(numbers: List[int]) -> int:
    """Sum a list of numbers using functools.reduce()."""
    return functools.reduce(add, numbers, 0)

if __name__ == '__main__':
    nums = list(range(1, 11))
    print("Sequence:", nums)
    print("Sum via reduce():", sum_sequence(nums))
