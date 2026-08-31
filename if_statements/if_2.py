"""Basic Conditional Statements: String Equality Comparison.

Demonstrates evaluating string equality using the '==' value comparison operator.

Import Notes:
    - 'from typing import Union': Demonstrates type hints supporting string inputs.
"""

from typing import Union


def verify_string_match(first_str: str, second_str: str) -> bool:
    """Check if two string values are identical.
    
    Pythonic note: 'first_str == second_str' directly returns a boolean.
    The 'if' statement structure here illustrates explicit boolean branching.
    """
    if first_str == second_str:
        return True
    return False


def demo_if_2() -> None:
    """Demonstrate string equality checking."""
    greeting_a = "Hello"
    greeting_b = "Hello"
    is_match = verify_string_match(greeting_a, greeting_b)
    print(f"Strings '{greeting_a}' and '{greeting_b}' match: {is_match}")


if __name__ == "__main__":
    demo_if_2()
