"""
Demonstrates higher-order function concepts using .
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List, Union


def square_value(num: Union[int, float]) -> Union[int, float]:
    """Return the square of a given number."""
    return num * num


def apply_square(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """Apply square_value to each element in the input list using map()."""
    return list(map(square_value, numbers))


if __name__ == '__main__':
    print("Mapped squares:", apply_square([1, 2, 3, 4]))
