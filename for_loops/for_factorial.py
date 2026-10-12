"""Iterative Factorial Calculation via 'for' Loop.

Calculates the factorial (n! = n * (n - 1) * ... * 1) of a non-negative integer
using an iterative accumulator inside a 'for' loop.

Import Notes:
    - 'from typing import Optional': Standard library typing import for optional type annotations.
"""

from typing import Optional


def calculate_factorial(num: int) -> int:
    """Calculate the factorial of a non-negative integer iteratively.

    Args:
        num: Non-negative integer whose factorial is to be computed.

    Returns:
        The computed factorial integer.

    Raises:
        ValueError: If num is negative.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    factorial_result = 1
    for i in range(1, num + 1):
        factorial_result *= i

    print(f"{num}! = {factorial_result}")
    return factorial_result


def demo_for_factorial(input_num: Optional[int] = 5) -> int:
    """Execute demonstration of iterative factorial calculation.

    Args:
        input_num: Optional integer to compute factorial for (default: 5).

    Returns:
        The computed factorial integer.
    """
    target = input_num if input_num is not None else 5
    print(f"--- Calculating Factorial for n = {target} ---")
    return calculate_factorial(target)


if __name__ == "__main__":
    demo_for_factorial()
