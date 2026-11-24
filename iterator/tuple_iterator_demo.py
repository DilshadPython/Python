"""
Tuple Iterator Demonstration Module.

This module demonstrates tuple_iterator mechanics over nested tuple structures.
"""
# "from typing import Tuple, List, Any" imports typing annotations.
from typing import Tuple, List, Any


def iterate_tuple_elements(data_tuple: Tuple[Any, ...]) -> List[Any]:
    """
    Traverse tuple elements using built-in iter() and next().

    Args:
        data_tuple (Tuple[Any, ...]): Nested tuple sequence.

    Returns:
        List[Any]: Extracted tuple elements.
    """
    tuple_iter = iter(data_tuple)
    extracted: List[Any] = []

    while True:
        try:
            extracted.append(next(tuple_iter))
        except StopIteration:
            break

    return extracted


if __name__ == "__main__":
    print("=== Tuple Iterator Demonstration ===")
    points_tuple = ((21, 6), (7, 12), (22, 31), (44, 22))
    print("Looping over tuple:")
    for pt in points_tuple:
        print(f"  Point: {pt}")

    print("\nManual next() iteration over tuple_iterator:")
    extracted_pts = iterate_tuple_elements(points_tuple)
    print(f"Extracted points list: {extracted_pts}")
