"""
Prime Number Verification Module (Python 3.3 to Python 3.13 Compatible)

Algorithm: O(sqrt(N)/2) trial division checking 2 and skipping even numbers.

Python Version Notes:
- Python 3.3 - 3.13: `math.floor()` returns an `int`.
- Python 2.7 Comparison: `math.floor()` returned a `float`. `int(math.floor(...))`
  ensures integer range steps function consistently across all versions.
"""

from __future__ import print_function
import math


def is_prime_number(num):
    """
    Returns True if num is prime, False otherwise.
    Handles non-positive integers, 0, 1, and even numbers.
    Time Complexity: O(sqrt(N)/2).
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max_divisor = int(math.floor(math.sqrt(num)))

    for divisor in range(3, max_divisor + 1, 2):
        if num % divisor == 0:
            return False
    return True


def number(val):
    """Legacy helper function returning prime status for val."""
    return is_prime_number(val)


def run_prime_demo(limit=100):
    """Demonstrates prime checking for numbers from 1 up to limit."""
    primes = [i for i in range(1, limit + 1) if is_prime_number(i)]
    print("Primes up to {0}: {1}".format(limit, primes))
    return primes


if __name__ == '__main__':
    run_prime_demo(100)
