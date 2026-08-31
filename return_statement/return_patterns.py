"""Return Patterns and Best Practices Module.

This module demonstrates software engineering best practices for return statements,
including guard clauses (early returns), structured dictionary returns, error handling
strategies, and introspection of function return objects using dir().
"""

# import typing for structured dictionary definitions and type hints
from typing import Dict, Any, Union, List, Optional


def validate_and_process_user(data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Demonstrate the Guard Clause (Early Return) pattern.

    Instead of deep nesting with multiple `if/else` blocks, guard clauses
    check validation failure conditions first and return early, keeping the
    happy path unindented and readable.

    Args:
        data: Dictionary of user input data or None.

    Returns:
        A dictionary containing processing results and status flag.
    """
    # Guard 1: Null check
    if data is None:
        return {"status": "error", "message": "Input data cannot be None"}

    # Guard 2: Required field validation
    if "username" not in data or not data["username"]:
        return {"status": "error", "message": "Missing required field: username"}

    # Guard 3: Age limit check
    age = data.get("age", 0)
    if not isinstance(age, (int, float)) or age < 18:
        return {"status": "error", "message": "User must be at least 18 years old"}

    # Main business logic execution (unindented happy path)
    normalized_username = str(data["username"]).strip().lower()
    return {
        "status": "success",
        "message": "User processed successfully",
        "processed_data": {
            "username": normalized_username,
            "age": int(age),
            "is_active": True,
        },
    }


def inspect_return_object(obj: Any) -> List[str]:
    """Demonstrate dir() introspection on function return values.

    Args:
        obj: Any returned Python object.

    Returns:
        List of non-dunder attribute and method names available on the object.
    """
    attributes = dir(obj)
    # Filter out private double-underscore (dunder) methods for clear inspection
    public_attributes = [attr for attr in attributes if not attr.startswith("__")]
    return public_attributes


if __name__ == "__main__":
    print("=== Python Return Patterns & Best Practices ===")

    # 1. Testing Guard Clause validation returns
    test_inputs = [
        None,
        {},
        {"username": "  Alice  ", "age": 16},
        {"username": "  Bob  ", "age": 25},
    ]

    for sample in test_inputs:
        res = validate_and_process_user(sample)
        print(f"Input: {sample} -> Result: {res}")

    # 2. Introspection of returned objects using dir()
    print("\n--- Return Object Introspection with dir() ---")
    str_attrs = inspect_return_object("Python Return Tutorial")
    print(f"Public methods on returned str (first 5): {str_attrs[:5]}")

    dict_attrs = inspect_return_object({"key": "value"})
    print(f"Public methods on returned dict: {dict_attrs}")
