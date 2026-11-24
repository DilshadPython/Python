"""Unit test suite for the Return statement tutorial module (return_basics.py)."""

import unittest
from cloud_app.tutorials.return_basics import (
    advanced_return_mechanics,
    calculate_cube_volume,
    calculate_triangle_volume,
    check_even_odd,
    consume_generator,
    create_multiplier,
    execute_finally_return_demo,
    explicit_none_return,
    get_coordinate_3d,
    inspect_return_object,
    raise_fatal_error,
    return_patterns_and_guard_clauses,
    return_vs_legacy_mechanics,
    starter_return_examples,
    validate_and_process_user,
)


class TestReturnTutorial(unittest.TestCase):
    """Test cases for return statement mechanics and patterns."""

    def test_starter_return_examples(self) -> None:
        """Verify starter return examples data structure and outputs."""
        res = starter_return_examples()
        self.assertIsNone(res["implicit_none_result"])
        self.assertEqual(res["implicit_none_type"], "NoneType")
        self.assertEqual(res["cube_volume"], 224.0)
        self.assertEqual(res["explicit_none_true"], "Condition satisfied")
        self.assertIsNone(res["explicit_none_false"])
        self.assertEqual(res["returned_tuple"], (7.0, 8.0, 4.0))
        self.assertEqual(res["unpacked_coords"], {"x": 7.0, "y": 8.0, "z": 4.0})
        self.assertEqual(res["even_check"], "Even")
        self.assertEqual(res["odd_check"], "Odd")

    def test_calculate_cube_volume(self) -> None:
        """Test calculation of rectangular prism volume."""
        self.assertEqual(calculate_cube_volume(2.0, 3.0, 4.0), 24.0)
        self.assertEqual(calculate_cube_volume(0, 5.0, 10.0), 0.0)

    def test_check_even_odd(self) -> None:
        """Test even and odd conditional returns and error handling."""
        self.assertEqual(check_even_odd(10), "Even")
        self.assertEqual(check_even_odd(15), "Odd")
        with self.assertRaises(TypeError):
            check_even_odd("10")  # type: ignore

    def test_advanced_return_mechanics(self) -> None:
        """Verify closures, try-finally override, and generator StopIteration return value."""
        res = advanced_return_mechanics(limit=5, override_finally=True)
        self.assertEqual(res["double_7"], 14.0)
        self.assertEqual(res["triple_7"], 21.0)
        self.assertEqual(res["try_normal_return"], "Return from try block")
        self.assertEqual(res["try_override_return"], "Return overridden by finally block")
        self.assertEqual(res["generator_yielded_items"], [0, 1, 2, 3, 4])
        self.assertEqual(res["generator_stop_iteration_value"], "Completed generator iteration up to 5")
        self.assertTrue(res["no_return_exception_caught"])
        self.assertIn("Fatal error encountered", res["no_return_error_message"])

    def test_create_multiplier_closure(self) -> None:
        """Test higher-order multiplier closure generation."""
        times_five = create_multiplier(5.0)
        self.assertEqual(times_five(10.0), 50.0)

    def test_execute_finally_return_demo(self) -> None:
        """Test try-finally return override behavior."""
        self.assertEqual(execute_finally_return_demo(override=False), "Return from try block")
        self.assertEqual(execute_finally_return_demo(override=True), "Return overridden by finally block")

    def test_consume_generator_pep380(self) -> None:
        """Test generator consumption and PEP 380 return value extraction."""
        items, status = consume_generator(3)
        self.assertEqual(items, [0, 1, 2])
        self.assertEqual(status, "Completed generator iteration up to 3")

    def test_raise_fatal_error_noreturn(self) -> None:
        """Test NoReturn error raising function."""
        with self.assertRaises(RuntimeError) as ctx:
            raise_fatal_error("Database connection lost")
        self.assertIn("Database connection lost", str(ctx.exception))

    def test_return_patterns_and_guard_clauses(self) -> None:
        """Test guard clause validations and dir() introspection outputs."""
        res = return_patterns_and_guard_clauses()
        guards = res["guard_results"]
        self.assertEqual(guards["none_input"]["status"], "error")
        self.assertEqual(guards["empty_input"]["status"], "error")
        self.assertEqual(guards["underage_input"]["status"], "error")
        self.assertEqual(guards["valid_input"]["status"], "success")
        self.assertEqual(guards["valid_input"]["processed_data"]["username"], "bob")

        self.assertGreater(res["str_public_methods_count"], 0)
        self.assertIn("keys", res["dict_public_methods"])
        self.assertIn("values", res["dict_public_methods"])

    def test_validate_and_process_user(self) -> None:
        """Test individual guard clause validation branches."""
        self.assertEqual(validate_and_process_user(None)["message"], "Input data cannot be None")
        self.assertEqual(validate_and_process_user("not a dict")["message"], "Input data must be a dictionary")  # type: ignore
        self.assertEqual(validate_and_process_user({})["message"], "Missing required field: username")
        self.assertEqual(validate_and_process_user({"username": "Sam", "age": 12})["message"], "User must be at least 18 years old")
        
        valid_res = validate_and_process_user({"username": "  Alice  ", "age": 30})
        self.assertEqual(valid_res["status"], "success")
        self.assertEqual(valid_res["processed_data"]["username"], "alice")

    def test_inspect_return_object(self) -> None:
        """Test dir() filtering of private double-underscore methods."""
        methods = inspect_return_object([1, 2, 3])
        self.assertIn("append", methods)
        self.assertIn("pop", methods)
        self.assertNotIn("__len__", methods)

    def test_return_vs_legacy_mechanics(self) -> None:
        """Verify cross-version evolution benchmarking outputs."""
        res = return_vs_legacy_mechanics()
        self.assertIn("RETURN_VALUE", res["bytecode_opcodes"])
        self.assertIn("RETURN_CONST", res["bytecode_opcodes"])
        self.assertIn("Python 3.3", res["version_milestones"])
        self.assertIn("Python 3.12", res["version_milestones"])


if __name__ == "__main__":
    unittest.main()
