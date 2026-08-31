"""Advanced Conditional Expressions (Ternary Operators) in Python.

This module demonstrates conditional expressions (commonly known as the ternary
operator) in Python: `x if condition else y`.

Import Notes:
    - 'import sys': Imports the full 'sys' standard library module namespace.
      Accessing attributes via 'sys.version_info' avoids namespace pollution.
    - 'from typing import Tuple, Union': Imports specific type hint constructs directly
      into the local namespace for cleaner function signatures.
"""

import sys
from typing import Tuple, Union


def get_minimum_value(first_val: int, second_val: int) -> int:
    """Return the minimum of two numbers using a ternary conditional expression.
    
    Syntax: <result_if_true> if <condition> else <result_if_false>
    """
    # Ternary expression evaluates 'first_val < second_val'
    # Returns 'first_val' if True, otherwise returns 'second_val'
    minimum_value = first_val if first_val < second_val else second_val
    return minimum_value


def classify_number_ternary(number: Union[int, float]) -> str:
    """Classify a number using nested ternary conditional expressions.
    
    Pythonic recommendation: Limit ternary nesting to 1-2 levels for readability.
    """
    # Inline nested ternary expression: positive check -> negative check -> fallback zero
    return "Positive" if number > 0 else ("Negative" if number < 0 else "Zero")


def demo_advance_if() -> Tuple[int, str]:
    """Execute demonstration of advanced ternary conditional evaluation."""
    first_num, second_num = 50, 25
    result_minimum = get_minimum_value(first_num, second_num)
    print(f"Minimum between {first_num} and {second_num}: {result_minimum}")

    sample_val = -10
    classification = classify_number_ternary(sample_val)
    print(f"Classification of {sample_val}: {classification}")

    return result_minimum, classification


if __name__ == "__main__":
    # Display Python runtime version information
    print(f"Executing on Python {sys.version_info.major}.{sys.version_info.minor}")
    demo_advance_if()