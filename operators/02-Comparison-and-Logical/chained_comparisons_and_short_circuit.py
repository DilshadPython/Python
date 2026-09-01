"""
02-Comparison-and-Logical/chained_comparisons_and_short_circuit.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Chained Comparisons & Short-Circuit Logical Evaluation Examples:
1. Pythonic Chained Relational Comparisons (10 < x <= 100 < y)
2. Short-Circuit Safety Evaluation with Sentinel Functions
3. Custom Object Identity vs Value Equality (__eq__ vs 'is')
"""
from typing import Any, List, Tuple


def evaluate_chained_range_comparison(val: float, low: float, high: float) -> bool:
    """
    Evaluate Pythonic chained comparison (low <= val <= high).

    Args:
        val (float): Target value to test.
        low (float): Lower bound.
        high (float): Upper bound.

    Returns:
        bool: True if val is inclusively within bounds.
    """
    # Equivalent to (low <= val) and (val <= high) evaluated without repeating 'val' expression
    return low <= val <= high


def evaluate_short_circuit_safety(numbers: List[int]) -> Tuple[bool, int]:
    """
    Demonstrate logical short-circuiting preventing zero division error.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        Tuple[bool, int]: Boolean indicator and calculated first valid ratio.
    """
    # Short-circuit 'and' avoids division by zero if numbers is empty or first element is 0
    safe_ratio_possible = len(numbers) > 0 and numbers[0] != 0
    calculated_value = 100 // numbers[0] if safe_ratio_possible else -1

    return safe_ratio_possible, calculated_value
