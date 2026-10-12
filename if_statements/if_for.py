"""Filtering Iterations in Loops using Conditional 'if' Statements.

Demonstrates placing conditional 'if' statements inside a 'for' loop to selectively
filter or handle specific iterations.

Import Notes:
    - 'from typing import List, Tuple': Imports generic containers from 'typing'
      for function signature return annotation.
"""

from typing import List, Tuple


def filter_numbers_above_threshold(threshold: int, limit: int) -> Tuple[List[int], List[int]]:
    """Partition numbers in range(limit) into numbers above and at-or-below threshold."""
    numbers_above: List[int] = []
    numbers_below_or_equal: List[int] = []

    for item in range(limit):
        if item > threshold:
            numbers_above.append(item)
        else:
            numbers_below_or_equal.append(item)

    return numbers_above, numbers_below_or_equal


def demo_if_for() -> None:
    """Run loop iteration filtering demonstration."""
    midpoint = 5
    upper_bound = 10

    above, below = filter_numbers_above_threshold(midpoint, upper_bound)
    print(f"Range 0..{upper_bound-1} filtered at threshold {midpoint}:")
    print(f"  Above threshold {midpoint}: {above}")
    print(f"  At or below threshold {midpoint}: {below}")


if __name__ == "__main__":
    demo_if_for()
