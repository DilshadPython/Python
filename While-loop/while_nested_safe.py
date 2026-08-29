"""
Demonstrates nested while loops and safe iteration boundaries to prevent infinite loops.
"""
from typing import List


def nested_while_safe(max_outer: int = 3, max_inner: int = 3) -> List[int]:
    """Execute bounded nested while loop preventing infinite loop condition."""
    outer = 0
    execution_counter = 0

    while outer < max_outer:
        inner = 0
        while inner < max_inner:
            execution_counter += 1
            inner += 1
        outer += 1

    return [execution_counter]


if __name__ == '__main__':
    cnt = nested_while_safe(3, 3)
    print(f"Total safe nested iterations executed: {cnt[0]}")
