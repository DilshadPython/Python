"""
Demonstrates map() higher-order function applied to custom functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List, Union


def square_element(n: Union[int, float]) -> Union[int, float]:
    """Return the square of an element."""
    return n * n


def map_squares(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """Return list of squared numbers using map()."""
    return list(map(square_element, numbers))


if __name__ == '__main__':
    print("Mapped squares:", map_squares([1, 2, 3]))
