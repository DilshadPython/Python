"""
Demonstrates argument unpacking (*args) in Python functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def calculate_sum(*args: Union[int, float]) -> Union[int, float]:
    """Calculate and return the sum of positional arguments."""
    return sum(args)


if __name__ == "__main__":
    numbers = [10, 20, 30]
    print(f"Sum of list: {calculate_sum(*numbers)}")
    tup = (5, 15, 25)
    print(f"Sum of tuple: {calculate_sum(*tup)}")
