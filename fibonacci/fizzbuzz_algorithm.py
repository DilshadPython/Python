"""
Algorithms: Modular FizzBuzz Implementation

This module provides a clean, Pythonic implementation of the classic FizzBuzz
algorithm.

Rules:
- For multiples of 3, return "Fizz".
- For multiples of 5, return "Buzz".
- For multiples of both 3 and 5, return "FizzBuzz".
- For all other numbers, return string representation of the number.
"""
from typing import List, Union


def fizzbuzz_item(number: int) -> str:
    """
    Evaluates a single number against FizzBuzz criteria.

    Args:
        number (int): The number to evaluate.

    Returns:
        str: "FizzBuzz", "Fizz", "Buzz", or str(number).
    """
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def generate_fizzbuzz_sequence(limit: int) -> List[str]:
    """
    Generates a list of FizzBuzz strings for numbers from 1 to `limit`.

    Args:
        limit (int): The upper range bound (inclusive).

    Returns:
        List[str]: List of evaluated FizzBuzz strings.

    Raises:
        ValueError: If limit is less than 1.
    """
    if limit < 1:
        raise ValueError("Limit must be at least 1.")

    return [fizzbuzz_item(n) for n in range(1, limit + 1)]


def main() -> None:
    """Demonstrates FizzBuzz sequence generation."""
    print("=" * 60)
    print("7. Modular FizzBuzz Algorithm Demonstration")
    print("=" * 60)

    limit = 30
    results = generate_fizzbuzz_sequence(limit)

    print(f"\nFizzBuzz outputs for range 1 to {limit}:")
    for i, res in enumerate(results, start=1):
        print(f"  {i:2d}: {res}")


if __name__ == "__main__":
    main()
