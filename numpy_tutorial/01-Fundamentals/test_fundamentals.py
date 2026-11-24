"""
Unit Test Suite for NumPy Fundamentals Module.

Tests basic array creation, structural initializers (zeros, ones, eye),
3D tensor creation, metadata inspection, and reshaping capabilities.
"""

from pathlib import Path
import sys
import unittest

# Ensure current folder is in Python search path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

import numpy as np

from array_creation_and_dtypes import create_basic_arrays, create_structural_matrices
from array_shapes_and_dimensions import create_3d_tensor, inspect_array_metadata, reshape_array


class TestNumPyFundamentals(unittest.TestCase):
    """Test cases for NumPy array creation, metadata, and reshaping."""

    def test_create_basic_arrays(self) -> None:
        """Verify 1D, 2D, and tuple-derived array creation."""
        arr1, arr2d, arr_tup = create_basic_arrays()

        self.assertEqual(arr1.shape, (7,))
        self.assertEqual(arr1.ndim, 1)
        self.assertEqual(arr2d.shape, (2, 7))
        self.assertEqual(arr2d.ndim, 2)
        self.assertEqual(arr_tup.shape, (8,))

    def test_create_structural_matrices(self) -> None:
        """Verify matrix initializers (ones, empty, eye)."""
        ones_m, empty_m, eye_m = create_structural_matrices()

        self.assertEqual(ones_m.shape, (10, 10))
        self.assertTrue(np.all(ones_m == 1.0))
        self.assertEqual(empty_m.shape, (8, 8))
        self.assertEqual(eye_m.shape, (5, 5))
        self.assertEqual(np.trace(eye_m), 5.0)

    def test_create_3d_tensor(self) -> None:
        """Verify 3D array tensor creation and properties."""
        tensor = create_3d_tensor()
        self.assertEqual(tensor.ndim, 3)
        self.assertEqual(tensor.shape, (2, 2, 3))
        self.assertEqual(tensor.size, 12)

    def test_inspect_array_metadata(self) -> None:
        """Verify dictionary metadata outputs."""
        tensor = create_3d_tensor()
        meta = inspect_array_metadata(tensor)

        self.assertEqual(meta["ndim"], 3)
        self.assertEqual(meta["shape"], (2, 2, 3))
        self.assertEqual(meta["size"], 12)
        self.assertEqual(meta["dtype"], "int32")

    def test_reshape_array(self) -> None:
        """Verify matrix reshaping logic."""
        flat = np.arange(12)
        reshaped = reshape_array(flat, (3, 4))

        self.assertEqual(reshaped.shape, (3, 4))
        self.assertEqual(reshaped[0, 0], 0)
        self.assertEqual(reshaped[2, 3], 11)


if __name__ == "__main__":
    unittest.main()
