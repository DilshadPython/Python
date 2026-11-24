"""Unit Test Suite for the Python Return Tutorial Module.

This module provides comprehensive test coverage for all return functions,
closure returns, try-finally override behaviors, generator return values,
guard clause validations, and object introspection across return_basics,
return_advanced, return_patterns, and return_.
"""

# import standard unittest module for assertions and test runner
import unittest

# import functions to test from module files
from return_basics import (
    calculate_triangle_volume,
    calculate_cube_volume,
    explicit_none_return,
    get_coordinate_3d,
    check_even_odd,
)
from return_advanced import (
    create_multiplier,
    execute_finally_return_demo,
    generator_with_return_value,
    consume_generator,
    raise_fatal_error,
)
from return_patterns import (
    validate_and_process_user,
    inspect_return_object,
)
import return_ as legacy_return


class TestReturnBasics(unittest.TestCase):
    """Unit tests for basic return statement mechanics in return_basics.py."""

    def test_implicit_none_return(self) -> None:
        """Verify that functions without a return statement return None."""
        result = calculate_triangle_volume(7.0, 8.0)
        self.assertIsNone(result)

    def test_explicit_value_return(self) -> None:
        """Verify that calculate_cube_volume returns the correct numeric product."""
        result = calculate_cube_volume(7.0, 8.0, 4.0)
        self.assertEqual(result, 224.0)

    def test_explicit_none_return(self) -> None:
        """Verify explicit return of string vs explicit return None."""
        self.assertEqual(explicit_none_return(True), "Condition satisfied")
        self.assertIsNone(explicit_none_return(False))

    def test_multiple_return_tuple_packing(self) -> None:
        """Verify returning multiple comma-separated values returns a packed tuple."""
        coords = get_coordinate_3d(1.5, 2.5, 3.5)
        self.assertIsInstance(coords, tuple)
        self.assertEqual(coords, (1.5, 2.5, 3.5))

    def test_conditional_early_return(self) -> None:
        """Verify early return branching in check_even_odd."""
        self.assertEqual(check_even_odd(10), "Even")
        self.assertEqual(check_even_odd(7), "Odd")


class TestReturnAdvanced(unittest.TestCase):
    """Unit tests for advanced return patterns in return_advanced.py."""

    def test_returning_closure_callable(self) -> None:
        """Verify higher-order function returning a callable closure."""
        double = create_multiplier(2.0)
        self.assertTrue(callable(double))
        self.assertEqual(double(5.0), 10.0)

    def test_try_finally_return_precedence(self) -> None:
        """Verify return value override behavior inside try...finally blocks."""
        normal_res = execute_finally_return_demo(override=False)
        self.assertEqual(normal_res, "Return from try block")

        overridden_res = execute_finally_return_demo(override=True)
        self.assertEqual(overridden_res, "Return overridden by finally block")

    def test_generator_return_value_pep_380(self) -> None:
        """Verify generator return value payload inside StopIteration.value."""
        items, status_msg = consume_generator(3)
        self.assertEqual(items, [0, 1, 2])
        self.assertEqual(status_msg, "Completed generator iteration up to 3")

    def test_no_return_type_hint(self) -> None:
        """Verify that functions annotated with NoReturn raise an exception."""
        with self.assertRaises(RuntimeError) as ctx:
            raise_fatal_error("Database offline")
        self.assertIn("Database offline", str(ctx.exception))


class TestReturnPatterns(unittest.TestCase):
    """Unit tests for guard clause patterns and dir() introspection."""

    def test_guard_clause_validation(self) -> None:
        """Verify early guard clause returns for invalid inputs."""
        # Test None input guard
        res_none = validate_and_process_user(None)
        self.assertEqual(res_none["status"], "error")
        self.assertIn("cannot be None", res_none["message"])

        # Test missing username guard
        res_no_user = validate_and_process_user({"age": 20})
        self.assertEqual(res_no_user["status"], "error")
        self.assertIn("username", res_no_user["message"])

        # Test age requirement guard
        res_young = validate_and_process_user({"username": "Sam", "age": 15})
        self.assertEqual(res_young["status"], "error")
        self.assertIn("18 years old", res_young["message"])

        # Test happy path return
        res_valid = validate_and_process_user({"username": "  Alice  ", "age": 21})
        self.assertEqual(res_valid["status"], "success")
        self.assertEqual(res_valid["processed_data"]["username"], "alice")

    def test_dir_introspection(self) -> None:
        """Verify public method introspection using dir()."""
        attrs = inspect_return_object("Test String")
        self.assertIn("upper", attrs)
        self.assertNotIn("__add__", attrs)


class TestLegacyReturnScript(unittest.TestCase):
    """Unit tests verifying backward compatibility of return_.py."""

    def test_legacy_triangle(self) -> None:
        """Verify legacy triangle function returns None."""
        self.assertIsNone(legacy_return.triangle(7.0, 8.0, 4.0))

    def test_legacy_cube(self) -> None:
        """Verify legacy cube function returns correct volume product."""
        self.assertEqual(legacy_return.cube(7.0, 8.0, 4.0), 224.0)


if __name__ == "__main__":
    unittest.main()
