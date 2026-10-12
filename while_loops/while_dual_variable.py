"""
Demonstrates dual variable counter manipulation inside a single while loop condition.
"""
from typing import List, Tuple


def dual_variable_loop(x_start: int, y_start: int, x_limit: int = 10, y_limit: int = 0) -> List[Tuple[int, int]]:
    """Simultaneously increment x and decrement y while compound condition holds true."""
    x = x_start
    y = y_start
    pairs: List[Tuple[int, int]] = []

    while x <= x_limit and y >= y_limit:
        x += 1
        y -= 1
        pairs.append((x, y))

    return pairs


if __name__ == '__main__':
    res = dual_variable_loop(0, 10, 10, 0)
    print("Dual variable trajectory (x, y):", res)
