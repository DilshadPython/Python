"""Number Divisibility and Parity Evaluator.

Demonstrates evaluating integer properties (even, divisible by 3 and 5, odd)
using chained 'if-elif-else' conditions.

Import Notes:
    - 'from typing import List': Standard library typing import for list parameter typing.
"""

from typing import List


def evaluate_number_properties(number: int) -> str:
    """Classify integer parity and divisibility."""
    if number % 3 == 0 and number % 5 == 0:
        return f"The number {number} is divisible by both 3 and 5 (Multi-divisible)."
    elif number % 2 == 0:
        return f"The number {number} is an Even number."
    else:
        return f"The number {number} is an Odd number."


def demo_if_then() -> None:
    """Run divisibility evaluation demonstration."""
    sample_numbers: List[int] = [15, 4, 7, 30, 9]
    for num in sample_numbers:
        print(evaluate_number_properties(num))


if __name__ == "__main__":
    demo_if_then()
