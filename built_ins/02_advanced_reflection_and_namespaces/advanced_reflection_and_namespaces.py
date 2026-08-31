"""
Advanced Reflection, Introspection, and Namespace Management Module.

This module demonstrates advanced Python dynamic reflection techniques:
- `dir()` introspection filtering for core types (`dict`, `list`, `str`, `tuple`)
- `globals()` and `locals()` runtime namespace dictionary inspection
- Dynamic attribute access via `getattr()`, `hasattr()`, `setattr()`
- Practical mathematical solver: Newton's Method for Square Roots using built-in `abs()`

PEP 8 compliant, type-annotated, compatible with Python 2.7 - 3.13.
"""

import math
from typing import Any, Dict, List, Optional


def inspect_type_methods(target_type: type) -> List[str]:
    """
    Retrieves public (non-dunder) methods and attributes for a given type using dir().

    Args:
        target_type (type): Python class or primitive type (e.g. str, list, dict).

    Returns:
        List[str]: Alphabetical list of public attribute and method names.
    """
    return [attr for attr in dir(target_type) if not attr.startswith("__")]


def get_current_namespace_summary(scope_dict: Dict[str, Any]) -> Dict[str, str]:
    """
    Summarizes key-value types in a namespace dictionary (globals() or locals()).

    Args:
        scope_dict (Dict[str, Any]): Scope dictionary (globals() or locals()).

    Returns:
        Dict[str, str]: Map of variable names to their type representation names.
    """
    summary: Dict[str, str] = {}
    for key, value in scope_dict.items():
        if not key.startswith("__"):
            summary[key] = type(value).__name__
    return summary


def newton_square_root(number: float, tolerance: float = 1e-7, max_iterations: int = 100) -> float:
    """
    Computes square root of a non-negative number using Newton's Iterative Method.

    Demonstrates practical usage of the built-in `abs()` function for checking
    convergence delta (|guess^2 - number| < tolerance).

    Args:
        number (float): Target non-negative number.
        tolerance (float): Convergence threshold (default: 1e-7).
        max_iterations (int): Maximum convergence loop steps.

    Returns:
        float: Computed square root approximation.

    Raises:
        ValueError: If input number is negative.
    """
    if number < 0:
        raise ValueError(f"Cannot compute real square root of negative number: {number}")
    if number == 0:
        return 0.0

    guess = number / 2.0
    for _ in range(max_iterations):
        if abs(guess * guess - number) < tolerance:
            break
        guess = (guess + number / guess) / 2.0

    return round(guess, 6)


class DynamicAttributeContainer:
    """Demonstrates dynamic attribute creation and retrieval using hasattr/getattr/setattr."""

    def __init__(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def safe_get(self, attribute_name: str, default: Any = None) -> Any:
        """Safely retrieves an attribute if it exists, otherwise returns default."""
        if hasattr(self, attribute_name):
            return getattr(self, attribute_name)
        return default


if __name__ == "__main__":
    print("Public Methods on 'dict':", inspect_type_methods(dict)[:8])
    print("Public Methods on 'str' :", inspect_type_methods(str)[:8])

    print("\nNewton's Method Square Root Verification:")
    print("  sqrt(25.0) =", newton_square_root(25.0))
    print("  sqrt(2.0)  =", newton_square_root(2.0))
    print("  math.sqrt(2.0) =", round(math.sqrt(2.0), 6))
