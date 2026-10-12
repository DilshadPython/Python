"""
NumPy Array Creation and Data Types Module.

This module demonstrates fundamental NumPy array creation functions:
- np.array: Convert lists, tuples, or nested sequences to ndarrays.
- np.zeros / np.ones: Initialize arrays filled with 0s or 1s.
- np.empty: Allocate uninitialized array buffers.
- np.eye: Create identity matrices.
- Data types (dtype) and scalar handling.
"""

# Import numpy for high-performance numerical array operations
import numpy as np


def create_basic_arrays() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Demonstrate basic array creation from lists, tuples, and sets.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Created 1D and 2D arrays.
    """
    # Create 1D array from integer list
    number_list: list[int] = [22, 17, 9, 18, 33, 81, 50]
    first_array: np.ndarray = np.array(number_list, dtype=np.int64)

    # Create 2D array (matrix) from list of lists
    second_list: list[int] = [21, 19, 4, 30, 66, 6, 17]
    combined_list: list[list[int]] = [number_list, second_list]
    two_dim_array: np.ndarray = np.array(combined_list, dtype=np.int64)

    # Create 1D array from tuple sequence
    tuple_sequence: tuple[int, ...] = (17, 9, 76, 1, 2, 3, 4, 17)
    tuple_array: np.ndarray = np.array(tuple_sequence)

    return first_array, two_dim_array, tuple_array


def create_structural_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Demonstrate structural matrix initializers: ones, empty, and eye.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Matrices created with initializer functions.
    """
    # 10x10 Matrix of Floating Point Ones
    ones_matrix: np.ndarray = np.ones((10, 10), dtype=np.float64)

    # Uninitialized 8x8 Matrix
    empty_matrix: np.ndarray = np.empty((8, 8), dtype=np.float64)

    # 5x5 Identity Matrix with 1.0 along the main diagonal
    identity_matrix: np.ndarray = np.eye(5, dtype=np.float64)

    return ones_matrix, empty_matrix, identity_matrix


if __name__ == "__main__":
    arr1, arr2d, arr_tup = create_basic_arrays()
    print("--- 1D Array ---")
    print("Content:", arr1)
    print("Shape:", arr1.shape, "Dtype:", arr1.dtype)

    print("\n--- 2D Array ---")
    print("Content:\n", arr2d)
    print("Shape:", arr2d.shape, "Dtype:", arr2d.dtype)

    ones_m, empty_m, eye_m = create_structural_matrices()
    print("\n--- 5x5 Identity Matrix ---")
    print(eye_m)
