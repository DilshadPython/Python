"""Unit test suite for Python Function Architecture, Parameter Passing, LEGB Scope & Recursion Mechanics."""

import unittest
from cloud_app.tutorials.function_basics import (
    starter_function_examples,
    scope_and_legb_rule,
    functional_utilities_and_dispatch,
    recursion_mechanics,
    legacy_python2_comparison_demo,
    execute_all_dir_function_methods,
    cross_version_function_analysis,
)


class TestFunctionTutorial(unittest.TestCase):
    """Test suite for verifying function parameter passing, scope resolution, higher-order functions, and recursion."""

    def test_starter_function_examples_defaults(self):
        """Validates default arguments, *args, **kwargs, and arithmetic returns."""
        res = starter_function_examples("Monika", 20, 5, 10, role="Engineer", location="London")

        self.assertIn("Welcome, Monika!", res["greeting_msg"])
        self.assertEqual(res["args_sum"], 35)  # 20 + 5 + 10
        self.assertEqual(res["unpacked_args_count"], 2)
        self.assertEqual(res["user_profile"]["role"], "Engineer")
        self.assertEqual(res["user_profile"]["location"], "London")
        self.assertEqual(res["arithmetic_stats"]["sum"], 25)  # 20 + 5
        self.assertEqual(res["arithmetic_stats"]["product"], 100)  # 20 * 5
        self.assertEqual(res["arithmetic_stats"]["average"], 12.5)

    def test_starter_function_examples_invalid_type(self):
        """Validates guard clause error handling for invalid input types."""
        with self.assertRaises(TypeError):
            starter_function_examples(12345, 10)
        with self.assertRaises(TypeError):
            starter_function_examples("Dilshad", "not a number")

    def test_scope_and_legb_rule(self):
        """Validates global modification, LEGB scope lookup, nonlocal scope, and closures."""
        res = scope_and_legb_rule(15)

        self.assertEqual(res["modified_global"], res["original_global"] + 15)
        self.assertEqual(res["local_shadow_val"], 30)
        self.assertEqual(res["enclosing_first_step"], 60)   # 50 + 10
        self.assertEqual(res["enclosing_second_step"], 80)  # 60 + 20
        self.assertEqual(res["closure_double_val"], 60)     # 30 * 2
        self.assertEqual(res["closure_triple_val"], 90)     # 30 * 3

    def test_scope_invalid_type(self):
        """Validates guard clause error handling for non-integer initial value."""
        with self.assertRaises(TypeError):
            scope_and_legb_rule("invalid")

    def test_functional_utilities_and_dispatch(self):
        """Validates lambda functions, filter, reduce, dispatch tables, and higher-order functions."""
        items = [1, 2, 3, 4, 5]
        res = functional_utilities_and_dispatch(items, op_name="product")

        self.assertEqual(res["squared_list"], [1, 4, 9, 16, 25])
        self.assertEqual(res["even_items"], [2, 4])
        self.assertEqual(res["product_reduction"], 120)  # 1 * 2 * 3 * 4 * 5
        self.assertEqual(res["dispatch_result"], 120)
        self.assertEqual(res["cube_transform"], [1, 8, 27, 64, 125])

    def test_functional_utilities_invalid_type(self):
        """Validates guard clause error handling for invalid sequence inputs."""
        with self.assertRaises(TypeError):
            functional_utilities_and_dispatch("not a list")

    def test_recursion_mechanics(self):
        """Validates recursive factorial, character count, and string deduplication."""
        res = recursion_mechanics(5, "baanaanaa")

        self.assertEqual(res["input_number"], 5)
        self.assertEqual(res["factorial_result"], 120)
        self.assertEqual(res["target_letter_count"], 6)
        self.assertEqual(res["deduplicated_text"], "banana")

    def test_recursion_invalid_input(self):
        """Validates guard clauses for negative numbers and non-string inputs."""
        with self.assertRaises(ValueError):
            recursion_mechanics(-1, "hello")
        with self.assertRaises(TypeError):
            recursion_mechanics(5, 12345)

    def test_legacy_python2_comparison_demo(self):
        """Validates Python 2 vs Python 3 tuple unpacking, nonlocal state, and dynamic calls."""
        res = legacy_python2_comparison_demo((10, 20), 3)

        self.assertEqual(res["scaled_point"], (30, 60))
        self.assertEqual(res["closure_state_counter"], 2)
        self.assertEqual(res["dynamic_unpacking_result"], 30)
        self.assertEqual(res["dunder_name"], "sample_func")

    def test_execute_all_dir_function_methods(self):
        """Validates function dunder attributes inspection and callable checks."""
        res = execute_all_dir_function_methods()

        self.assertEqual(res["function_name"], "target_function")
        self.assertIn("Sample function docstring", res["docstring"])
        self.assertEqual(res["parameter_names"], ["a", "b"])
        self.assertTrue(res["is_callable"])

    def test_cross_version_function_analysis(self):
        """Validates Python 3.8+ positional-only (/) and keyword-only (*) syntax checks."""
        res = cross_version_function_analysis()

        self.assertEqual(res["positional_and_kwonly_result"], 60)
        self.assertTrue(res["has_positional_only_params"])
        self.assertTrue(res["has_keyword_only_params"])


if __name__ == "__main__":
    unittest.main()
