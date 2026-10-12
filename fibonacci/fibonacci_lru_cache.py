"""
Fibonacci Algorithms: Built-in `@functools.lru_cache` Decorator

This module demonstrates memoization using Python's standard library
`@functools.lru_cache` (Least Recently Used cache) decorator.

Decorator Methods & Introspection:
- `@lru_cache(maxsize=128)`: Wraps function to cache return values.
- `func.cache_info()`: Returns cache statistics (`hits`, `misses`, `maxsize`, `currsize`).
- `func.cache_clear()`: Clears the LRU cache contents.
"""
from functools import lru_cache
from typing import NamedTuple


@lru_cache(maxsize=500)
def fibonacci_lru(n: int) -> int:
    """
    Computes the n-th Fibonacci number using built-in LRU memoization cache.

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

    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def main() -> None:
    """Demonstrates @lru_cache memoization and cache statistics introspection."""
    print("=" * 60)
    print("4. Built-in `@functools.lru_cache` Decorator")
    print("=" * 60)

    # 1. Compute values
    terms = [20, 50, 100, 200]
    print("\nComputing terms using `@lru_cache`:")
    for t in terms:
        val = fibonacci_lru(t)
        print(f"  F({t:3d}) = {val}")

    # 2. Inspect LRU Cache statistics
    info = fibonacci_lru.cache_info()
    print("\nLRU Cache Statistics (`fibonacci_lru.cache_info()`):")
    print(f"  Cache Hits:   {info.hits}")
    print(f"  Cache Misses: {info.misses}")
    print(f"  Max Size:     {info.maxsize}")
    print(f"  Current Size: {info.currsize}")

    # 3. Clear cache
    fibonacci_lru.cache_clear()
    print("\nCache cleared using `fibonacci_lru.cache_clear()`.")
    print(f"  Post-clear Cache Size: {fibonacci_lru.cache_info().currsize}")


if __name__ == "__main__":
    main()
