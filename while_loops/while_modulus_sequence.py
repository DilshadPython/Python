"""
Demonstrates modulus operations and conditional branching inside a while loop.
"""
from typing import List, Tuple


def modulus_sequence(limit: int = 7) -> List[Tuple[int, str]]:
    """Generate sequence analysis of numbers up to modulus limit."""
    a = 1
    records: List[Tuple[int, str]] = []
    while a % limit != 0:
        if a % 2 == 0:
            records.append((a, "EVEN"))
        elif a == 2:
            records.append((a, "TWO"))
        else:
            records.append((a, "ODD"))
        a += 1
    return records


if __name__ == '__main__':
    res = modulus_sequence(7)
    print("Modulus sequence analysis:", res)
