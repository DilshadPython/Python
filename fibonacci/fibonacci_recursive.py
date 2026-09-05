"""
Fibonacci Algorithms: Naive Recursive Approach ($O(2^N)$ Time)

This module demonstrates the naive top-down recursive implementation of the
Fibonacci sequence.

Mathematical & Complexity Analysis:
- Time Complexity: $O(2^N)$ exponential due to redundant re-computation of subproblems.
- Space Complexity: $O(N)$ auxiliary stack space.
- Demonstrates why un-memoized recursion fails for $N > 35$.
"""
import time
from typing import Tuple


def fibonacci_recursive(n: int) -> int:
    """
    Computes the n-th Fibonacci number using naive recursion.

    Args:
        n (int): The Fibonacci term index.

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

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def benchmark_recursive_execution(n: int) -> Tuple[int, float]:
    """
    Measures the execution time of naive recursive calculation.

    Args:
        n (int): The term to calculate.

    Returns:
        Tuple[int, float]: (Result, elapsed time in seconds).
    """
    start_time = time.perf_counter()
    result = fibonacci_recursive(n)
    elapsed = time.perf_counter() - start_time
    return result, elapsed


def main() -> None:
    """Demonstrates recursive Fibonacci performance curve."""
    print("=" * 60)
    print("2. Naive Recursive Fibonacci ($O(2^N)$ Exponential Time)")
    print("=" * 60)

    print("\nBenchmarking exponential runtime growth:")
    for term in [10, 20, 30, 35]:
        val, duration = benchmark_recursive_execution(term)
        print(f"  F({term:2d}) = {val:<10d} (Time: {duration:8.5f} seconds)")

    print("\nNote: Calculating F(40+) without memoization takes tens of seconds due to $O(2^N)$ subproblems.")


if __name__ == "__main__":
    main()
