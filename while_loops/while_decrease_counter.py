"""
Demonstrates decrementing count-controlled while loop counter.
"""
from typing import List


def decrease_counter(start: int = 5, limit: int = 0) -> List[int]:
    """Decrement an integer variable from start down to limit using a while loop."""
    val = start
    history: List[int] = []
    while val >= limit:
        history.append(val)
        val -= 1
    return history


if __name__ == '__main__':
    res = decrease_counter(5, 0)
    print("Decreased counter sequence:", res)
