"""
NumPy Array Indexing, Slicing, and Boolean Masking Module.

This module demonstrates:
- Basic 1D and 2D slicing (sub-arrays, specific row/column extraction).
- Fancy indexing using integer arrays.
- Boolean masking and conditional selection.
- In-place mutation via slice assignment.
"""

# Import numpy for high-performance array indexing and slicing operations
import numpy as np


def extract_specific_row_and_column() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Demonstrate row and column extraction from a 2D matrix.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]:
            - Extract third column from all rows.
            - Extract first row completely.
            - Extract third row up to index 3.
    """
    matrix = np.array([
        ["a", "b", "c", "d", "e"],
        ["ab", "cd", "ef", "gh", "ij"],
        ["kl", "mn", "op", "qr", "st"]
    ])

    third_column: np.ndarray = matrix[:, 2]      # ['c', 'ef', 'op']
    first_row: np.ndarray = matrix[0, :]          # ['a', 'b', 'c', 'd', 'e']
    partial_row: np.ndarray = matrix[2, :3]       # ['kl', 'mn', 'op']

    return third_column, first_row, partial_row


def mutate_slice_in_place(arr: np.ndarray, start_idx: int, end_idx: int, fill_value: int) -> np.ndarray:
    """Mutate a slice of an array in place with a given fill value.

    Args:
        arr (np.ndarray): Target array to mutate.
        start_idx (int): Inclusive start slice index.
        end_idx (int): Exclusive end slice index.
        fill_value (int): Scalar value to assign to the slice.

    Returns:
        np.ndarray: The mutated array.
    """
    mutated = arr.copy()
    mutated[start_idx:end_idx] = fill_value
    return mutated


def perform_fancy_indexing_and_masking(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Perform fancy integer indexing and boolean condition masking.

    Args:
        arr (np.ndarray): 1D input array.

    Returns:
        tuple[np.ndarray, np.ndarray]:
            - Fancy indexed elements at specific index list.
            - Boolean masked elements matching condition (> threshold).
    """
    indices = [0, 2, 4]
    fancy_selected: np.ndarray = arr[indices]

    # Boolean condition mask (elements greater than mean value)
    mean_val = np.mean(arr)
    masked_selected: np.ndarray = arr[arr > mean_val]

    return fancy_selected, masked_selected


if __name__ == "__main__":
    col, row, part = extract_specific_row_and_column()
    print("--- 2D Slicing Demo ---")
    print("Third Column:", col)
    print("First Row:   ", row)
    print("Partial Row: ", part)

    nums = np.arange(20, 40)
    print("\n--- Original Array ---")
    print(nums)

    mutated = mutate_slice_in_place(nums, 6, 11, 70)
    print("\n--- Mutated Array (Slice [6:11] = 70) ---")
    print(mutated)

    fancy, mask = perform_fancy_indexing_and_masking(nums)
    print("\n--- Fancy Indexing ---", fancy)
    print("--- Boolean Masking (> mean) ---", mask)
