"""String Type Conversion and Inspection Operations Module.

Provides functions demonstrating safe type casting between numbers and strings (`str`, `int`, `float`),
string representations (`repr`, `ascii`), and runtime type inspection (`type`, `isinstance`).
"""

from typing import Any, Dict, Tuple


def convert_to_string(value: Any) -> str:
    """Convert any Python value into a string using `str()`.

    Args:
        value: Any Python object.

    Returns:
        Human-readable string representation.
    """
    return str(value)


def get_string_representation(value: Any) -> str:
    """Get unambiguous developer string representation using `repr()`.

    Args:
        value: Any Python object.

    Returns:
        Canonical developer string representation.
    """
    return repr(value)


def inspect_variable_type(value: Any) -> Dict[str, Any]:
    """Inspect type metadata and type assertions for a given value.

    Args:
        value: Value to inspect.

    Returns:
        Dictionary containing type name, str representation, and boolean type checks.
    """
    return {
        "value": value,
        "type_name": type(value).__name__,
        "is_str": isinstance(value, str),
        "is_int": isinstance(value, int),
        "is_float": isinstance(value, float),
        "is_list": isinstance(value, list),
    }


def convert_int_and_float_strings(num_str: str) -> Tuple[int, float]:
    """Safely convert numeric string representation into `int` and `float`.

    Args:
        num_str: String representation of a number.

    Returns:
        Tuple of (integer_value, float_value).
    """
    float_val = float(num_str)
    int_val = int(float_val)
    return int_val, float_val


def main() -> None:
    """Demonstrate type conversion and inspection operations."""
    print("--- Type Conversion & Inspection Operations ---")

    # 1. str() vs repr()
    sample_text = "Python\nDevelopment"
    print(f"[str()]  {convert_to_string(sample_text)}")
    print(f"[repr()] {get_string_representation(sample_text)}")

    # 2. Type inspection
    sample_list = [1, 2, 3]
    type_info = inspect_variable_type(sample_list)
    print(f"\n[inspect_type] Metadata for list: {type_info}")

    # 3. Numeric string conversions
    num_str = "123.45"
    i_val, f_val = convert_int_and_float_strings(num_str)
    print(f"\n[conversions] String '{num_str}' -> int={i_val}, float={f_val}")


if __name__ == "__main__":
    main()
