"""
Unit Test Suite for NumPy Advanced Math and Operators Module.

Tests indexing, slicing, boolean masking, universal functions (ufuncs),
matrix transposition, dot products, matrix multiplication (@), string arrays, and I/O.
"""

from pathlib import Path
import sys
import unittest

# Ensure current folder is in Python search path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

import numpy as np

from array_math_and_ufuncs import (
    apply_binary_ufuncs,
    apply_unary_ufuncs,
    compute_matrix_transposition_and_dot,
)
from indexing_slicing_and_masking import (
    extract_specific_row_and_column,
    mutate_slice_in_place,
    perform_fancy_indexing_and_masking,
)
from string_arrays_and_io import (
    demonstrate_string_array_operations,
    save_and_load_binary_array,
    save_and_load_text_matrix,
)


class TestNumPyAdvancedOperations(unittest.TestCase):
    """Test cases for indexing, vector math, matrix operations, and I/O."""

    def test_extract_specific_row_and_column(self) -> None:
        """Verify row and column extraction from 2D character matrix."""
        col, row, part = extract_specific_row_and_column()
        self.assertEqual(list(col), ["c", "ef", "op"])
        self.assertEqual(list(row), ["a", "b", "c", "d", "e"])
        self.assertEqual(list(part), ["kl", "mn", "op"])

    def test_mutate_slice_in_place(self) -> None:
        """Verify slice mutation in array copy."""
        arr = np.arange(20)
        mutated = mutate_slice_in_place(arr, 5, 10, 99)
        self.assertEqual(list(mutated[5:10]), [99, 99, 99, 99, 99])
        self.assertEqual(arr[5], 5)  # Ensure original untouched

    def test_fancy_indexing_and_masking(self) -> None:
        """Verify fancy indexing and boolean masking."""
        arr = np.array([10, 20, 30, 40, 50])
        fancy, mask = perform_fancy_indexing_and_masking(arr)
        self.assertEqual(list(fancy), [10, 30, 50])
        self.assertEqual(list(mask), [40, 50])  # Elements > mean (30)

    def test_apply_unary_ufuncs(self) -> None:
        """Verify square root and exponential ufuncs."""
        arr = np.array([4.0, 9.0, 16.0])
        sqrt_res, exp_res = apply_unary_ufuncs(arr)
        self.assertTrue(np.allclose(sqrt_res, [2.0, 3.0, 4.0]))
        self.assertTrue(np.allclose(exp_res, np.exp([4.0, 9.0, 16.0])))

    def test_apply_binary_ufuncs(self) -> None:
        """Verify binary addition, maximum, and minimum ufuncs."""
        x = np.array([1, 5, 10])
        y = np.array([2, 3, 8])
        sum_res, max_res, min_res = apply_binary_ufuncs(x, y)
        self.assertEqual(list(sum_res), [3, 8, 18])
        self.assertEqual(list(max_res), [2, 5, 10])
        self.assertEqual(list(min_res), [1, 3, 8])

    def test_compute_matrix_transposition_and_dot(self) -> None:
        """Verify matrix transposition, dot product, and matrix operator @."""
        mat = np.arange(6).reshape((2, 3))
        trans, dot_prod, mat_mul = compute_matrix_transposition_and_dot(mat)

        self.assertEqual(trans.shape, (3, 2))
        self.assertEqual(dot_prod.shape, (3, 3))
        self.assertTrue(np.array_equal(dot_prod, mat_mul))

    def test_string_array_operations(self) -> None:
        """Verify vectorized string operations."""
        up, rep, contains = demonstrate_string_array_operations()
        self.assertEqual(up[0], "TOYOTA")
        self.assertEqual(rep[0], "T0y0ta")
        self.assertTrue(contains[2])  # "Ford" at index 2

    def test_binary_and_text_io(self) -> None:
        """Verify binary .npy and text matrix persistence."""
        temp_file_bin = Path("test_temp_bin.npy")
        temp_file_txt = Path("test_temp_txt.csv")

        arr = np.array([1, 2, 3, 4])
        mat = np.eye(3)

        try:
            loaded_bin = save_and_load_binary_array(arr, temp_file_bin)
            loaded_txt = save_and_load_text_matrix(mat, temp_file_txt)

            self.assertTrue(np.array_equal(arr, loaded_bin))
            self.assertTrue(np.allclose(mat, loaded_txt))
        finally:
            temp_file_bin.unlink(missing_ok=True)
            temp_file_txt.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
