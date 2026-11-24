"""Sequence slicing fundamentals demonstration in Python.

This module demonstrates list slicing syntax: `sequence[start:stop:step]`
including positive, negative, and reverse step indexing.
"""

from typing import Sequence, TypeVar

T = TypeVar("T")


def slice_subsequence(seq: Sequence[T], start: int = None, stop: int = None, step: int = None) -> Sequence[T]:
    """Slice any sequence safely using start, stop, and step bounds.

    Args:
        seq: Target sequence (list, tuple, string).
        start: Starting index (inclusive). Defaults to None (sequence start/end).
        stop: Stopping index (exclusive). Defaults to None.
        step: Stride size and direction. Defaults to None (+1).

    Returns:
        Sequence[T]: The extracted slice.
    """
    return seq[start:stop:step]


def demonstrate_slicing_patterns() -> dict[str, list[int]]:
    """Demonstrate common slicing patterns on a 0-10 integer sequence.

    Returns:
        dict[str, list[int]]: Mapping of slice pattern description to result.
    """
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return {
        "range_1_to_8": numbers[1:8],          # [1, 2, 3, 4, 5, 6, 7]
        "every_10th": numbers[::10],           # [0, 10]
        "even_stride_from_2": numbers[2:10:2], # [2, 4, 6, 8]
        "every_3rd_from_0": numbers[0::3],     # [0, 3, 6, 9]
        "reversed": numbers[::-1],             # [10, 9, 8, ..., 0]
        "from_index_4": numbers[4:],           # [4, 5, 6, 7, 8, 9, 10]
        "negative_bounds": numbers[-8:-2],     # [3, 4, 5, 6, 7, 8]
        "negative_step": numbers[-3:2:-2],     # [8, 6, 4]
    }


if __name__ == "__main__":
    patterns = demonstrate_slicing_patterns()
    for description, result in patterns.items():
        print(f"{description:<25} -> {result}")
