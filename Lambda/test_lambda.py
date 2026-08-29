"""
Comprehensive Unit Test Suite for Python Lambda Expression Modules.
Tests lambda operations including arithmetic, string formatting, last-name sorting,
division by zero handling, exponentiation, and dictionary dispatch table calculations.
"""

import sys
import unittest
from pathlib import Path

# Add current directory to sys.path for direct module imports
sys.path.insert(0, str(Path(__file__).parent))

from lambda_name_formatter import format_full_name, sort_names_by_last_name
from lambda_addition import add_eight, add_two_numbers, calculate_addition
from lambda_division import divide_by_eight, divide_two_numbers, calculate_division
from lambda_multiplication import multiply_by_82, multiply_two_numbers, calculate_multiplication
from lambda_exponentiation import power_of_nine, power_base_exp, calculate_power
from lambda_remainder import remainder_by_eight, remainder_two_integers, calculate_remainder
from lambda_string_concat import append_surname, format_full_name_string, build_full_name
from lambda_subtraction import subtract_eight, subtract_two_numbers, calculate_subtraction
from lambda_calculator_dispatch import CALCULATOR_OPS, calculate_operation


class TestLambdaStringOperations(unittest.TestCase):
    """Test lambda functions for string formatting and sequence sorting."""

    def test_format_full_name(self):
        self.assertEqual(format_full_name(" john", "  smith"), "John Smith")

    def test_sort_names_by_last_name(self):
        names = ['John Smith', 'Nicholas Herriot', 'Paulo Maldini']
        sorted_names = sort_names_by_last_name(names)
        self.assertEqual(sorted_names, ['Nicholas Herriot', 'Paulo Maldini', 'John Smith'])

    def test_string_concat(self):
        self.assertEqual(append_surname("John"), "John Smith")
        self.assertEqual(format_full_name_string("  john "), "John Smith")
        self.assertEqual(build_full_name("john"), "John Smith")


class TestLambdaArithmeticOperations(unittest.TestCase):
    """Test lambda functions for arithmetic operations."""

    def test_addition(self):
        self.assertEqual(add_eight(10), 18)
        self.assertEqual(add_two_numbers(9, 77), 86)
        self.assertEqual(calculate_addition(10), 18)

    def test_division(self):
        self.assertEqual(divide_by_eight(64), 8.0)
        self.assertEqual(divide_two_numbers(20, 4), 5.0)
        self.assertTrue(sys.float_info.min > 0)
        self.assertTrue(str(divide_two_numbers(10, 0)) == 'nan')
        self.assertEqual(calculate_division(64), 8.0)

    def test_multiplication(self):
        self.assertEqual(multiply_by_82(5), 410)
        self.assertEqual(multiply_two_numbers(7, 9), 63)
        self.assertEqual(calculate_multiplication(5), 410)

    def test_exponentiation(self):
        self.assertEqual(power_of_nine(2), 512)
        self.assertEqual(power_base_exp(3, 4), 81)
        self.assertEqual(calculate_power(2), 512)

    def test_remainder(self):
        self.assertEqual(remainder_by_eight(19), 3)
        self.assertEqual(remainder_two_integers(25, 7), 4)
        self.assertEqual(remainder_two_integers(10, 0), 0)
        self.assertEqual(calculate_remainder(19), 3)

    def test_subtraction(self):
        self.assertEqual(subtract_eight(20), 12)
        self.assertEqual(subtract_two_numbers(100, 45), 55)
        self.assertEqual(calculate_subtraction(20), 12)


class TestLambdaDispatchTable(unittest.TestCase):
    """Test calculator dictionary dispatch table backed by lambda functions."""

    def test_calculate_operation(self):
        self.assertEqual(calculate_operation(7, 9, '+'), 16)
        self.assertEqual(calculate_operation(7, 9, '-'), -2)
        self.assertEqual(calculate_operation(20, 4, '/'), 5.0)
        self.assertEqual(calculate_operation(7, 9, '%'), 7)
        self.assertEqual(calculate_operation(7, 9, '*'), 63)
        self.assertEqual(calculate_operation(2, 3, '**'), 8)

    def test_invalid_operator(self):
        with self.assertRaises(KeyError):
            calculate_operation(10, 5, '^')


if __name__ == '__main__':
    unittest.main()
