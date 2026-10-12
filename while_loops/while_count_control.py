"""
Demonstrates basic count-controlled while loop iteration in Python.
"""
from typing import List


def count_control(limit: int = 4) -> List[int]:
    """Execute a count-controlled while loop up to specified limit."""
    count = 0
    results: List[int] = []
    while count <= limit:
        results.append(count)
        count += 1
    return results


if __name__ == '__main__':
    res = count_control(4)
    print("Count-controlled loop results:", res)
