"""
Basic Prime Number Checker - Version 1 (Python 3.3 to Python 3.13 Compatible)

Algorithm: Simple O(N) trial division from 2 to N-1.

Python Version Notes:
- Python 3.3 - 3.13: `range()` is an iterator/range generator object.
- Python 2.7 Comparison: `range()` constructed a full list in memory; `xrange()` was used for lazy evaluation.
"""

from __future__ import print_function
import time


def is_prime_v(num):
    """
    Returns True if num is prime, False otherwise.
    Basic trial division checking all divisors from 2 to num - 1.
    Time Complexity: O(N).
    """
    if num <= 1:
        return False  # Numbers <= 1 are not prime

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def benchmark_prime_v(upper_bound=29):
    """Executes prime checks up to upper_bound and returns results and elapsed time."""
    start_time = time.time()
    results = {}
    for num in range(1, upper_bound):
        is_p = is_prime_v(num)
        results[num] = is_p
        print("{0} {1}".format(num, is_p))

    elapsed_time = time.time() - start_time
    print("Speed needed: {0:.6f} seconds".format(elapsed_time))
    return results, elapsed_time


if __name__ == '__main__':
    benchmark_prime_v()