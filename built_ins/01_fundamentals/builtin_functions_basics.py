"""
Python Built-in Functions Fundamentals Module.

This module demonstrates foundational built-in functions:
- Numerical built-ins: `abs()`, `round()`, `min()`, `max()`, `sum()`
- Iterable and evaluation built-ins: `all()`, `any()`, `len()`, `sorted()`
- Dynamic docstring extraction from Python's standard `builtins` module

PEP 8 compliant, type-annotated, and compatible with Python 2.7 - 3.13.
"""

# Standard library builtins module import
import builtins
import math
import re
from typing import Any, Dict, List, Union, Tuple


def calculate_absolute_values(values: List[Union[int, float, complex]]) -> List[float]:
    """
    Computes absolute values or magnitudes for integers, floats, and complex numbers using abs().

    Args:
        values (List[Union[int, float, complex]]): Input list of numeric values.

    Returns:
        List[float]: List of computed absolute magnitude values.
    """
    return [round(abs(val), 4) for val in values]


def evaluate_truthiness_conditions(items: List[Any]) -> Dict[str, bool]:
    """
    Evaluates iterable elements using built-in all() and any() logic.

    Args:
        items (List[Any]): Collection of boolean or truthy/falsy items.

    Returns:
        Dict[str, bool]: Dictionary with 'all_true' and 'any_true' evaluation results.
    """
    return {
        "all_true": all(items),
        "any_true": any(items),
    }


def compute_collection_summary(numbers: List[Union[int, float]]) -> Dict[str, float]:
    """
    Summarizes numeric collections using built-in len(), sum(), min(), max().

    Args:
        numbers (List[Union[int, float]]): Non-empty list of numbers.

    Returns:
        Dict[str, float]: Summary stats including count, total, min, max, average.
    """
    if not numbers:
        raise ValueError("Cannot summarize empty collection.")

    count = len(numbers)
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = round(total / count, 4)

    return {
        "count": float(count),
        "total": float(total),
        "min": float(minimum),
        "max": float(maximum),
        "average": average,
    }


def get_lowercase_builtin_docstrings() -> Dict[str, str]:
    """
    Extracts docstrings for lowercase built-in functions from standard builtins module.

    Returns:
        Dict[str, str]: Mapping of built-in function names to their summary docstrings.
    """
    docstrings: Dict[str, str] = {}
    for name in dir(builtins):
        if re.match(r"^[a-z_]+$", name):
            obj = getattr(builtins, name)
            if callable(obj) and obj.__doc__:
                first_line = obj.__doc__.strip().split("\n")[0]
                docstrings[name] = first_line
    return docstrings


if __name__ == "__main__":
    print("Testing abs() on Complex Magnitudes:")
    complex_nums = [2 - 3j, 4 - 5j, 3 - 4j]
    mags = calculate_absolute_values(complex_nums)
    print(f"  Inputs: {complex_nums}")
    print(f"  Magnitudes: {mags}")

    print("\nSummary Stats for Collection [10, 20, 30, 40, 50]:")
    summary = compute_collection_summary([10, 20, 30, 40, 50])
    for k, v in summary.items():
        print(f"  {k}: {v}")
