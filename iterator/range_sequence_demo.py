"""
Range Sequence Iterator Demonstration Module.

This module demonstrates creating range sequence iterators and fetching elements with next().
"""
# "from typing import List" imports type hint annotations.
from typing import List


def iterate_range_elements(start: int, stop: int, count: int) -> List[int]:
    """
    Extract first 'count' elements from range(start, stop) using iter() and next().

    Args:
        start (int): Start integer.
        stop (int): Stop integer.
        count (int): Number of elements to extract.

    Returns:
        List[int]: Extracted elements.
    """
    r_iter = iter(range(start, stop))
    extracted: List[int] = []

    for _ in range(count):
        try:
            extracted.append(next(r_iter))
        except StopIteration:
            break

    return extracted


if __name__ == "__main__":
    print("=== Range Sequence Iterator Demonstration ===")
    sample_range_items = iterate_range_elements(1, 11, 3)
    print(f"First 3 elements of range(1, 11): {sample_range_items}")
