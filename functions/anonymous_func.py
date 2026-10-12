"""
Demonstrates anonymous functions (lambda expressions) for lightweight calculations.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable

add: Callable[[float, float], float] = lambda x, y: x + y
square: Callable[[float], float] = lambda x: x ** 2

if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"4^2 = {square(4)}")
