"""
Demonstrates string validation loop with sentinel matching.
"""
from typing import List, Tuple


def validate_username(names: List[str]) -> Tuple[bool, int]:
    """Iterate through candidate names until matching target username 'Dilshad'."""
    attempts = 0
    for name in names:
        attempts += 1
        if name == 'Dilshad':
            return True, attempts
    return False, attempts


if __name__ == '__main__':
    found, count = validate_username(['John', 'Dilshad'])
    print(f"User validation: {found} in {count} attempts.")
