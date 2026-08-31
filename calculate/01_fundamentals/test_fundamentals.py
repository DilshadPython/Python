"""
Unit Test Suite for Mathematical Calculator Fundamentals Module.

Tests Pythagorean hypotenuse computation, difference of squares calculation,
and 2D Euclidean distance formulas.
"""

import unittest
from math_calculator_basics import (
    compute_difference_of_squares,
    compute_euclidean_distance,
    compute_pythagorean_hypotenuse,
)


class TestMathCalculatorFundamentals(unittest.TestCase):
    """Test cases for core mathematical calculator formulas."""

    def test_compute_pythagorean_hypotenuse(self) -> None:
        """Verify Pythagorean hypotenuse calculation for 3-4-5 right triangle."""
        hyp = compute_pythagorean_hypotenuse(3.0, 4.0)
        self.assertEqual(hyp, 5.0)

        hyp_float = compute_pythagorean_hypotenuse(5.0, 12.0)
        self.assertEqual(hyp_float, 13.0)

    def test_compute_difference_of_squares(self) -> None:
        """Verify difference of squares formula (a^2 - b^2)."""
        diff = compute_difference_of_squares(5.0, 3.0)
        self.assertEqual(diff, 16.0)  # 25 - 9 = 16

        diff_neg = compute_difference_of_squares(3.0, 5.0)
        self.assertEqual(diff_neg, -16.0)

    def test_compute_euclidean_distance(self) -> None:
        """Verify 2D Euclidean distance calculation."""
        dist = compute_euclidean_distance((0.0, 0.0), (3.0, 4.0))
        self.assertEqual(dist, 5.0)

        dist_zero = compute_euclidean_distance((2.5, 2.5), (2.5, 2.5))
        self.assertEqual(dist_zero, 0.0)


if __name__ == "__main__":
    unittest.main()
