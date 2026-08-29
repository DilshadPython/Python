"""
Demonstrates while True loop with numeric sentinel (-1) break to calculate averages.
"""
from typing import List, Tuple


def accumulate_until_sentinel(inputs: List[float], sentinel: float = -1.0) -> Tuple[float, int, float]:
    """Accumulate float values until sentinel is encountered, returning total, count, and average."""
    total = 0.0
    count = 0

    for num in inputs:
        if num == sentinel:
            break
        total += num
        count += 1

    average = total / count if count > 0 else 0.0
    return total, count, average


if __name__ == '__main__':
    tot, cnt, avg = accumulate_until_sentinel([10.0, 20.0, 30.0, -1.0])
    print(f"Total: {tot}, Count: {cnt}, Average: {avg}")
