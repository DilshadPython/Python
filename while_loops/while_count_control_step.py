"""
Demonstrates count-controlled while loop with custom start, stop, and step intervals.
"""
from typing import List


def count_control_step(start: int = 1, end: int = 10, step: int = 1) -> List[int]:
    """Execute count-controlled while loop with incremental step values."""
    counter = start
    sequence: List[int] = []
    while counter <= end:
        sequence.append(counter)
        counter += step
    return sequence


if __name__ == '__main__':
    result = count_control_step(1, 10, 2)
    print(f"Step loop (1 to 10 by 2): {result}")
