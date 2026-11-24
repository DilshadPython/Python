"""
Demonstrates assigning function references and invoking function objects dynamically.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def square_function_ref(num: Union[int, float]) -> Union[int, float]:
    """Return the square of a given number."""
    return num * num


if __name__ == '__main__':
    func_ref = square_function_ref
    print("Square via reference:", func_ref(5))
