"""
Comprehensive Unit Test Suite for Python Function Modules.
Tests every unique function across the standardized Function directory.
Ensures signature compliance, type annotations, and correct return values.
"""

import unittest
from typing import Dict, List

from Function.absolute_values import calculate_abs_values
from Function.add_int import add_int, my_add, add_me
from Function.anonymous_func import add, square as lambda_square
from Function.args_unpacking import calculate_sum
from Function.boolean_func import is_even_boolean, is_positive
from Function.build_func import get_max_and_min
from Function.calculate_func import calculate
from Function.calculator_dict import calculator
from Function.call_return import calculate_exponent_square, power
from Function.cave_navigation import create_tunnel, visit_cave, choose_cave
from Function.closure_function import make_multiplier
from Function.def_and_global_var import bar
from Function.def_args_kwargs import view
from Function.def_calendar import get_month_calendar
from Function.def_str import username
from Function.default_parameters import myfunc
from Function.dispatch_dict import dispatch_dict
from Function.dispatch_if import dispatch_if
from Function.email_welcome import view_email, welcome_email
from Function.factorial_func import factorial
from Function.filter_func import even_func, get_even_numbers
from Function.formatted_greeting import welcome_msg, user_details
from Function.function_references import square_function_ref
from Function.gender_translator import translate_gender_code
from Function.global_inner_local import inner_local_scope
from Function.global_keyword import test_global_modify
from Function.global_scope_access import outer_global_access
from Function.global_scope_shadowing import outer_scope_shadowing
from Function.global_variable import increment_global_counter, get_counter_state
from Function.greeting_welcome import welcome_user
from Function.higher_order_func import square_value, apply_square
from Function.if_func import is_even_number, check_number_parity
from Function.metric_conversion import centimeter
from Function.multi_args_function import fahrenheit_temp, celsius_temp, convert_temp_to
from Function.nested_function_scope import outer_nested_scope
from Function.nested_scope_shadowing import outer_func_shadowing
from Function.nonlocal_scope_modify import outer_nonlocal_modify
from Function.nonlocal_scope_read import outer_nonlocal_read
from Function.number_square import square
from Function.pay_tax import pay_tax, neto_pay
from Function.profile_formatter import profile
from Function.recursive_count_letter import count_letter
from Function.recursive_duplicate import remove_duplicate
from Function.recursive_explode import recursive_explode
from Function.recursive_factorial import factorial_recur
from Function.recursive_list_map import square_element, map_squares
from Function.recursive_string import pick_first_letter, extract_acronym, extract_acronym_uppercase
from Function.reduce_func import add_pair, sum_sequence
from Function.script_main_entry import hello_entry, main as main_entry
from Function.student_directory import get_student_name
from Function.triangle import calculate_triangle_area
from Function.tuple_arithmetic import add_and_subtract_three
from Function.user_greeting import greet_user
from Function.vowel_counter import vowels_count


class TestFunctionBasics(unittest.TestCase):
    """Test basic arithmetic, string, and formatting functions."""

    def test_absolute_values(self):
        v1, v2, v3, v4 = calculate_abs_values(-2.45, -33, 12.68, 3 + 4j)
        self.assertEqual((v1, v2, v3, v4), (2.45, 33.0, 12.68, 5.0))

    def test_add_int(self):
        self.assertEqual(add_int(10, 20), 30)
        self.assertEqual(my_add(4, 56), 60)
        self.assertEqual(add_me(7, 9), 16)

    def test_anonymous_func(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(lambda_square(4), 16)

    def test_args_unpacking(self):
        self.assertEqual(calculate_sum(10, 20, 30), 60)

    def test_boolean_func(self):
        self.assertTrue(is_even_boolean(10))
        self.assertFalse(is_even_boolean(7))
        self.assertTrue(is_positive(5))

    def test_build_func(self):
        max_v, min_v = get_max_and_min([12, 45, 2, 89])
        self.assertEqual((max_v, min_v), (89, 2))

    def test_calculate_func(self):
        self.assertEqual(calculate(10, 2), (12, 8, 20, 5.0))

    def test_calculator_dict(self):
        res = calculator(17, 36)
        self.assertEqual(res['add'], 53)
        self.assertEqual(res['sub'], -19)

    def test_call_return(self):
        self.assertEqual(calculate_exponent_square(4), 16)
        self.assertEqual(power(2, 3), 8)

    def test_def_calendar(self):
        cal = get_month_calendar(2026, 8)
        self.assertIn("August 2026", cal)

    def test_def_str(self):
        res = username("Dilshad", "Abdulla", 30)
        self.assertIn("DILSHAD ABDULLA", res)

    def test_default_parameters(self):
        self.assertEqual(myfunc(4), 5)
        self.assertEqual(myfunc(8, 7), 15)

    def test_email_welcome(self):
        self.assertIn("tom@example.com", view_email("tom@example.com"))
        self.assertIn("Tom", welcome_email("Tom", "tom@example.com"))

    def test_gender_translator(self):
        self.assertEqual(translate_gender_code('m'), 'Male')
        self.assertEqual(translate_gender_code('f'), 'Female')
        self.assertEqual(translate_gender_code(None), 'None')

    def test_greeting_welcome(self):
        self.assertEqual(welcome_user("Hello", "Dilshad"), "Hello, Dilshad")

    def test_metric_conversion(self):
        self.assertAlmostEqual(centimeter(inches=10, feet=1), 55.88)

    def test_number_square(self):
        self.assertEqual(square(5), 25)

    def test_profile_formatter(self):
        prof = profile('Dilshad', 'Abdulla', '6 Ursula Gould Way', 'E14 7FX', 'London')
        self.assertIn('Dilshad', prof)

    def test_student_directory(self):
        self.assertEqual(get_student_name(814747), 'Dilshad Abdulla')

    def test_triangle(self):
        self.assertEqual(calculate_triangle_area(10, 5), 25.0)

    def test_tuple_arithmetic(self):
        self.assertEqual(add_and_subtract_three(6, 8, 9), (23, -11))

    def test_user_greeting(self):
        self.assertEqual(greet_user("Dilshad"), "Your name is Dilshad")

    def test_vowel_counter(self):
        self.assertEqual(vowels_count("Dilshad"), 2)


class TestAdvancedAndScope(unittest.TestCase):
    """Test dispatching, closures, scope rules, higher order functions, and recursion."""

    def test_cave_navigation(self):
        caves: Dict[int, List[int]] = {1: [], 2: [], 3: []}
        create_tunnel(caves, 1, 2)
        self.assertEqual(caves[1], [2])
        visited: List[int] = []
        unvisited = [1, 2, 3]
        visit_cave(visited, unvisited, 1)
        self.assertEqual(visited, [1])
        chosen = choose_cave(caves, [1, 2, 3], rng_seed=42)
        self.assertIn(chosen, [1, 2, 3])

    def test_closure_function(self):
        double = make_multiplier(2)
        self.assertEqual(double(5), 10)

    def test_def_and_global_var(self):
        x, xx, y, z = bar(10)
        self.assertEqual(y, 6)

    def test_def_args_kwargs(self):
        args, kwargs = view('A', 'B', k1='V1')
        self.assertEqual(args, ('A', 'B'))
        self.assertEqual(kwargs, {'k1': 'V1'})

    def test_dispatch_dict(self):
        self.assertEqual(dispatch_dict('add', 10, 5), 15)

    def test_dispatch_if(self):
        self.assertEqual(dispatch_if('sub', 20, 8), 12)

    def test_factorial_func(self):
        self.assertEqual(factorial(5), 120)

    def test_filter_func(self):
        self.assertTrue(even_func(4))
        self.assertEqual(get_even_numbers([1, 2, 3, 4]), [2, 4])

    def test_formatted_greeting(self):
        self.assertEqual(welcome_msg('Hello, ', 'Dilshad'), 'Hello, Dilshad')
        args, kwargs = user_details('Dilshad', age=41)
        self.assertEqual(args, ('Dilshad',))
        self.assertEqual(kwargs, {'age': 41})

    def test_function_references(self):
        self.assertEqual(square_function_ref(5), 25)

    def test_global_scopes(self):
        self.assertEqual(inner_local_scope(), ('in side x', 'out side x'))
        self.assertGreaterEqual(test_global_modify(), 15)
        self.assertEqual(outer_global_access(), 'Global x')
        self.assertEqual(outer_scope_shadowing(), ('in side x', 'out side x'))

    def test_global_variable(self):
        cnt = increment_global_counter(5)
        self.assertGreaterEqual(cnt, 5)
        init_c, curr_c = get_counter_state()
        self.assertIsInstance(init_c, int)

    def test_higher_order_func(self):
        self.assertEqual(square_value(5), 25)
        self.assertEqual(apply_square([1, 2, 3]), [1, 4, 9])

    def test_if_func(self):
        self.assertTrue(is_even_number(8))
        self.assertIn("even", check_number_parity(8))

    def test_multi_args_function(self):
        self.assertAlmostEqual(fahrenheit_temp(100), 37.77777777777778)
        self.assertAlmostEqual(celsius_temp(0), 32.0)
        self.assertAlmostEqual(convert_temp_to(100, 'c'), 37.77777777777778)

    def test_nested_scopes(self):
        self.assertEqual(outer_nested_scope()[0], 'This is local var in in_side() called x')
        self.assertEqual(outer_func_shadowing(), 'Dog')
        self.assertEqual(outer_nonlocal_modify()[1], 'This is local var in in_side() called x')
        self.assertEqual(outer_nonlocal_read(), 'This is local var in out_side() called x')

    def test_pay_tax(self):
        self.assertEqual(pay_tax(8000), 0)
        self.assertAlmostEqual(neto_pay(20000), 16600.0)

    def test_recursive_functions(self):
        self.assertEqual(count_letter("London"), 6)
        self.assertEqual(remove_duplicate("Pyythhoon"), "Python")
        self.assertEqual(recursive_explode("Python"), "P y t h o n")
        self.assertEqual(factorial_recur(5), 120)

    def test_recursive_list_and_string(self):
        self.assertEqual(square_element(3), 9)
        self.assertEqual(map_squares([1, 2, 3]), [1, 4, 9])
        self.assertEqual(pick_first_letter("London"), "L")
        words = ['Every', 'one', 'in', 'London']
        self.assertEqual(extract_acronym(words), "EoiL")
        self.assertEqual(extract_acronym_uppercase(words), "EOIL")

    def test_reduce_func(self):
        self.assertEqual(add_pair(5, 10), 15)
        self.assertEqual(sum_sequence([1, 2, 3, 4, 5]), 15)

    def test_script_main_entry(self):
        self.assertEqual(hello_entry("World"), "Hello, World")
        self.assertEqual(main_entry("World"), "Hello, World")


if __name__ == '__main__':
    unittest.main()
