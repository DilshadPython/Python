"""Basic Conditional Statements: Numeric Magnitude Comparison.

Demonstrates simple 'if' statements evaluating numeric inequalities.

Import Notes:
    - 'from typing import Tuple': Imports 'Tuple' from 'typing' to type-annotate
      function parameter pairs and return values.
"""

from typing import Tuple


def compare_numbers(first_num: int, second_num: int) -> str:
    """Compare two numbers and return a descriptive comparison string."""
    if first_num < second_num:
        return f"{first_num} is strictly lower than {second_num}"
    elif first_num > second_num:
        return f"{first_num} is strictly greater than {second_num}"
    else:
        return f"{first_num} and {second_num} are equal"


def demo_if_1() -> None:
    """Run basic magnitude comparison demonstration."""
    num_a, num_b = 23, 30
    comparison_message = compare_numbers(num_a, num_b)
    print(f"Comparison Result: {comparison_message}")


if __name__ == "__main__":
    demo_if_1()
