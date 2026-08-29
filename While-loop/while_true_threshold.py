"""
Demonstrates while True loop validating threshold condition >= 10.
"""
from typing import List, Tuple


def validate_threshold(inputs: List[int], threshold: int = 10) -> Tuple[int, int]:
    """Process numbers until encountering value greater than or equal to threshold."""
    attempts = 0
    for num in inputs:
        attempts += 1
        if num >= threshold:
            return num, attempts
    return -1, attempts


if __name__ == '__main__':
    val, tries = validate_threshold([3, 7, 12, 5])
    print(f"Threshold reached with value {val} on try {tries}")
