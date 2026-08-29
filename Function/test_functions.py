"""
Comprehensive Unit Test Suite for Python Function Modules.
Tests basic function definitions, argument parsing (*args, **kwargs),
lambda expressions, higher-order functions, scope rules (LEGB/nonlocal/global),
dispatch patterns, closures, recursion, and utility functions.
Tests both descriptive PEP 8 modules and backward-compatibility wrapper aliases.
"""

# "import module" imports the standard library "unittest" module into local scope.
import importlib
import unittest

# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Dict, List

# Imports from core Function modules using explicit namespace binding
from Function.add_int import add_int, my_add, add_me
from Function.anonymous_func import add, square as lambda_square
from Function.args_unpacking import calculate_sum
from Function.boolean_func import is_even, is_positive
from Function.boolian_func import is_even as boolian_is_even  # Spelling alias
from Function.build_func import get_max_and_min
from Function.calculate_func import calculate
from Function.calclute_dunc import calculate as alias_calculate  # Spelling alias
from Function.call_return import square as call_return_square, power
from Function.closure_function import make_multiplier
from Function.clouser_function import make_multiplier as alias_make_multiplier  # Spelling alias
from Function.def_and_global_var import bar as def_global_bar
from Function.def_args_kwargs import view
from Function.basic_calculator import calculator as basic_calculator
from Function.def_cal import calculator as def_cal_calculator  # Alias
from Function.def_calendar import get_month_calendar
from Function.def_calander import get_month_calendar as alias_get_month_calendar  # Spelling alias
from Function.def_str import username
from Function.student_directory import get_student_name
from Function.dict_id import get_student_name as dict_id_get_student_name  # Alias
from Function.dispatch_dict import dispatch_dict
from Function.dispatch_if import dispatch_if
from Function.number_square import square as number_square
from Function.example_1 import square as example1_square  # Alias
from Function.vowel_counter import vowels_count
from Function.example_2 import vowels_count as example2_vowels_count  # Alias
from Function.factorial_func import factorial
from Function.filter_func import even_func, get_even_numbers
from Function.cave_navigation import create_tunnel, visit_cave, choose_cave
from Function.func import create_tunnel as alias_create_tunnel  # Alias
from Function.gender_translator import get_gender as func1_get_gender
from Function.func_1 import get_gender as alias_func1_get_gender  # Alias
from Function.gender_mapping import get_gender as func2_get_gender
from Function.func_2 import get_gender as alias_func2_get_gender  # Alias
from Function.profile_formatter import profile
from Function.func_3 import profile as alias_profile  # Alias
from Function.user_greeting import greet_user
from Function.func_4 import greet_user as alias_greet_user  # Alias
from Function.calculator_dict import calculator as func5_calculator
from Function.func_5 import calculator as alias_func5_calculator  # Alias
from Function.tuple_arithmetic import add_and_subtract_three
from Function.func_6 import add_and_subtract_three as alias_add_subtract_three  # Alias
from Function.absolute_values import calculate_abs_values
from Function.func_abs import calculate_abs_values as alias_calculate_abs_values  # Alias
from Function.nested_scope_shadowing import outer_func as outer_func_nested
from Function.func_call_itself import outer_func as alias_outer_func_nested  # Alias
from Function.formatted_greeting import welcome_msg, user_details
from Function.func_format import welcome_msg as alias_welcome_msg  # Alias
from Function.greeting_welcome import welcome as welcome_two_args
from Function.func_two_args import welcome as alias_welcome_two_args  # Alias
from Function.email_welcome import view_email, welcome as welcome_with_email
from Function.func_with_argument import welcome as alias_welcome_with_email  # Alias
from Function.global_keyword import test_global_modify
from Function.global_scope_shadowing import out_side as global_1_out_side
from Function.global_1 import out_side as alias_global_1_out_side  # Alias
from Function.global_scope_access import out_side as global_2_out_side
from Function.global_2 import out_side as alias_global_2_out_side  # Alias
from Function.global_inner_local import out_side as global_kw_out_side
from Function.global_kw import out_side as alias_global_kw_out_side  # Alias
from Function.global_variable import increment_global_counter, get_counter_state
from Function.global_varaible import increment_global_counter as alias_inc_counter, get_counter_state as alias_get_counter_state  # Spelling alias
from Function.higher_order_func import apply_square, square as higher_order_square
from Function.if_func import is_even as if_func_is_even, check_number_parity
from Function.nested_function_scope import out_side as in_out_out_side
from Function.in_out_func import out_side as alias_in_out_out_side  # Alias
from Function.default_parameters import myfunc
from Function.info import myfunc as alias_myfunc  # Alias
from Function.metric_conversion import centimeter
from Function.kwargs_func import centimeter as alias_centimeter  # Alias
from Function.nonlocal_scope_read import out_side as local_var_out_side
from Function.local_var import out_side as alias_local_var_out_side  # Alias
from Function.script_main_entry import hello as main_hello, main as main_func
from Function.main import main as alias_main_func  # Alias
from Function.greeting_handler import hello as main1_hello, main as main1_main
from Function.main_1 import main as alias_main1_main  # Alias
from Function.multi_args_function import convert_temp_to, fahrenheit_temp, celsius_temp
from Function.nonlocal_scope_modify import out_side as nonlocal_out_side
from Function.no_local import out_side as alias_nonlocal_out_side  # Alias
from Function.pay_tax import pay_tax, neto_pay
from Function.recursive_count_letter import count_letter
from Function.recursive_duplicate import remove_duplicate
from Function.recursive_duplecate import remove_duplicate as alias_remove_duplicate  # Spelling alias
from Function.recursive_explode import recursive_explode
from Function.recursive_explod import recursive_explode as alias_recursive_explode  # Spelling alias
from Function.recursive_factorial import factorial_recur
from Function.recursive_func import factorial_recur as alias_factorial_recur  # Alias
from Function.recursive_factorial_v1 import factorial_recur as rec1_factorial
from Function.recursive_func1 import factorial_recur as alias_rec1_factorial  # Alias
from Function.recursive_factorial_v2 import factorial_recur as rec2_factorial
from Function.recursive_func2 import factorial_recur as alias_rec2_factorial  # Alias
from Function.recursive_factorial_v3 import factorial_recur as rec3_factorial
from Function.recursive_func3 import factorial_recur as alias_rec3_factorial  # Alias
from Function.recursive_list_map import map_squares
from Function.function_references import square as rec_square
from Function.recursive_square import square as alias_rec_square  # Alias
from Function.recursive_string import pick_first_letter, extract_acronym, extract_acronym_uppercase
from Function.reduce_func import add as reduce_add, sum_sequence
from Function.tax_return_func import pay_tax as tax_return_pay_tax, neto_pay as tax_return_neto_pay
from Function.triangle import calculate_triangle_area

# Dynamically import Function.global reserved module alias
global_mod_alias = importlib.import_module("Function.global")
alias_test_global_modify = getattr(global_mod_alias, "test_global_modify")


class TestFunctionBasics(unittest.TestCase):
    """Test standard function signatures, parameter passing, and return types."""

    def test_add_int(self):
        self.assertEqual(add_int(10, 20), 30)
        self.assertAlmostEqual(add_int(1.5, 2.5), 4.0)
        self.assertEqual(my_add(4, 56), 60)
        self.assertEqual(add_me(7, 9), 16)

    def test_anonymous_func(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(lambda_square(4), 16)

    def test_args_unpacking(self):
        nums = [10, 20, 30]
        self.assertEqual(calculate_sum(*nums), 60)
        tup = (5, 15, 25)
        self.assertEqual(calculate_sum(*tup), 45)

    def test_boolean_func(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(7))
        self.assertTrue(is_positive(5))
        self.assertFalse(is_positive(-3))
        # Verify backward-compatibility spelling alias works identically
        self.assertTrue(boolian_is_even(10))

    def test_build_func(self):
        nums = [12, 45, 2, 89, 34]
        max_val, min_val = get_max_and_min(nums)
        self.assertEqual(max_val, 89)
        self.assertEqual(min_val, 2)

    def test_calculator_variations(self):
        res = basic_calculator(20, 5)
        self.assertEqual(res['add'], 25)
        self.assertEqual(res['sub'], 15)
        self.assertEqual(res['mul'], 100)
        self.assertEqual(res['div'], 4.0)
        self.assertEqual(def_cal_calculator(20, 5), res)

        res5 = func5_calculator(17, 36)
        self.assertEqual(res5['add'], 53)
        self.assertEqual(alias_func5_calculator(17, 36), res5)

    def test_calculate_tuple(self):
        add_res, sub_res, mul_res, div_res = calculate(10, 2)
        self.assertEqual(add_res, 12)
        self.assertEqual(sub_res, 8)
        self.assertEqual(mul_res, 20)
        self.assertEqual(div_res, 5.0)
        # Verify alias function
        self.assertEqual(alias_calculate(10, 2), (12, 8, 20, 5.0))

    def test_calendar(self):
        cal_str = get_month_calendar(2026, 8)
        self.assertIn("August 2026", cal_str)
        self.assertIn("August 2026", alias_get_month_calendar(2026, 8))

    def test_greeting_and_formatting(self):
        self.assertEqual(greet_user("Dilshad"), "Your name is Dilshad")
        self.assertEqual(alias_greet_user("Dilshad"), "Your name is Dilshad")
        self.assertEqual(welcome_two_args("Hello", "Dilshad"), "Hello, Dilshad")
        self.assertEqual(alias_welcome_two_args("Hello", "Dilshad"), "Hello, Dilshad")
        self.assertEqual(main_hello("Python"), "Hello, Python")
        self.assertEqual(main_func("Python"), "Hello, Python")
        self.assertEqual(alias_main_func("Python"), "Hello, Python")
        self.assertEqual(main1_hello("Dilshad"), "Hello, Dilshad")
        self.assertEqual(main1_main("Dilshad"), "Hello, Dilshad")
        self.assertEqual(alias_main1_main("Dilshad"), "Hello, Dilshad")
        self.assertIn("tom@example.com", welcome_with_email("Tom", "tom@example.com"))
        self.assertIn("tom@example.com", alias_welcome_with_email("Tom", "tom@example.com"))

    def test_example_modules(self):
        self.assertEqual(number_square(5), 25)
        self.assertEqual(example1_square(5), 25)
        self.assertEqual(vowels_count("Dilshad"), 2)
        self.assertEqual(example2_vowels_count("Dilshad"), 2)

    def test_username_formatting(self):
        res = username("Dilshad", "Abdulla", 30)
        self.assertIn("DILSHAD ABDULLA", res)
        self.assertIn("30", res)

    def test_info_myfunc(self):
        self.assertEqual(myfunc(4), 5)
        self.assertEqual(alias_myfunc(4), 5)
        self.assertEqual(myfunc(8, 7), 15)


class TestAdvancedFunctions(unittest.TestCase):
    """Test closures, dispatch patterns, scope, and higher-order functions."""

    def test_closures(self):
        double = make_multiplier(2)
        triple = make_multiplier(3)
        self.assertEqual(double(5), 10)
        self.assertEqual(triple(5), 15)

        alias_double = alias_make_multiplier(2)
        self.assertEqual(alias_double(5), 10)

    def test_args_kwargs(self):
        args, kwargs = view('Alpha', 'Beta', key1='Val1', key2='Val2')
        self.assertEqual(args, ('Alpha', 'Beta'))
        self.assertEqual(kwargs, {'key1': 'Val1', 'key2': 'Val2'})

    def test_dict_lookup(self):
        self.assertEqual(get_student_name(814747), 'Dilshad Abdulla')
        self.assertEqual(dict_id_get_student_name(814747), 'Dilshad Abdulla')
        self.assertIn('Unknown user', get_student_name(999999))

    def test_dispatch_dict(self):
        self.assertEqual(dispatch_dict('add', 10, 5), 15)
        self.assertEqual(dispatch_dict('mul', 4, 3), 12)
        self.assertIsNone(dispatch_dict('invalid', 4, 3))

    def test_dispatch_if(self):
        self.assertEqual(dispatch_if('sub', 20, 8), 12)
        self.assertEqual(dispatch_if('div', 15, 3), 5.0)
        self.assertIsNone(dispatch_if('invalid', 5, 5))

    def test_higher_order_functions(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(apply_square(nums), [1, 4, 9, 16])
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertTrue(even_func(4))
        self.assertEqual(sum_sequence(list(range(1, 6))), 15)
        self.assertEqual(reduce_add(10, 20), 30)

    def test_func_stats_and_profile(self):
        prof = profile('Dilshad', 'Abdulla', '6 Ursula Gould Way', 'E14 7FX', 'London')
        self.assertIn('Dilshad', prof)
        self.assertIn('London', prof)
        self.assertEqual(alias_profile('Dilshad', 'Abdulla', '6 Ursula Gould Way', 'E14 7FX', 'London'), prof)

        add_v, sub_v = add_and_subtract_three(10, 5, 2)
        self.assertEqual(add_v, 17)
        self.assertEqual(sub_v, 3)
        self.assertEqual(alias_add_subtract_three(10, 5, 2), (17, 3))

        abs_vals = calculate_abs_values(-5.0, 10.0, -3.14, 3 + 4j)
        self.assertEqual(abs_vals, (5.0, 10.0, 3.14, 5.0))
        self.assertEqual(alias_calculate_abs_values(-5.0, 10.0, -3.14, 3 + 4j), (5.0, 10.0, 3.14, 5.0))

    def test_func_format(self):
        self.assertEqual(welcome_msg('Hello, ', 'Dilshad'), 'Hello, Dilshad')
        self.assertEqual(alias_welcome_msg('Hello, ', 'Dilshad'), 'Hello, Dilshad')
        args, kwargs = user_details('Dilshad', age=41)
        self.assertEqual(args, ('Dilshad',))
        self.assertEqual(kwargs, {'age': 41})

    def test_call_return(self):
        self.assertEqual(call_return_square(4), 16)
        self.assertEqual(power(2, 3), 8)

    def test_interactive_cave_func(self):
        caves: Dict[int, List[int]] = {1: [], 2: [], 3: []}
        create_tunnel(caves, 1, 2)
        self.assertEqual(caves[1], [2])
        self.assertEqual(caves[2], [1])

        caves_alias: Dict[int, List[int]] = {1: [], 2: [], 3: []}
        alias_create_tunnel(caves_alias, 1, 2)
        self.assertEqual(caves_alias[1], [2])

        visited: List[int] = []
        unvisited = [1, 2, 3]
        visit_cave(visited, unvisited, 1)
        self.assertEqual(visited, [1])
        self.assertNotIn(1, unvisited)

        chosen = choose_cave(caves, [1, 2, 3], rng_seed=42)
        self.assertIn(chosen, [1, 2, 3])


class TestRecursionAndUtilities(unittest.TestCase):
    """Test recursive functions, tax functions, and temperature conversion."""

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial_recur(5), 120)
        self.assertEqual(alias_factorial_recur(5), 120)
        self.assertEqual(rec1_factorial(5), 120)
        self.assertEqual(alias_rec1_factorial(5), 120)
        self.assertEqual(rec2_factorial(5), 120)
        self.assertEqual(alias_rec2_factorial(5), 120)
        self.assertEqual(rec3_factorial(5), 120)
        self.assertEqual(alias_rec3_factorial(5), 120)

    def test_recursive_string_operations(self):
        self.assertEqual(count_letter("London"), 6)
        self.assertEqual(remove_duplicate("Pyythhoon"), "Python")
        self.assertEqual(alias_remove_duplicate("Pyythhoon"), "Python")
        self.assertEqual(recursive_explode("Python"), "P y t h o n")
        self.assertEqual(alias_recursive_explode("Python"), "P y t h o n")
        
        words = ['Every', 'one', 'in', 'London', 'not', 'speak', 'english']
        self.assertEqual(extract_acronym(words), "EoiLnse")
        self.assertEqual(extract_acronym_uppercase(words), "EOILNSE")
        self.assertEqual(pick_first_letter("London"), "L")

    def test_recursive_maps_and_squares(self):
        self.assertEqual(rec_square(5), 25)
        self.assertEqual(alias_rec_square(5), 25)
        self.assertEqual(higher_order_square(5), 25)
        self.assertEqual(map_squares([1, 2, 3]), [1, 4, 9])

    def test_nested_and_scope(self):
        self.assertEqual(outer_func_nested(), "Dog")
        self.assertEqual(alias_outer_func_nested(), "Dog")

        inner_val, outer_val = global_1_out_side()
        self.assertEqual(inner_val, 'in side x')
        self.assertEqual(outer_val, 'out side x')
        self.assertEqual(alias_global_1_out_side(), (inner_val, outer_val))

        self.assertEqual(global_2_out_side(), 'Global x')
        self.assertEqual(alias_global_2_out_side(), 'Global x')

        gkw_inner, gkw_outer = global_inner_local.out_side() if 'global_inner_local' in globals() else global_kw_out_side()
        self.assertEqual(gkw_inner, 'in side x')
        self.assertEqual(alias_global_kw_out_side(), (gkw_inner, gkw_outer))

        in_val, out_val = in_out_out_side()
        self.assertEqual(in_val, 'This is local var in in_side() called x')
        self.assertEqual(alias_in_out_out_side(), (in_val, out_val))
        self.assertEqual(local_var_out_side(), 'This is local var in out_side() called x')
        self.assertEqual(alias_local_var_out_side(), 'This is local var in out_side() called x')

        initial_x, edited_x = nonlocal_out_side()
        self.assertEqual(initial_x, 'This is local var in out_side() called x')
        self.assertEqual(edited_x, 'This is local var in in_side() called x')
        self.assertEqual(alias_nonlocal_out_side(), (initial_x, edited_x))

        cnt1 = increment_global_counter(10)
        self.assertGreaterEqual(cnt1, 10)
        init_cnt, curr_cnt = get_counter_state()
        self.assertIsInstance(init_cnt, int)
        self.assertIsInstance(curr_cnt, int)

        # Alias testing
        alias_cnt = alias_inc_counter(5)
        self.assertGreaterEqual(alias_cnt, 15)

    def test_global_var_modifications(self):
        x_loc, xx_loc, y_glob, z_loc = def_global_bar(10)
        self.assertEqual(y_glob, 6)
        self.assertGreaterEqual(test_global_modify(), 15)
        self.assertGreaterEqual(alias_test_global_modify(), 18)

    def test_tax_and_conversions(self):
        self.assertEqual(pay_tax(8000), 0)
        self.assertAlmostEqual(pay_tax(20000), 3400.0)
        self.assertAlmostEqual(pay_tax(40000), 10800.0)
        self.assertAlmostEqual(neto_pay(20000), 16600.0)
        self.assertEqual(tax_return_pay_tax(8000), 0)
        self.assertAlmostEqual(tax_return_neto_pay(20000), 16600.0)

        self.assertAlmostEqual(convert_temp_to(100, 'c'), 37.77777777777778)
        self.assertAlmostEqual(convert_temp_to(0, 'f'), 32.0)
        self.assertAlmostEqual(fahrenheit_temp(100), 37.77777777777778)
        self.assertAlmostEqual(celsius_temp(0), 32.0)
        self.assertAlmostEqual(centimeter(inches=10, feet=1), 55.88)
        self.assertAlmostEqual(alias_centimeter(inches=10, feet=1), 55.88)

    def test_triangle(self):
        self.assertEqual(calculate_triangle_area(10, 5), 25.0)
        self.assertEqual(func1_get_gender('m'), 'Male')
        self.assertEqual(func1_get_gender('f'), 'Female')
        self.assertEqual(func1_get_gender(None), 'None')
        self.assertEqual(alias_func1_get_gender('m'), 'Male')

        self.assertEqual(func2_get_gender('m'), 'Male')
        self.assertEqual(func2_get_gender(None), 'There is no gender')
        self.assertEqual(alias_func2_get_gender('m'), 'Male')

    def test_if_func(self):
        self.assertTrue(if_func_is_even(8))
        self.assertIn("odd", check_number_parity(7))


if __name__ == '__main__':
    unittest.main()
