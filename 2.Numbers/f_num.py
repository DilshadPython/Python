
"""
Formatted Number Addition (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.6 - 3.13: Supports f-strings `f"{val}"` (PEP 498).
- Python 3.3 - 3.5 & Python 2.7: Uses `str.format()` or `%` formatting.
  `"{0} + {1} = {2}".format(a, b, c)` works universally across all versions.
"""

from __future__ import print_function


def add_constant_to_list(numbers, addnum):
    """
    Adds constant addnum to each number in list numbers.
    Returns a new list of transformed numbers.
    """
    return [num + addnum for num in numbers]


def run_demo():
    """Runs list modification demo with formatted string outputs."""
    numbers = [2, 3, 9, 24]
    addnum = 3

    print("--- Step-by-Step Addition ---")
    updated_numbers = []
    for num in numbers:
        new_val = num + addnum
        updated_numbers.append(new_val)
        # Using .format() for universal compatibility (Py2.7, Py3.3+)
        print("{0} + {1} = {2}".format(num, addnum, new_val))

    # Summary statement
    summary = "All items in list {0} added by {1} yield {2}".format(
        numbers, addnum, updated_numbers
    )
    print("\n" + summary)
    return updated_numbers


if __name__ == '__main__':
    run_demo()

