"""
cloud_app/tutorials/lambda_basics.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Comprehensive, PEP 8 compliant tutorial module demonstrating Python Lambda Functions.

This module provides a structured 3-tier pedagogical architecture for understanding:
1. Anonymous inline single-expression syntax (lambda arguments: expression).
2. Fundamental arithmetic, string transformation, and custom sorting with key=lambda.
3. First-class object dispatch tables and higher-order functional pipelines (map, filter, reduce).
4. CPython reflection matrix (dir(lambda) dunder attributes and methods).
5. Performance benchmarks, range() iterator integration, and Python 2.7 to 3.13 evolution.
"""

# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import math: Standard library module for mathematical constants and guards (math.isnan).
# - import functools: Standard library module for higher-order function utilities (functools.reduce).
# - from typing import Any, Callable, Dict, List, Tuple, Union: Type annotations for strict type checking.
# =========================================================================
import functools
import math
from typing import Any, Callable, Dict, List, Tuple, Union

# ── 1. Fundamental Arithmetic Lambda Expressions ──────────────────────────────

# Single-parameter addition & subtraction
add_eight: Callable[[Union[int, float]], Union[int, float]] = lambda num: num + 8
add_two_numbers: Callable[[Union[int, float], Union[int, float]], Union[int, float]] = lambda x, y: x + y

subtract_eight: Callable[[Union[int, float]], Union[int, float]] = lambda num: num - 8
subtract_two_numbers: Callable[[Union[int, float], Union[int, float]], Union[int, float]] = lambda a, b: a - b

# Single & multi-parameter multiplication & division
multiply_by_82: Callable[[Union[int, float]], Union[int, float]] = lambda num: num * 82
multiply_two_numbers: Callable[[Union[int, float], Union[int, float]], Union[int, float]] = lambda a, b: a * b

divide_by_eight: Callable[[Union[int, float]], float] = lambda num: num / 8.0
divide_two_numbers: Callable[[Union[int, float], Union[int, float]], float] = (
    lambda a, b: a / b if b != 0 else float("nan")
)

# Exponentiation & modulus remainder operations
power_of_nine: Callable[[Union[int, float]], Union[int, float]] = lambda num: num ** 9
power_base_exp: Callable[[Union[int, float], Union[int, float]], Union[int, float]] = lambda base, exp: base ** exp

remainder_by_eight: Callable[[int], int] = lambda num: num % 8
remainder_two_integers: Callable[[int, int], int] = lambda a, b: a % b if b != 0 else 0


# ── 2. String Transformation & Custom Key Sorting ─────────────────────────────

format_full_name_string: Callable[[str], str] = lambda name: f"{name.strip().title()} Smith"

format_full_name: Callable[[str, str], str] = lambda fname, lname: f"{fname.strip().title()} {lname.strip().title()}"


def sort_names_by_last_name(names: List[str]) -> List[str]:
    """Sort a list of full name strings by last name using key=lambda.

    Args:
        names: List of full name strings.

    Returns:
        New sorted list of names ordered alphabetically by last name.
    """
    if not isinstance(names, list):
        raise TypeError("Input names must be a list of strings.")
    return sorted(names, key=lambda name: name.strip().split()[-1].lower())


# ── 3. Dispatch Tables & Higher-Order Functional Pipelines ───────────────────

CALCULATOR_DISPATCH: Dict[str, Callable[[Union[int, float], Union[int, float]], Union[int, float]]] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else float("nan"),
    "**": lambda a, b: a ** b,
    "%": lambda a, b: a % b if b != 0 else 0,
}


def calculate_dispatch(op: str, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Execute arithmetic operation using dictionary dispatch table of lambdas.

    Args:
        op: Operator symbol string ('+', '-', '*', '/', '**', '%').
        a: First numeric operand.
        b: Second numeric operand.

    Returns:
        Computed numeric result.
    """
    if op not in CALCULATOR_DISPATCH:
        raise ValueError(f"Unsupported operator '{op}'. Valid: {list(CALCULATOR_DISPATCH.keys())}")
    return CALCULATOR_DISPATCH[op](a, b)


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """Filter even integers using built-in filter() and a lambda expression.

    Args:
        numbers: Sequence of integers.

    Returns:
        List containing only even integers.
    """
    if not isinstance(numbers, (list, tuple, range)):
        raise TypeError("Input numbers must be a list, tuple, or range.")
    return list(filter(lambda x: x % 2 == 0, numbers))


def map_square_numbers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """Transform sequence of numbers into squares using map() and a lambda expression.

    Args:
        numbers: Sequence of numbers.

    Returns:
        List containing squared numbers.
    """
    if not isinstance(numbers, (list, tuple, range)):
        raise TypeError("Input numbers must be a list, tuple, or range.")
    return list(map(lambda x: x ** 2, numbers))


def reduce_product_numbers(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Cumulative product of numbers using functools.reduce() and a lambda expression.

    Args:
        numbers: Sequence of numbers.

    Returns:
        Cumulative product value.
    """
    if not isinstance(numbers, (list, tuple, range)):
        raise TypeError("Input numbers must be a list, tuple, or range.")
    if not numbers:
        raise ValueError("Cannot reduce an empty sequence.")
    return functools.reduce(lambda acc, val: acc * val, numbers)


# ── 4. Reflection Matrix: Lambda Attributes & Dunder Methods ──────────────────

def inspect_lambda_attributes_and_methods(func: Callable = None) -> Dict[str, Any]:
    """Inspect and categorize all attributes and dunder methods of a lambda function.

    Args:
        func: Optional function to inspect (defaults to a sample lambda x, y: x + y).

    Returns:
        Structured dictionary breaking down internal function reflection attributes.
    """
    if func is None:
        func = lambda x, y: x + y

    all_dir_attrs = dir(func)

    reflection_attrs = {
        "__name__": getattr(func, "__name__", None),
        "__qualname__": getattr(func, "__qualname__", None),
        "__doc__": getattr(func, "__doc__", None),
        "__module__": getattr(func, "__module__", None),
        "__annotations__": getattr(func, "__annotations__", {}),
        "__defaults__": getattr(func, "__defaults__", None),
        "__kwdefaults__": getattr(func, "__kwdefaults__", None),
        "__closure__": str(getattr(func, "__closure__", None)),
        "__code__": str(getattr(func, "__code__", None)),
        "__globals_keys__": list(getattr(func, "__globals__", {}).keys())[:8],
        "__dict__": getattr(func, "__dict__", {}),
    }

    callable_methods = [
        attr for attr in all_dir_attrs if callable(getattr(func, attr, None))
    ]

    return {
        "func_repr": repr(func),
        "total_attributes": len(all_dir_attrs),
        "dir_attributes": all_dir_attrs,
        "reflection_attrs": reflection_attrs,
        "callable_methods": callable_methods,
        "is_anonymous": getattr(func, "__name__") == "<lambda>",
    }


# ── 5. Studio Sub-Pane Demonstrations ─────────────────────────────────────────

def demonstrate_arithmetic_lambdas() -> Dict[str, Any]:
    """Run basic arithmetic lambda demonstrations."""
    return {
        "add_eight(12)": add_eight(12),
        "add_two_numbers(15, 27)": add_two_numbers(15, 27),
        "subtract_eight(50)": subtract_eight(50),
        "subtract_two_numbers(100, 35)": subtract_two_numbers(100, 35),
        "multiply_by_82(5)": multiply_by_82(5),
        "multiply_two_numbers(12, 8)": multiply_two_numbers(12, 8),
        "divide_by_eight(64)": divide_by_eight(64),
        "divide_two_numbers(45, 9)": divide_two_numbers(45, 9),
        "divide_two_numbers(10, 0)": "NaN (Guarded)",
        "power_of_nine(2)": power_of_nine(2),
        "power_base_exp(3, 4)": power_base_exp(3, 4),
        "remainder_by_eight(29)": remainder_by_eight(29),
        "remainder_two_integers(43, 6)": remainder_two_integers(43, 6),
    }


def demonstrate_string_lambdas() -> Dict[str, Any]:
    """Run string formatting and sorting demonstrations."""
    raw_names = ["Guido van Rossum", "Ada Lovelace", "Linus Torvalds", "Grace Hopper"]
    sorted_names = sort_names_by_last_name(raw_names)
    return {
        'format_full_name_string("  john ")': format_full_name_string("  john "),
        'format_full_name("  dilshad ", "  python ")': format_full_name("  dilshad ", "  python "),
        "original_names": raw_names,
        "sorted_by_last_name": sorted_names,
    }


def demonstrate_dispatch_and_higher_order() -> Dict[str, Any]:
    """Run dictionary dispatch table and map/filter/reduce demonstrations."""
    sample_range = range(1, 11)
    evens = filter_even_numbers(list(sample_range))
    squares = map_square_numbers(list(range(1, 6)))
    product = reduce_product_numbers([1, 2, 3, 4, 5])
    return {
        "dispatch_+": calculate_dispatch("+", 10, 20),
        "dispatch_-": calculate_dispatch("-", 50, 15),
        "dispatch_*": calculate_dispatch("*", 6, 7),
        "dispatch_/": calculate_dispatch("/", 81, 9),
        "dispatch_**": calculate_dispatch("**", 2, 5),
        "dispatch_%": calculate_dispatch("%", 29, 4),
        "input_range": list(sample_range),
        "filtered_evens": evens,
        "mapped_squares": squares,
        "reduced_product": product,
    }


if __name__ == "__main__":
    print("=== Lambda Functions Tutorial Module ===")
    print("Arithmetic:", demonstrate_arithmetic_lambdas())
    print("String:", demonstrate_string_lambdas())
    print("Dispatch:", demonstrate_dispatch_and_higher_order())
    print("Inspection:", inspect_lambda_attributes_and_methods())
