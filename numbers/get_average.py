"""
Arithmetic Mean / Average Calculation (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: True division `/` returns float automatically (e.g. 5 / 2 == 2.5).
- Python 2.7 Comparison: `from __future__ import division` ensures float division on integers.
"""

from __future__ import print_function
from __future__ import division

DEFAULT_NUMBERS = [11, 19, 29, 74, 15, 34, 97, 57, 1, 63, 9, 13]


def calculate_average(numbers):
    """
    Calculates arithmetic mean of a sequence of numbers.
    Raises ValueError if sequence is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    return float(sum(numbers)) / len(numbers)


def run_average_demo(numbers=None):
    """
    Executes average calculation demonstration on provided or default list.
    """
    if numbers is None:
        numbers = DEFAULT_NUMBERS
    avg = calculate_average(numbers)
    print("The average is:  {0}".format(avg))
    return avg


if __name__ == '__main__':
    run_average_demo()