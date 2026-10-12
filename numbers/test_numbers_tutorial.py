import unittest
from cloud_app.tutorials.number_basics import (
    calculate_power,
    safe_division,
    convert_types
)

class TestNumbersTutorial(unittest.TestCase):
    """Unit test suite for Numbers tutorial module."""

    def test_calculate_power(self):
        self.assertEqual(calculate_power(2, 3), 8)
        self.assertEqual(calculate_power(4, 0.5), 2.0)

    def test_calculate_power_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_power("2", 3)

    def test_safe_division_valid(self):
        self.assertEqual(safe_division(10, 2), 5.0)

    def test_safe_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)

    def test_convert_types(self):
        i_val, f_val = convert_types("42.5")
        self.assertEqual(i_val, 42)
        self.assertEqual(f_val, 42.5)

if __name__ == "__main__":
    unittest.main()
