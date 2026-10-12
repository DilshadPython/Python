"""
Demonstrates early termination check in boolean flag controlled while loop.
"""
from typing import List, Tuple


def sum_accumulator_early_check(target: int = 24) -> List[Tuple[int, int, int]]:
    """Accumulate values checking termination flag at start of loop iteration."""
    keep_going = True
    a = 0
    b = 0
    snapshots: List[Tuple[int, int, int]] = []

    while keep_going:
        if a + b >= target:
            keep_going = False
            break
        a += 5
        b += 7
        snapshots.append((a, b, a + b))

    return snapshots


if __name__ == '__main__':
    snaps = sum_accumulator_early_check(24)
    print("Early check snapshots:", snaps)
