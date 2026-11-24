"""
tests/test_lambda_tutorial.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unit test suite for the Lambda Functions tutorial module (cloud_app/tutorials/lambda_basics.py).
"""

# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import math: Standard library module for NaN floating point checks (math.isnan).
# - import unittest: Standard Python unit testing framework.
# - from cloud_app.tutorials.lambda_basics import ...: Importing target functions under test.
# =========================================================================
import math
import unittest
from cloud_app.tutorials.lambda_basics import (
    add_eight,
    add_two_numbers,
    subtract_eight,
    subtract_two_numbers,
    multiply_by_82,
    multiply_two_numbers,
    divide_by_eight,
    divide_two_numbers,
    power_of_nine,
    power_base_exp,
    remainder_by_eight,
    remainder_two_integers,
    format_full_name_string,
    format_full_name,
    sort_names_by_last_name,
    calculate_dispatch,
    filter_even_numbers,
    map_square_numbers,
    reduce_product_numbers,
    inspect_lambda_attributes_and_methods,
    demonstrate_arithmetic_lambdas,
    demonstrate_string_lambdas,
    demonstrate_dispatch_and_higher_order,
)


class TestLambdaTutorial(unittest.TestCase):
    """Test suite covering arithmetic lambdas, string transformations, key sorting, dispatch tables, and higher-order functions."""

    def test_arithmetic_addition_and_subtraction(self):
        """Verify addition and subtraction lambda expressions."""
        self.assertEqual(add_eight(10), 18)
        self.assertEqual(add_two_numbers(7, 13), 20)
        self.assertEqual(subtract_eight(20), 12)
        self.assertEqual(subtract_two_numbers(50, 18), 32)

    def test_arithmetic_multiplication_and_division(self):
        """Verify multiplication and division lambdas including zero-division guard."""
        self.assertEqual(multiply_by_82(3), 246)
        self.assertEqual(multiply_two_numbers(6, 7), 42)
        self.assertEqual(divide_by_eight(64), 8.0)
        self.assertEqual(divide_two_numbers(50, 5), 10.0)

        # Division by zero edge case (returns float('nan'))
        result_nan = divide_two_numbers(10, 0)
        self.assertTrue(math.isnan(result_nan))

    def test_arithmetic_exponentiation_and_remainder(self):
        """Verify exponentiation and modulus remainder lambdas."""
        self.assertEqual(power_of_nine(2), 512)
        self.assertEqual(power_base_exp(3, 4), 81)
        self.assertEqual(remainder_by_eight(29), 5)
        self.assertEqual(remainder_two_integers(43, 6), 1)
        self.assertEqual(remainder_two_integers(10, 0), 0)

    def test_string_formatting_and_sorting(self):
        """Verify string formatting lambdas and key=lambda sorting logic."""
        self.assertEqual(format_full_name_string("  john "), "John Smith")
        self.assertEqual(format_full_name("  dilshad ", "  python "), "Dilshad Python")

        names = ["Guido van Rossum", "Ada Lovelace", "Linus Torvalds", "Grace Hopper"]
        sorted_names = sort_names_by_last_name(names)
        self.assertEqual(sorted_names, ["Grace Hopper", "Ada Lovelace", "Guido van Rossum", "Linus Torvalds"])

        with self.assertRaises(TypeError):
            sort_names_by_last_name("Not a list")  # type: ignore

    def test_calculator_dispatch_table(self):
        """Verify dictionary dispatch table arithmetic execution."""
        self.assertEqual(calculate_dispatch("+", 10, 20), 30)
        self.assertEqual(calculate_dispatch("-", 50, 15), 35)
        self.assertEqual(calculate_dispatch("*", 6, 7), 42)
        self.assertEqual(calculate_dispatch("/", 81, 9), 9.0)
        self.assertEqual(calculate_dispatch("**", 2, 5), 32)
        self.assertEqual(calculate_dispatch("%", 29, 4), 1)

        with self.assertRaises(ValueError):
            calculate_dispatch("invalid_op", 5, 5)

    def test_higher_order_map_filter_reduce(self):
        """Verify map(), filter(), and functools.reduce() lambda functional pipelines."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(filter_even_numbers(nums), [2, 4, 6, 8, 10])
        self.assertEqual(map_square_numbers([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])
        self.assertEqual(reduce_product_numbers([1, 2, 3, 4, 5]), 120)

        with self.assertRaises(TypeError):
            filter_even_numbers(12345)  # type: ignore

        with self.assertRaises(TypeError):
            map_square_numbers(12345)  # type: ignore

        with self.assertRaises(TypeError):
            reduce_product_numbers(12345)  # type: ignore

        with self.assertRaises(ValueError):
            reduce_product_numbers([])

    def test_inspect_lambda_attributes_and_methods(self):
        """Verify lambda reflection attributes and dir() dunder methods."""
        info = inspect_lambda_attributes_and_methods()
        self.assertIn("dir_attributes", info)
        self.assertIn("reflection_attrs", info)
        self.assertTrue(info["is_anonymous"])
        self.assertEqual(info["reflection_attrs"]["__name__"], "<lambda>")
        self.assertIn("__call__", info["dir_attributes"])
        self.assertIn("__get__", info["dir_attributes"])

    def test_demonstration_helpers(self):
        """Verify execution of demonstration helper functions."""
        arith_demo = demonstrate_arithmetic_lambdas()
        self.assertIn("add_eight(12)", arith_demo)
        self.assertEqual(arith_demo["add_eight(12)"], 20)

        str_demo = demonstrate_string_lambdas()
        self.assertIn("sorted_by_last_name", str_demo)

        dispatch_demo = demonstrate_dispatch_and_higher_order()
        self.assertIn("filtered_evens", dispatch_demo)
        self.assertEqual(dispatch_demo["reduced_product"], 120)


if __name__ == "__main__":
    unittest.main()
