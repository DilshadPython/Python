"""
Optimized Prime Number Checker - Version 2 (Python 3.3 to Python 3.13 Compatible)

Algorithm: O(sqrt(N)) trial division up to floor(sqrt(N)).

Python Version Notes:
- Python 3.3 - 3.13: `math.floor()` returns an `int`.
- Python 2.7 Comparison: `math.floor()` returned a `float`. Wrapping with `int(math.floor(...))`
  is required so `range()` receives integer argument parameters across all Python versions.
"""

from __future__ import print_function
import math
import time


def is_prime_v2(num):
    """
    Returns True if num is prime, False otherwise.
    Optimized trial division checking divisors up to sqrt(N).
    Time Complexity: O(sqrt(N)).
    """
    if num <= 1:
        return False  # Numbers <= 1 are not prime

    # Explicit int cast for Python 2.7 / 3.x cross-compatibility
    max_divisor = int(math.floor(math.sqrt(num)))

    for divisor in range(2, max_divisor + 1):
        if num % divisor == 0:
            return False
    return True


def benchmark_prime_v2(upper_bound=29):
    """Executes prime checks up to upper_bound and returns results and elapsed time."""
    start_time = time.time()
    results = {}
    for num in range(1, upper_bound):
        is_p = is_prime_v2(num)
        results[num] = is_p
        print("{0} {1}".format(num, is_p))

    elapsed_time = time.time() - start_time
    print("Speed needed: {0:.6f} seconds".format(elapsed_time))
    return results, elapsed_time


if __name__ == '__main__':
    benchmark_prime_v2()