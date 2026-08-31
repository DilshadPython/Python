"""
Demonstrates input validation loop checking exit trigger conditions.
"""
from typing import List, Tuple


def validate_exit_number(inputs: List[int]) -> Tuple[bool, int]:
    """Iterate through inputs until exit trigger (1) is encountered."""
    attempts = 0
    for num in inputs:
        attempts += 1
        if num == 1:
            return True, attempts
    return False, attempts


if __name__ == '__main__':
    success, tries = validate_exit_number([5, 8, 1])
    print(f"Exit validation: {success} in {tries} tries.")
