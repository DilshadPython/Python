"""
Random Number Generation (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.9 - 3.13: `random.sample()` accepts `range()` objects directly without sequence conversion.
- Python 3.3 - 3.8: `random.sample(range(a, b), k)` accepted range objects.
- Python 2.7 Comparison: `range()` returned a list, so `random.sample(range(...), k)` sampled from the list.
"""

from __future__ import print_function
import random


def get_random_single(start=1, stop=12):
    """Returns a single random integer in range [start, stop)."""
    return random.randrange(start, stop)


def get_random_sample(start=1, stop=12, count=4):
    """
    Returns a list of `count` unique random integers sampled from range [start, stop).
    Uses list(range(...)) for universal cross-version safety.
    """
    sample_range = list(range(start, stop))
    return random.sample(sample_range, count)


def run_demo():
    """Runs single random number display and multi-sample demonstration."""
    single_val = get_random_single(1, 12)
    print("Single Random (1 to 11):", single_val)

    print('\n=======')
    samples = get_random_sample(1, 12, 4)
    print("Random Sample of 4 values (1 to 11):")
    for val in samples:
        print(val)

    return single_val, samples


if __name__ == '__main__':
    run_demo()


