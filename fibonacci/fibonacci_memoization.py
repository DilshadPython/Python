"""
Fibonacci Algorithms: Explicit Memoization (Dynamic Programming)

This module demonstrates optimizing recursive Fibonacci calculations by storing
previously calculated values in an explicit lookup dictionary (`_fib_cache`).

Complexity:
- Time Complexity: Reduced from $O(2^N)$ to $O(N)$ linear time.
- Space Complexity: $O(N)$ for memory storage of cache entries.
"""
from typing import Dict, Tuple

# Explicit module-level dictionary cache
_fib_cache: Dict[int, int] = {0: 0, 1: 1}


def fibonacci_memoized(n: int) -> int:
    """
    Computes the n-th Fibonacci number using explicit dictionary memoization.

    Args:
        n (int): The Fibonacci term index.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative.")

    # 1. Return cached result if already calculated
    if n in _fib_cache:
        return _fib_cache[n]

    # 2. Compute subproblems recursively and store result in cache
    result = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    _fib_cache[n] = result
    return result


def clear_cache() -> None:
    """Clears the explicit memoization cache."""
    global _fib_cache
    _fib_cache = {0: 0, 1: 1}


def get_cache_size() -> int:
    """Returns the current number of cached Fibonacci terms."""
    return len(_fib_cache)


def main() -> None:
    """Demonstrates explicit memoized Fibonacci calculation."""
    print("=" * 60)
    print("3. Explicit Dictionary Memoization ($O(N)$ Time)")
    print("=" * 60)

    # Calculate large terms instantaneously
    target_terms = [10, 50, 100, 300]
    print("\nCalculating large Fibonacci numbers with dynamic programming cache:")
    for term in target_terms:
        val = fibonacci_memoized(term)
        print(f"  F({term:3d}) = {val}")

    print(f"\nTotal unique Fibonacci values cached in memory: {get_cache_size()}")


if __name__ == "__main__":
    main()
