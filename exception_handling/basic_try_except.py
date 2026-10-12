"""
Python Exception Handling: Basic `try-except` Blocks

This module demonstrates basic exception handling for standard Python runtime
errors including `ZeroDivisionError`, `ValueError`, `KeyError`, and `IndexError`.

Key Concepts:
- `try`: Encloses code that may raise an exception during execution.
- `except ExceptionType`: Traps specific exceptions and provides graceful fallback logic.
"""
from typing import Any, Dict, List, Optional


def safe_divide(numerator: float, denominator: float) -> Optional[float]:
    """
    Safely divides two numbers, catching ZeroDivisionError.

    Args:
        numerator (float): The dividend.
        denominator (float): The divisor.

    Returns:
        Optional[float]: The quotient float, or None if division by zero occurred.
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print(f"Error: Cannot divide {numerator} by zero!")
        return None


def safe_parse_int(value: str) -> Optional[int]:
    """
    Safely converts a string to an integer, catching ValueError.

    Args:
        value (str): The input string to parse.

    Returns:
        Optional[int]: Parsed integer, or None if conversion failed.
    """
    try:
        return int(value)
    except ValueError:
        print(f"Error: Cannot parse string '{value}' as an integer.")
        return None


def safe_get_dict_key(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    """
    Safely retrieves a dictionary key, catching KeyError.

    Args:
        data (Dict[str, Any]): The target dictionary.
        key (str): The lookup key.
        default (Any): Fallback value if key is missing.

    Returns:
        Any: Value corresponding to key, or default fallback.
    """
    try:
        return data[key]
    except KeyError:
        print(f"Warning: Key '{key}' not found in dictionary.")
        return default


def safe_get_list_element(items: List[Any], index: int, default: Any = None) -> Any:
    """
    Safely accesses a list element by index, catching IndexError.

    Args:
        items (List[Any]): Target list.
        index (int): Target element index.
        default (Any): Fallback value if index out of bounds.

    Returns:
        Any: List element at index, or default fallback.
    """
    try:
        return items[index]
    except IndexError:
        print(f"Warning: Index {index} is out of bounds for list of length {len(items)}.")
        return default


def main() -> None:
    """Demonstrates basic exception handling functions."""
    print("=" * 60)
    print("1. Basic Exception Handling (`try-except`) Demonstrations")
    print("=" * 60)

    # 1. Division by Zero
    res_div = safe_divide(10.0, 0.0)
    print(f"  safe_divide(10.0, 0.0) -> {res_div}")

    # 2. Invalid Integer Conversion
    res_int = safe_parse_int("abc")
    print(f"  safe_parse_int('abc') -> {res_int}")

    # 3. Missing Dictionary Key
    ages = {"adam": 33, "tom": 21}
    res_dict = safe_get_dict_key(ages, "alice", default=0)
    print(f"  safe_get_dict_key(ages, 'alice') -> {res_dict}")

    # 4. Out of Bounds List Access
    colors = ["red", "green", "blue"]
    res_list = safe_get_list_element(colors, 5, default="unknown")
    print(f"  safe_get_list_element(colors, 5) -> {res_list}")


if __name__ == "__main__":
    main()
