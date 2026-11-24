"""
Fibonacci Algorithms: Lazy Evaluation Generator (`yield`)

This module demonstrates lazy evaluation of Fibonacci numbers using Python generator
functions (`yield`).

Key Concepts:
- Generators evaluate terms on demand, consuming minimal $O(1)$ memory even when
  generating millions of numbers.
- `next(gen)` yields successive numbers sequentially.
"""
from typing import Generator, List


def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """
    Generator yielding `limit` Fibonacci numbers sequentially.

    Args:
        limit (int): Number of Fibonacci terms to yield.

    Yields:
        int: Successive Fibonacci sequence numbers.

    Raises:
        ValueError: If limit is negative.
    """
    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    count = 0
    a, b = 0, 1
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def main() -> None:
    """Demonstrates generator-based lazy Fibonacci evaluation."""
    print("=" * 60)
    print("5. Lazy Evaluation Generator (`yield`) ($O(1)$ Memory Overhead)")
    print("=" * 60)

    # 1. Iterate over generator using for loop
    limit = 10
    print(f"\n1. First {limit} terms from generator:")
    for index, val in enumerate(fibonacci_generator(limit)):
        print(f"   Term {index:2d}: {val}")

    # 2. Step through generator using next()
    print("\n2. Manual step-by-step evaluation using `next()`:")
    gen = fibonacci_generator(5)
    print(f"   First step:  {next(gen)}")
    print(f"   Second step: {next(gen)}")
    print(f"   Third step:  {next(gen)}")


if __name__ == "__main__":
    main()
