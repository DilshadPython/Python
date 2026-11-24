"""
Unit test suite for geometry_circles module verifying circle area calculations,
floating point accuracy with assertAlmostEqual, and exception handling.
"""
# "import module" loads math and unittest modules into global test scope.
import math
import unittest

# "from module import name" imports circle_area function directly into local scope.
from geometry_circles import circle_area


class TestCircleArea(unittest.TestCase):
    """Test suite verifying circle area calculation accuracy and edge cases."""

    def test_area(self):
        """Test circle areas with non-negative real numbers."""
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0.0)
        self.assertAlmostEqual(circle_area(2.1), math.pi * (2.1 ** 2))

    def test_negative_radius_value_error(self):
        """Verify ValueError is raised when radius is less than zero."""
        with self.assertRaises(ValueError) as ctx:
            circle_area(-2)
        self.assertIn("cannot be negative", str(ctx.exception))

    def test_invalid_types_type_error(self):
        """Verify TypeError is raised when radius is non-numeric or boolean."""
        invalid_inputs = [3 + 5j, True, False, 'radius', [2.5], None]
        for item in invalid_inputs:
            with self.subTest(item=item):
                self.assertRaises(TypeError, circle_area, item)


if __name__ == '__main__':
    unittest.main()
