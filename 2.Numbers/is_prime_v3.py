"""
Highly Optimized Prime Number Checker - Version 3 (Python 3.3 to Python 3.13 Compatible)

Algorithm: O(sqrt(N)/2) trial division skipping even numbers after checking 2.

Python Version Notes:
- Python 3.3 - 3.13: `math.floor()` returns an `int`.
- Python 2.7 Comparison: `math.floor()` returned a `float`. Wrapping with `int(math.floor(...))`
  ensures integer step ranges work correctly across all Python versions.
"""

from __future__ import print_function
import math
import time


def is_prime_v3(num):
    """
    Returns True if num is prime, False otherwise.
    Fast trial division checking 2 and then odd numbers up to sqrt(N).
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


def benchmark_prime_v3(upper_bound=29):
    """Executes prime checks up to upper_bound and returns results and elapsed time."""
    start_time = time.time()
    results = {}
    for num in range(1, upper_bound):
        is_p = is_prime_v3(num)
        results[num] = is_p
        print("{0} {1}".format(num, is_p))

    elapsed_time = time.time() - start_time
    print("Speed needed: {0:.6f} seconds".format(elapsed_time))
    return results, elapsed_time


if __name__ == '__main__':
    benchmark_prime_v3()