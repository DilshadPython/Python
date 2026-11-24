"""
Demonstrates boolean flag control (`keep_going`) for while loop termination.
"""
from typing import List, Tuple


def sum_accumulator_5_7(target: int = 24) -> List[Tuple[int, int, int]]:
    """Accumulate increments of 5 and 7 until combined sum reaches target."""
    keep_going = True
    a = 0
    b = 0
    history: List[Tuple[int, int, int]] = []

    while keep_going:
        a += 5
        b += 7
        total = a + b
        history.append((a, b, total))
        if total >= target:
            keep_going = False

    return history


if __name__ == '__main__':
    log = sum_accumulator_5_7(24)
    print("Accumulation steps:", log)
