"""
Demonstrates while loop validating modulus divisibility conditions.
"""
from typing import List, Optional, Tuple


def find_divisible_by_seven(inputs: List[int]) -> Tuple[Optional[int], int]:
    """Find the first input number that is divisible by 7 without remainder."""
    attempts = 0
    for val in inputs:
        attempts += 1
        if val % 7 == 0:
            return val, attempts
    return None, attempts


if __name__ == '__main__':
    matched, attempts = find_divisible_by_seven([10, 15, 49])
    print(f"Found divisible number {matched} in {attempts} attempts.")
