"""
Unit test suite verifying calculator arithmetic functions, zero division checks, and subtests.
"""
# "import module" loads unittest from standard library.
import unittest
# "from module import name" imports calculator arithmetic functions into test scope.
from calculator import add, divide, multiply, power, subtract


class TestCalculator(unittest.TestCase):
    """Test suite covering calculator arithmetic logic and boundary conditions."""

    def test_add(self):
        """Test addition of positive, negative, and floating numbers."""
        self.assertEqual(add(4, 8), 12)
        self.assertEqual(add(-3, 4), 1)
        self.assertEqual(add(-3, -3), -6)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        """Test subtraction logic."""
        self.assertEqual(subtract(4, 2), 2)
        self.assertEqual(subtract(-5, 4), -9)
        self.assertEqual(subtract(-7, -5), -2)

    def test_multiply(self):
        """Test multiplication logic."""
        self.assertEqual(multiply(8, 3), 24)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        """Test division and zero divisor ValueError handling."""
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-12, 3), -4.0)

        # Verify ValueError is raised when dividing by zero using context manager
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertIn("Divisor cannot be zero", str(ctx.exception))

    def test_power_subtests(self):
        """Demonstrate Python 3.4+ self.subTest() for parameterized power testing."""
        cases = [
            (2, 3, 8),
            (5, 0, 1),
            (3, 2, 9),
            (10, -1, 0.1),
        ]
        for base, exp, expected in cases:
            with self.subTest(base=base, exp=exp):
                self.assertEqual(power(base, exp), expected)


if __name__ == '__main__':
    unittest.main()
