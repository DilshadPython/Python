"""
Comprehensive Unit Test Suite for Advanced Python Function Modules.
Tests variable positional (*args) and keyword (**kwargs) argument handling,
combining positional and keyword inputs, and variadic calculations.
"""

import sys
import unittest
from pathlib import Path

# Add current directory to sys.path for direct module imports
sys.path.insert(0, str(Path(__file__).parent))

from positional_varargs import process_positional_args
from keyword_varargs import process_keyword_args
from combined_args_kwargs import (
    print_args_details,
    print_kwargs_details,
    print_combined_user_details
)
from variadic_sum_subtract import (
    calculate_variadic_sum,
    calculate_variadic_subtraction
)


class TestPositionalVarargs(unittest.TestCase):
    """Test positional variable-length argument (*args) handling."""

    def test_process_positional_args(self):
        heading, args = process_positional_args(2, 9, 3)
        self.assertEqual(heading, 2)
        self.assertEqual(args, (9, 3))

    def test_empty_positional_args(self):
        heading, args = process_positional_args("Test")
        self.assertEqual(heading, "Test")
        self.assertEqual(args, ())


class TestKeywordVarargs(unittest.TestCase):
    """Test keyword variable-length argument (**kwargs) handling."""

    def test_process_keyword_args(self):
        word, kwargs = process_keyword_args(word=8, myword="Hello", keyword_val=27)
        self.assertEqual(word, 8)
        self.assertEqual(kwargs, {"myword": "Hello", "keyword_val": 27})

    def test_empty_keyword_args(self):
        word, kwargs = process_keyword_args(word=100)
        self.assertEqual(word, 100)
        self.assertEqual(kwargs, {})


class TestCombinedArgsKwargs(unittest.TestCase):
    """Test functions accepting both positional (*args) and keyword (**kwargs) arguments."""

    def test_print_args_details(self):
        args = print_args_details('Dilshad', 'Abdulla', 'Developer')
        self.assertEqual(args, ('Dilshad', 'Abdulla', 'Developer'))

    def test_print_kwargs_details(self):
        kwargs = print_kwargs_details(fname='Dilshad', lname='Abdulla', height=175)
        self.assertEqual(kwargs, {'fname': 'Dilshad', 'lname': 'Abdulla', 'height': 175})

    def test_print_combined_user_details(self):
        args, kwargs = print_combined_user_details('Adam', 'Smith', 44, city='Brentwood', country='UK')
        self.assertEqual(args, ('Adam', 'Smith', 44))
        self.assertEqual(kwargs, {'city': 'Brentwood', 'country': 'UK'})


class TestVariadicSumSubtract(unittest.TestCase):
    """Test variadic numeric summation and subtraction operations."""

    def test_calculate_variadic_sum(self):
        self.assertEqual(calculate_variadic_sum(2, 3, 4, 8), 17)
        self.assertEqual(calculate_variadic_sum(11, 24, 83), 118)
        self.assertEqual(calculate_variadic_sum(4, 3, 64, 8, 33, 23, -8), 127)
        self.assertEqual(calculate_variadic_sum(), 0)

    def test_calculate_variadic_subtraction(self):
        self.assertEqual(calculate_variadic_subtraction(22, 3, -4, 8), -29)
        self.assertEqual(calculate_variadic_subtraction(141, 24, 83, -99, -34), -115)
        self.assertEqual(calculate_variadic_subtraction(), 0)


if __name__ == '__main__':
    unittest.main()
