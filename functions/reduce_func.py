"""
Demonstrates `functools.reduce()` for accumulating sequence results.
"""
import functools
from typing import List, Union


def add_pair(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Add two numeric values together."""
    return x + y


def sum_sequence(sequence: List[Union[int, float]]) -> Union[int, float]:
    """Reduce sequence elements to a single cumulative sum."""
    return functools.reduce(add_pair, sequence)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(f"Cumulative sum of {numbers}: {sum_sequence(numbers)}")
