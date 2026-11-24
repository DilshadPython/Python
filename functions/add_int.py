"""
Demonstrates basic function definitions, addition operations, and type annotations in Python.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def add_int(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers and return their sum."""
    return a + b


def my_add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def add_me(x: int, y: int) -> int:
    """Return the sum of two integers."""
    return x + y


if __name__ == "__main__":
    print(add_int(10, 20))
    print(my_add(4, 56))
    print(add_me(7, 9))
