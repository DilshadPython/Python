"""Automated Unit Test Suite for Python Loop Modules (`Loops`).

Provides comprehensive unit testing using standard library 'unittest' to verify
functional correctness across all 25 loop scripts in the 'Loops' directory.

Import Notes:
    - 'import os, sys, unittest': Standard library infrastructure for path resolution,
      system environment execution, and testing assertions.
    - 'from unittest.mock import patch': Standard library mock utility used to patch
      interactive input calls during automated test execution.
    - Imports all module functions under test from local directory modules.
"""

import os
import sys
import unittest
from unittest.mock import patch

# Ensure current directory is on sys.path for direct imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _notused import execute_unused_variable_loop
from add_nums import accumulate_list_manually, accumulate_list_builtin, deduplicate_numbers
from big_word import calculate_word_frequencies, find_most_frequent_word
from def_for import generate_range_list
from def_while_for import validate_positive_integer, repeat_python_greeting
from double_def_for import execute_repeated_greeting
from elevator import navigate_elevator
from exculator import run_exculator_simulation
from end_py import format_horizontal_sequence, demonstrate_print_end_parameter
from for_bar import generate_grade_bar, process_grade_bars
from for_dic_key import (
    inspect_dictionary_keys,
    inspect_dictionary_values,
    inspect_dictionary_key_value_pairs,
)
from for_dict import (
    get_sample_users,
    display_user_summaries,
    filter_users_by_social_platform,
    search_users_by_id_range,
)
from for_else import search_technology_stack
from for_enumerate_index import generate_enumerated_pairs
from for_factorial import calculate_factorial
from for_factrorial import run_legacy_factorial_demo
from for_index import search_car_inventory_fixed_range, search_car_inventory_dynamic_range
from for_len import get_python_libraries, list_libraries_via_range_len, list_libraries_via_enumerate
from for_list import iterate_entire_list, iterate_list_slice
from for_loop import (
    iterate_names_basic,
    demonstrate_break,
    demonstrate_continue,
    demonstrate_nested_loops,
)
from for_print import repeat_string_horizontal, repeat_string_vertical
from for_range import (
    generate_single_arg_range,
    generate_two_arg_range,
    generate_stepped_range,
)
from for_tuple import iterate_tuple_elements, accumulate_tuple_sum, find_longest_string_in_tuple
from print_shape_forloop import generate_ascending_hash_triangle, generate_descending_hash_triangle
from shape_code import generate_numeric_pyramid_shape
from stop import evaluate_loop_keywords
from while_for import validate_positive_number, repeat_greeting_loop


class TestLoopsSuite(unittest.TestCase):
    """Test suite covering all loop modules and functions."""

    def setUp(self):
        """Set up script directory path reference."""
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def test_unused_variable_loop(self):
        """Test throwaway variable loop functionality in _notused.py."""
        results = execute_unused_variable_loop(3)
        self.assertEqual(len(results), 3)
        self.assertIn("throwaway variable", results[0])

    def test_add_nums(self):
        """Test manual sum, built-in sum, and set deduplication in add_nums.py."""
        numbers = [4, 5, 7, 5, 4, 8]
        self.assertEqual(accumulate_list_manually(numbers), 33)
        self.assertEqual(accumulate_list_builtin(numbers), 33)
        self.assertEqual(deduplicate_numbers(numbers), {4, 5, 7, 8})

    def test_big_word(self):
        """Test word frequency and top word detection in big_word.py."""
        target_file = os.path.join(self.script_dir, "words.txt")
        counts = calculate_word_frequencies(target_file)
        self.assertIsInstance(counts, dict)
        self.assertGreater(len(counts), 0)
        top_word, top_count = find_most_frequent_word(counts)
        self.assertIsNotNone(top_word)
        self.assertGreater(top_count, 0)

    def test_def_for(self):
        """Test range generation function in def_for.py."""
        res = generate_range_list(1, 5)
        self.assertEqual(res, [1, 2, 3, 4, 5])

    @patch("builtins.input", return_value="4")
    def test_def_while_for(self, mock_input):
        """Test integer validation and greeting generation in def_while_for.py."""
        val = validate_positive_integer("Prompt: ", default_val=3)
        self.assertEqual(val, 4)
        greetings = repeat_python_greeting(3)
        self.assertEqual(len(greetings), 3)

    def test_double_def_for(self):
        """Test repeated greeting in double_def_for.py."""
        greetings = execute_repeated_greeting(4)
        self.assertEqual(len(greetings), 4)

    def test_elevator_and_exculator(self):
        """Test floor navigation in elevator.py and exculator.py."""
        success, visited = navigate_elevator(5, 12)
        self.assertTrue(success)
        self.assertEqual(visited, [1, 2, 3, 4, 5])

        # Test exculator compatibility wrapper
        s2, v2 = run_exculator_simulation(3)
        self.assertTrue(s2)
        self.assertEqual(v2, [1, 2, 3])

    def test_end_py(self):
        """Test print end parameter formatting in end_py.py."""
        formatted = format_horizontal_sequence(5, ", ")
        self.assertEqual(formatted, "0, 1, 2, 3, 4")
        outputs = demonstrate_print_end_parameter()
        self.assertGreaterEqual(len(outputs), 2)

    def test_for_bar(self):
        """Test grade bar chart generation in for_bar.py."""
        bar_str, last_idx = generate_grade_bar(23, 5)
        self.assertEqual(bar_str, "####")
        self.assertEqual(last_idx, 23)

        target_file = os.path.join(self.script_dir, "grade.txt")
        bars = process_grade_bars(target_file)
        self.assertGreater(len(bars), 0)

    def test_for_dic_key(self):
        """Test dictionary keys and values iteration in for_dic_key.py."""
        people = {"Alan": 23, "Sara": 30, "Tom": 28}
        self.assertEqual(inspect_dictionary_keys(people), ["Alan", "Sara", "Tom"])
        self.assertEqual(inspect_dictionary_values(people), [23, 30, 28])
        pairs = inspect_dictionary_key_value_pairs(people)
        self.assertEqual(len(pairs), 3)

    def test_for_dict(self):
        """Test user filtering and ID searching in for_dict.py."""
        users = get_sample_users()
        summaries = display_user_summaries(users)
        self.assertEqual(len(summaries), 4)

        tw_users, li_users = filter_users_by_social_platform(users)
        self.assertEqual(len(tw_users), 1)
        self.assertEqual(len(li_users), 1)

        matched = search_users_by_id_range(users, 10)
        self.assertEqual(len(matched), 4)

    def test_for_else(self):
        """Test for-else loop search in for_else.py."""
        techs = ["Python", "Java", "C++"]
        found, msg1 = search_technology_stack(techs, "Java")
        self.assertTrue(found)
        self.assertIn("found", msg1)

        not_found, msg2 = search_technology_stack(techs, "Ruby")
        self.assertFalse(not_found)
        self.assertIn("not found", msg2)

    def test_for_enumerate_index(self):
        """Test enumerated loop pairing in for_enumerate_index.py."""
        names = ["Tom"]
        numbers = [1, 2]
        alphas = ["A"]
        records = generate_enumerated_pairs(names, numbers, alphas)
        self.assertEqual(len(records), 3)

    def test_factorial(self):
        """Test factorial calculation in for_factorial.py and for_factrorial.py."""
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        with self.assertRaises(ValueError):
            calculate_factorial(-3)

        self.assertEqual(run_legacy_factorial_demo(5), 120)

    def test_for_index(self):
        """Test car inventory search in for_index.py."""
        cars = ["Audi", "Fiat", "Alfa Romeo", "Porsche", "Volvo"]
        f1, s1 = search_car_inventory_fixed_range(cars, "Porsche")
        self.assertTrue(f1)
        f2, s2 = search_car_inventory_dynamic_range(cars, "Fiat")
        self.assertTrue(f2)

    def test_for_len(self):
        """Test library listing in for_len.py."""
        libs = get_python_libraries()
        res1 = list_libraries_via_range_len(libs)
        res2 = list_libraries_via_enumerate(libs)
        self.assertEqual(len(res1), len(libs))
        self.assertEqual(res1, res2)

    def test_for_list(self):
        """Test list iteration and slicing in for_list.py."""
        cities = ["Paris", "London", "Berlin", "Tokyo", "Brussels", "Rome"]
        self.assertEqual(iterate_entire_list([1, 2, 3]), [1, 2, 3])
        slice_res = iterate_list_slice(cities, 2, 5)
        self.assertEqual(slice_res, ["Berlin", "Tokyo", "Brussels"])

    def test_for_loop(self):
        """Test break, continue, and nested loop in for_loop.py."""
        names = ["Tom", "Chris", "Julia", "Rob", "Claudio"]
        nums = [1, 2]
        self.assertEqual(iterate_names_basic(names), names)
        broken = demonstrate_break(names, "Rob")
        self.assertEqual(broken, ["Tom", "Chris", "Julia"])
        continued = demonstrate_continue(names, "Rob")
        self.assertEqual(len(continued), 4)
        pairs = demonstrate_nested_loops(["Tom"], nums)
        self.assertEqual(len(pairs), 2)

    def test_for_print(self):
        """Test string repetition in for_print.py."""
        h_str = repeat_string_horizontal("Hi", 3)
        self.assertEqual(h_str, "Hi\tHi\tHi\t")
        v_str = repeat_string_vertical("Hi", 2)
        self.assertEqual(v_str, "Hi\nHi\n")

    def test_for_range(self):
        """Test range sequence functions in for_range.py."""
        self.assertEqual(generate_single_arg_range(5), [0, 1, 2, 3, 4])
        self.assertEqual(generate_two_arg_range(1, 5), [1, 2, 3, 4])
        self.assertEqual(generate_stepped_range(1, 10, 3), [1, 4, 7])

    def test_for_tuple(self):
        """Test tuple iteration, sum, and longest string in for_tuple.py."""
        tup = (1, 2, 3, 4)
        self.assertEqual(iterate_tuple_elements(tup), [1, 2, 3, 4])
        self.assertEqual(accumulate_tuple_sum(tup), 10)

        cities = ("Paris", "London", "Brussels")
        top_name, idx = find_longest_string_in_tuple(cities)
        self.assertEqual(top_name, "Brussels")
        self.assertEqual(idx, 2)

    def test_print_shape_forloop(self):
        """Test hash triangle shape generation in print_shape_forloop.py."""
        asc = generate_ascending_hash_triangle(3)
        self.assertEqual(len(asc), 3)
        self.assertEqual(asc[0], "#")
        self.assertEqual(asc[2], "# # #")

        desc = generate_descending_hash_triangle(3)
        self.assertEqual(len(desc), 3)
        self.assertEqual(desc[0], "# # #")
        self.assertEqual(desc[2], "#")

    def test_shape_code(self):
        """Test complex pyramid shape generation in shape_code.py."""
        lines = generate_numeric_pyramid_shape(4)
        self.assertEqual(len(lines), 4)

    def test_stop(self):
        """Test loop control keywords break, continue, pass in stop.py."""
        data = ["a", "SKIP", "b", "STOP", "c"]
        processed, state = evaluate_loop_keywords(data, "STOP", "SKIP")
        self.assertEqual(processed, ["a", "b"])
        self.assertEqual(state, "BROKEN_AT_STOP")

    @patch("builtins.input", return_value="3")
    def test_while_for(self, mock_input):
        """Test repeating greeting loop in while_for.py."""
        val = validate_positive_number(default_val=3)
        self.assertEqual(val, 3)
        greetings = repeat_greeting_loop(4)
        self.assertEqual(len(greetings), 4)


if __name__ == "__main__":
    unittest.main()
