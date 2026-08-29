"""
Demonstrates global variable scope modification within functions.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Tuple

x = 1
y = 2
z = 3


def bar(xx: int) -> Tuple[int, int, int, int]:
    """Demonstrate local variable shadowing vs global variable modification."""
    global y
    x_local = 4
    xx_local = 5
    y = 6
    z_local = 7
    return x_local, xx_local, y, z_local


if __name__ == "__main__":
    bar(x)
    print(f"Global y after bar call: {y}")
