"""
Demonstrates ascending and descending while loops with explicit break triggers.
"""
from typing import List, Tuple


def loop_up(limit: int = 20) -> List[int]:
    """Ascend from 0 to limit using a while loop."""
    a = 0
    asc: List[int] = []
    while a <= limit:
        asc.append(a)
        a += 1
    return asc


def loop_down(start: int = 20) -> List[int]:
    """Descend from start to 0 with explicit break on reaching boundary."""
    b = start
    desc: List[int] = []
    while b >= 0:
        desc.append(b)
        b -= 1
        if b == -1:
            break
    return desc


if __name__ == '__main__':
    print("Ascending count len:", len(loop_up(20)))
    print("Descending count len:", len(loop_down(20)))
