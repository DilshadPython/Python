"""
Unittest Suite for Exception Handling Module (`exception_handling`)
"""
import os
import unittest
from exception_handling.basic_try_except import (
    safe_divide,
    safe_parse_int,
    safe_get_dict_key,
    safe_get_list_element,
)
from exception_handling.multiple_exceptions import (
    parse_and_divide,
    process_command_args,
)
from exception_handling.try_else_finally import execute_transaction
from exception_handling.exception_objects_and_traceback import inspect_exception_details
from exception_handling.raising_and_custom_exceptions import (
    register_user,
    connect_database,
    ValidationError,
    DatabaseConnectionError,
)
from exception_handling.exception_propagation_and_stack import CalculationService
from exception_handling.file_and_resource_handling import (
    read_config_file_try_finally,
    read_config_file_context_manager,
)


class TestExceptionHandling(unittest.TestCase):
    """Test case suite covering all exception handling modules."""

    def test_basic_try_except(self) -> None:
        """Tests basic safe wrapper functions."""
        self.assertEqual(safe_divide(10.0, 2.0), 5.0)
        self.assertIsNone(safe_divide(10.0, 0.0))

        self.assertEqual(safe_parse_int("42"), 42)
        self.assertIsNone(safe_parse_int("invalid"))

        ages = {"adam": 33}
        self.assertEqual(safe_get_dict_key(ages, "adam"), 33)
        self.assertEqual(safe_get_dict_key(ages, "missing", default=0), 0)

        items = ["a", "b"]
        self.assertEqual(safe_get_list_element(items, 1), "b")
        self.assertEqual(safe_get_list_element(items, 5, default="x"), "x")

    def test_multiple_exceptions(self) -> None:
        """Tests multiple exception handling functions."""
        data = ["10", "2", "0", "invalid"]
        self.assertEqual(parse_and_divide(data, 0, 1), 5.0)
        self.assertIn("ZeroDivisionError", parse_and_divide(data, 0, 2))
        self.assertIn("ValueError", parse_and_divide(data, 0, 3))
        self.assertIn("IndexError", parse_and_divide(data, 0, 10))

        ok, msg = process_command_args(["100"])
        self.assertTrue(ok)
        self.assertIn("Successfully parsed", msg)

        fail, fail_msg = process_command_args([])
        self.assertFalse(fail)
        self.assertIn("InputError", fail_msg)

    def test_try_else_finally(self) -> None:
        """Tests try-except-else-finally workflow logs and balance calculation."""
        ok, bal, logs = execute_transaction(50.0, 200.0)
        self.assertTrue(ok)
        self.assertEqual(bal, 150.0)
        self.assertTrue(any("`else` block" in entry for entry in logs))
        self.assertTrue(any("`finally` block" in entry for entry in logs))

        fail_ok, fail_bal, fail_logs = execute_transaction(300.0, 200.0)
        self.assertFalse(fail_ok)
        self.assertEqual(fail_bal, 200.0)
        self.assertTrue(any("`except` block" in entry for entry in fail_logs))
        self.assertTrue(any("`finally` block" in entry for entry in fail_logs))

    def test_exception_objects_and_traceback(self) -> None:
        """Tests exception inspection and traceback details."""
        info = inspect_exception_details("zero")
        self.assertEqual(info["type_name"], "ZeroDivisionError")
        self.assertIn("Traceback", info["formatted_traceback"])

    def test_custom_exceptions(self) -> None:
        """Tests raising custom ValidationError and chained DatabaseConnectionError."""
        valid_res = register_user({"username": "alice", "age": 25})
        self.assertIn("successfully registered", valid_res)

        with self.assertRaises(ValidationError) as ctx:
            register_user({"username": "bob", "age": 15})
        self.assertEqual(ctx.exception.field, "age")
        self.assertEqual(ctx.exception.code, 400)

        with self.assertRaises(DatabaseConnectionError) as db_ctx:
            connect_database("invalid_url")
        self.assertIsInstance(db_ctx.exception.__cause__, TimeoutError)

    def test_propagation_and_stack(self) -> None:
        """Tests call stack propagation."""
        service = CalculationService()
        self.assertEqual(service.process_data([20.0, 4.0]), 5.0)
        with self.assertRaises(ZeroDivisionError):
            service.process_data([20.0, 0.0])

    def test_file_resource_handling(self) -> None:
        """Tests File I/O exception handling."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "config_file.txt")
        content = read_config_file_context_manager(config_path)
        self.assertIsNotNone(content)
        self.assertIn("port=8080", content)

        self.assertIsNone(read_config_file_context_manager("non_existent_file.txt"))


if __name__ == "__main__":
    unittest.main()
