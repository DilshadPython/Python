"""
Comprehensive Unit Test Suite for Python Methods & Function Modules.
Tests dynamic attribute deletion, dict key deletion, factorial calculations,
mean filtering, map transformations, string manipulations, reduce operations,
and Function vs Method object comparisons.
"""

import sys
import unittest
from pathlib import Path

# Add current directory to sys.path for direct module imports
sys.path.insert(0, str(Path(__file__).parent))

from class_attribute_deleter import inspect_and_delete_attribute
from object_vs_dict_deleter import CarProfile, delete_object_attribute, delete_dictionary_key
from factorial_calculator import calculate_factorial
from iterable_filter_mean import filter_numbers_by_mean
from falsy_value_filter import remove_falsy_values
from string_length_calculator import calculate_string_length
from temperature_map_converter import convert_celsius_to_fahrenheit
from string_lowercase_converter import convert_to_lowercase
from circle_area_map_calculator import calculate_circle_area, calculate_areas_for_radii
from random_math_evaluator import generate_random_number, evaluate_math_operations
from functional_reduce_product import calculate_cumulative_product
from string_splitter import split_string
from string_whitespace_stripper import strip_whitespace
from string_uppercase_converter import convert_to_uppercase
from function_vs_method_comparison import (
    standalone_function,
    CalculatorService,
    compare_function_and_method
)


class TestClassAndObjectMethods(unittest.TestCase):
    """Test dynamic attribute and dictionary deletion functions."""

    def test_inspect_and_delete_attribute(self):
        class DummyVehicle:
            name = "Volvo"
            year = 2010

        before, after = inspect_and_delete_attribute(DummyVehicle, 'name')
        self.assertTrue(before)
        self.assertFalse(after)

    def test_object_vs_dict_deleter(self):
        car = CarProfile("Audi", 2005, "A3")
        self.assertTrue(delete_object_attribute(car, "year"))
        self.assertFalse(hasattr(car, "year"))

        car_dict = {"brand": "Volvo", "year": 2010}
        self.assertTrue(delete_dictionary_key(car_dict, "year"))
        self.assertNotIn("year", car_dict)


class TestStringMethods(unittest.TestCase):
    """Test string built-in method wrappers."""

    def test_string_length(self):
        self.assertEqual(calculate_string_length("Python"), 6)

    def test_lowercase_and_uppercase(self):
        self.assertEqual(convert_to_lowercase("PYTHON"), "python")
        self.assertEqual(convert_to_uppercase("python"), "PYTHON")

    def test_string_split(self):
        self.assertEqual(split_string("apple,banana", ","), ["apple", "banana"])

    def test_whitespace_strip(self):
        self.assertEqual(strip_whitespace("  hello  "), "hello")


class TestFunctionalMethods(unittest.TestCase):
    """Test higher-order functional methods (map, filter, reduce, factorial)."""

    def test_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        with self.assertRaises(ValueError):
            calculate_factorial(-5)

    def test_iterable_filter_mean(self):
        data = [2.0, 4.0, 6.0, 8.0, 10.0]
        avg, above, below = filter_numbers_by_mean(data)
        self.assertEqual(avg, 6.0)
        self.assertEqual(above, [8.0, 10.0])
        self.assertEqual(below, [2.0, 4.0])

    def test_falsy_filter(self):
        items = ['Rome', '', False, None, 0, 'Paris']
        self.assertEqual(remove_falsy_values(items), ['Rome', 'Paris'])

    def test_temperature_map(self):
        celsius = [('Moscow', -10.0), ('Cairo', 20.0)]
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        self.assertEqual(fahrenheit, [('Moscow', 14.0), ('Cairo', 68.0)])

    def test_circle_area_map(self):
        radii = [1.0, 2.0]
        areas = calculate_areas_for_radii(radii)
        self.assertAlmostEqual(areas[0], 3.14159, places=4)

    def test_reduce_product(self):
        self.assertEqual(calculate_cumulative_product([2, 3, 4]), 24)
        self.assertEqual(calculate_cumulative_product([]), 0)

    def test_random_math_evaluator(self):
        num = generate_random_number(1, 10)
        self.assertTrue(1 <= num <= 10)
        a, b, c, d, e, f = evaluate_math_operations(10, 2)
        self.assertEqual((a, b, c, d, e, f), (12, 8, 20, 5, 0, 5.0))


class TestFunctionVsMethodComparison(unittest.TestCase):
    """Test comparison between standalone functions and class methods."""

    def test_compare_function_and_method(self):
        self.assertEqual(standalone_function(10, 20), 30)
        service = CalculatorService(100)
        self.assertEqual(service.instance_method(50), 150)
        self.assertEqual(CalculatorService.class_method(50), 100)
        self.assertEqual(CalculatorService.static_method(5), 25)

        comp = compare_function_and_method()
        self.assertEqual(comp["function_analysis"]["type"], "function")
        self.assertEqual(comp["instance_method_analysis"]["type"], "method")
        self.assertTrue(comp["instance_method_analysis"]["self_bound"])


if __name__ == '__main__':
    unittest.main()
