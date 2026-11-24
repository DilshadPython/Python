"""Unit tests for Python slicing module.

Verifies sequence slicing patterns, boundary conditions, negative strides,
and URL string slicing.
"""

import unittest

from slicing.example import slice_subsequence, demonstrate_slicing_patterns
from slicing.url_slicing import demonstrate_url_slicing


class TestSlicingTutorial(unittest.TestCase):
    """Test suite covering sequence slicing operations."""

    def test_demonstrate_slicing_patterns(self):
        """Verify list slicing patterns against expected integer sequences."""
        patterns = demonstrate_slicing_patterns()
        self.assertEqual(patterns["range_1_to_8"], [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(patterns["every_10th"], [0, 10])
        self.assertEqual(patterns["even_stride_from_2"], [2, 4, 6, 8])
        self.assertEqual(patterns["every_3rd_from_0"], [0, 3, 6, 9])
        self.assertEqual(patterns["reversed"], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(patterns["from_index_4"], [4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(patterns["negative_bounds"], [3, 4, 5, 6, 7, 8])
        self.assertEqual(patterns["negative_step"], [8, 6, 4])

    def test_slice_subsequence_generic(self):
        """Verify generic slice helper on lists and strings."""
        nums = [10, 20, 30, 40, 50]
        self.assertEqual(slice_subsequence(nums, 1, 4), [20, 30, 40])
        self.assertEqual(slice_subsequence(nums, step=-1), [50, 40, 30, 20, 10])

        text = "Python"
        self.assertEqual(slice_subsequence(text, 0, 2), "Py")
        self.assertEqual(slice_subsequence(text, step=-1), "nohtyP")

    def test_url_slicing_demonstration(self):
        """Verify URL string slicing extraction."""
        url = "http://www.python.org/"
        results = demonstrate_url_slicing(url)
        self.assertEqual(results["original_url"], url)
        self.assertEqual(results["tld_extension"], ".org/")
        self.assertEqual(results["domain_name"], "python.org")


if __name__ == "__main__":
    unittest.main()
