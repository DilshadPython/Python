"""
Demonstrates simple number squaring functions in Python.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def square(num: Union[int, float]) -> Union[int, float]:
    """Return the square of a given number."""
    return num * num


if __name__ == '__main__':
    print("5 squared is:", square(5))
