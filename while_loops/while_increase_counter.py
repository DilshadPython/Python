"""
Demonstrates increasing integer counter variable inside a while loop.
"""
from typing import List


def increase_counter(start: int = 0, stop: int = 20) -> List[int]:
    """Increment variable from start to stop inclusive."""
    x = start
    values: List[int] = []
    while x <= stop:
        values.append(x)
        x += 1
    return values


if __name__ == '__main__':
    res = increase_counter(0, 5)
    print("Increased counter sequence (0 to 5):", res)
