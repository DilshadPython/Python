"""
Python Exception Handling: Exception Instances & Traceback Introspection

This module demonstrates inspecting exception instances (`as err`), extracting
error arguments (`err.args`), identifying error types (`type(err).__name__`),
and formatting stack tracebacks using Python's standard `traceback` module.

Key Concepts:
- `as err`: Assigns the caught exception object to variable `err`.
- `err.args`: Tuple of positional arguments passed to the exception constructor.
- `traceback.format_exc()`: Returns the full stack trace string of the current exception.
"""
import sys
import traceback
from typing import Dict, Any


def inspect_exception_details(operation_type: str) -> Dict[str, Any]:
    """
    Triggers an exception based on operation type and captures detailed metadata.

    Args:
        operation_type (str): Type of error to trigger ('key', 'index', 'zero').

    Returns:
        Dict[str, Any]: Dictionary containing exception type, args, and formatted traceback.
    """
    info: Dict[str, Any] = {}
    try:
        if operation_type == "key":
            lookup: Dict[str, str] = {}
            _ = lookup["missing_key"]
        elif operation_type == "index":
            items = [1, 2]
            _ = items[10]
        elif operation_type == "zero":
            _ = 1 / 0
        else:
            raise ValueError(f"Unknown operation_type: {operation_type}")
    except Exception as err:
        # Capture exception metadata
        info["type_name"] = type(err).__name__
        info["module"] = type(err).__module__
        info["args"] = err.args
        info["str_representation"] = str(err)
        info["formatted_traceback"] = traceback.format_exc()
        info["exc_info"] = sys.exc_info()[0].__name__ if sys.exc_info()[0] else None

    return info


def main() -> None:
    """Demonstrates exception instance and traceback inspection."""
    print("=" * 60)
    print("4. Exception Object & Traceback Introspection")
    print("=" * 60)

    for op in ["key", "index", "zero"]:
        print(f"\n--- Operation: {op!r} ---")
        details = inspect_exception_details(op)
        print(f"  Exception Class: {details['module']}.{details['type_name']}")
        print(f"  Exception Args:  {details['args']!r}")
        print(f"  String Value:    {details['str_representation']!r}")
        print("  Formatted Stack Trace snippet:")
        tb_lines = details["formatted_traceback"].strip().splitlines()
        for line in tb_lines[-3:]:  # Display last 3 lines of traceback
            print(f"    {line}")


if __name__ == "__main__":
    main()
