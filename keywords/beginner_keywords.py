"""
Beginner Level Python Keywords Demonstration Module.

This module provides clear, well-commented examples of fundamental Python reserved keywords
designed for beginner developers (`if`, `else`, `elif`, `for`, `while`, `def`, `return`, `try`, `except`, `in`, `is`, `and`, `or`, `not`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI exit codes.
# - `from typing import Dict, List, Union`: PEP 484 type hints for beginners.
# =========================================================================
import sys
from typing import Dict, List, Union


def demonstrate_control_flow(score: int) -> str:
    """Demonstrate decision-making keywords: `if`, `elif`, `else`, `return`.

    Args:
        score (int): Test score integer between 0 and 100.

    Returns:
        str: Grade description string.
    """
    if score >= 90:
        return "Grade A: Excellent"
    elif score >= 75:
        return "Grade B: Good"
    elif score >= 60:
        return "Grade C: Satisfactory"
    else:
        return "Grade F: Needs Improvement"


def demonstrate_loops(items_count: int) -> List[int]:
    """Demonstrate iteration keywords: `for`, `in`, `while`.

    Args:
        items_count (int): Number of items to iterate.

    Returns:
        List[int]: Generated squared numbers list.
    """
    squares: List[int] = []

    # `for` loop iterating through a range sequence (`in` keyword)
    for i in range(items_count):
        squares.append(i * i)

    # `while` loop countdown
    counter = items_count
    while counter > 0:
        counter -= 1

    return squares


def demonstrate_boolean_logic(is_active: bool, is_verified: bool) -> Dict[str, bool]:
    """Demonstrate logical operator keywords: `and`, `or`, `not`, `is`.

    Args:
        is_active (bool): User active status.
        is_verified (bool): User email verification status.

    Returns:
        Dict[str, bool]: Calculated boolean evaluation results.
    """
    return {
        "can_login": is_active and is_verified,
        "needs_attention": (not is_active) or (not is_verified),
        "is_active_check": is_active is True,
    }


def demonstrate_error_handling(raw_input: str) -> Union[float, str]:
    """Demonstrate exception handling keywords: `try`, `except`.

    Args:
        raw_input (str): User input string to convert to float.

    Returns:
        Union[float, str]: Converted float number or error string message.
    """
    try:
        converted_value = float(raw_input)
        return converted_value
    except ValueError:
        return f"Error: Cannot convert '{raw_input}' to float number."


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner keywords demonstration."""
    print("=== Beginner Level Python Keywords Demonstration ===")
    print("Control Flow:", demonstrate_control_flow(85))
    print("Loop Squares:", demonstrate_loops(5))
    print("Boolean Logic:", demonstrate_boolean_logic(True, False))
    print("Error Handling:", demonstrate_error_handling("42.5"))
    print("Error Handling Invalid:", demonstrate_error_handling("invalid_number"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
