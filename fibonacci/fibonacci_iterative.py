"""
Fibonacci Algorithms: Iterative Generation

This module demonstrates calculating Fibonacci numbers iteratively using variable
swapping (`a, b = b, a + b`), achieving optimal $O(N)$ time complexity and $O(1)$ space complexity.

Mathematical Definition:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n >= 2
"""
from typing import List


def get_fibonacci_nth(n: int) -> int:
    """
    Computes the n-th Fibonacci number iteratively.

    Args:
        n (int): The index of the Fibonacci number (0-indexed).

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def generate_fibonacci_sequence(count: int) -> List[int]:
    """
    Generates a list of the first `count` Fibonacci numbers.

    Args:
        count (int): Number of terms to generate.

    Returns:
        List[int]: List containing Fibonacci numbers.

    Raises:
        ValueError: If count is negative.
    """
    if count < 0:
        raise ValueError("Count cannot be negative.")
    if count == 0:
        return []
    if count == 1:
        return [0]

    sequence = [0, 1]
    a, b = 0, 1
    for _ in range(2, count):
        a, b = b, a + b
        sequence.append(b)
    return sequence


def main() -> None:
    """Demonstrates iterative Fibonacci calculation."""
    print("=" * 60)
    print("1. Iterative Fibonacci Sequence Generation ($O(N)$ time, $O(1)$ space)")
    print("=" * 60)

    # 1. Compute specific n-th Fibonacci term
    n = 10
    fib_n = get_fibonacci_nth(n)
    print(f"  F({n}) = {fib_n}")

    # 2. Generate sequence of first 15 terms
    terms = 15
    seq = generate_fibonacci_sequence(terms)
    print(f"  First {terms} terms: {seq}")


if __name__ == "__main__":
    main()
