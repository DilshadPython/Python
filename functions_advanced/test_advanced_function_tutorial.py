"""Unit test suite for Advanced Python Functions, Decorators, Generators, Async Coroutines & Functools Utilities."""

import unittest
from cloud_app.tutorials.advanced_function_basics import (
    decorator_patterns_and_wrappers,
    generator_mechanics_and_coroutines,
    functools_advanced_utilities,
    async_coroutines_and_generators,
    python2_legacy_advanced_comparison,
    execute_advanced_function_introspection,
)


class TestAdvancedFunctionTutorial(unittest.TestCase):
    """Test suite for verifying advanced decorators, generators, functools utilities, and async coroutines."""

    def test_decorator_patterns_and_wrappers(self):
        """Validates timer decorator, retry decorator, class decorator, and @wraps metadata."""
        res = decorator_patterns_and_wrappers(10, 5)

        self.assertEqual(res["timer_result"], 50)
        self.assertTrue(res["latency_measured"])
        self.assertEqual(res["wrapped_name"], "sample_multiply")
        self.assertEqual(res["wrapped_doc"], "Multiplies two numbers.")
        self.assertTrue(res["has_wrapped_attr"])
        self.assertTrue(res["retry_success"]["success"])
        self.assertEqual(res["retry_success"]["result"], 2.0)
        self.assertFalse(res["retry_failure"]["success"])
        self.assertEqual(res["retry_failure"]["attempts"], 2)
        self.assertEqual(res["class_decorator_call_1"]["call_count"], 1)
        self.assertEqual(res["class_decorator_call_2"]["call_count"], 2)

    def test_decorator_invalid_input(self):
        """Validates guard clauses for invalid numerical inputs in decorator wrapper."""
        with self.assertRaises(TypeError):
            decorator_patterns_and_wrappers("invalid", 5)

    def test_generator_mechanics_and_coroutines(self):
        """Validates yield, yield from subgenerator delegation, and bidirectional .send()."""
        res = generator_mechanics_and_coroutines(5)

        self.assertEqual(res["fibonacci_sequence"], [0, 1, 1, 2, 3])
        self.assertEqual(res["delegated_items"], ["Header Start", "Task Alpha", "Task Beta", "Header End"])
        self.assertEqual(res["parent_summary"], {"worker_summary": "Worker Complete"})
        self.assertEqual(res["bidirectional_steps"], [10, 35])
        self.assertEqual(res["final_accumulated_total"], 35)
        self.assertLess(res["gen_exp_size_bytes"], res["list_comp_size_bytes"])

    def test_generator_invalid_input(self):
        """Validates guard clause error handling for negative or zero limits."""
        with self.assertRaises(ValueError):
            generator_mechanics_and_coroutines(-5)

    def test_functools_advanced_utilities(self):
        """Validates functools.partial, lru_cache memoization, and singledispatch function overloading."""
        res = functools_advanced_utilities(2)

        self.assertEqual(res["partial_square_5"], 25)
        self.assertEqual(res["partial_cube_5"], 125)
        self.assertEqual(res["partial_target_func"], "power_calculator")
        self.assertEqual(res["partial_keywords"], {"exponent": 2})
        self.assertEqual(res["cached_fib_30"], 832040)
        self.assertGreater(res["cache_hits"], 0)
        self.assertEqual(res["cache_maxsize"], 128)
        self.assertIn("Integer payload handler", res["singledispatch_int"])
        self.assertIn("List payload handler", res["singledispatch_list"])
        self.assertIn("Dict payload handler", res["singledispatch_dict"])
        self.assertIn("Generic payload handler", res["singledispatch_str"])

    def test_functools_invalid_input(self):
        """Validates guard clauses for invalid power parameter."""
        with self.assertRaises(TypeError):
            functools_advanced_utilities("invalid")

    def test_async_coroutines_and_generators(self):
        """Validates native async def / await coroutines and async stream generators."""
        res = async_coroutines_and_generators(3)

        self.assertEqual(len(res["coroutine_results"]), 3)
        self.assertEqual(res["coroutine_results"][0]["status"], "completed")
        self.assertEqual(res["streamed_items"], [10, 20, 30])

    def test_async_invalid_input(self):
        """Validates guard clause for invalid async task count."""
        with self.assertRaises(ValueError):
            async_coroutines_and_generators(0)

    def test_python2_legacy_advanced_comparison(self):
        """Validates Python 2 legacy generator next() vs Python 3 next() and manual memoize class."""
        res = python2_legacy_advanced_comparison()

        self.assertEqual(res["generator_next_py3_syntax"], [100, 200])
        self.assertEqual(res["manual_memoize_py2_result"], 120)
        self.assertGreaterEqual(res["manual_memoize_cache_size"], 5)

    def test_execute_advanced_function_introspection(self):
        """Validates introspection of generator states, partial keywords, wraps metadata, and coroutines."""
        res = execute_advanced_function_introspection()

        self.assertEqual(res["generator_state_created"], "GEN_CREATED")
        self.assertTrue(res["generator_is_running"])
        self.assertEqual(res["partial_func_name"], "target")
        self.assertEqual(res["partial_keywords"], {"b": 20})
        self.assertEqual(res["decorated_wrapped_name"], "annotated_fn")
        self.assertEqual(res["decorated_docstring"], "Annotated function doc.")
        self.assertTrue(res["is_coroutine_function"])


if __name__ == "__main__":
    unittest.main()
