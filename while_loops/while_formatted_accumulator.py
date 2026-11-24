"""
Demonstrates string formatting within while loop state tracking.
"""
from typing import List


def formatted_accumulator(target: int = 24) -> List[str]:
    """Generate formatted state strings for each accumulation iteration."""
    keep_going = True
    a = 0
    b = 0
    messages: List[str] = []

    while keep_going:
        if a + b > target:
            keep_going = False
            break
        a += 5
        b += 7
        messages.append(f"First add a = {a} and b = {b}: total = {a + b}")

    return messages


if __name__ == '__main__':
    msgs = formatted_accumulator(24)
    for m in msgs:
        print(m)
