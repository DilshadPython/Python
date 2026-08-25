"""
String endswith Method Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `str.endswith(suffix[, start[, end]])` checks if string ends with suffix.
  Suffix can be a single string or a tuple of strings across all Python versions.
"""

from __future__ import print_function


def check_endswith(txt, suffix, start=None, end=None):
    """
    Checks if txt ends with suffix (str or tuple of strings).
    Supports optional start and end indexing.
    """
    if start is not None and end is not None:
        return txt.endswith(suffix, start, end)
    elif start is not None:
        return txt.endswith(suffix, start)
    return txt.endswith(suffix)


def run_demo():
    """Runs endswith checks."""
    txt = 'Welcome to the Europe to watch the fantastic football.'
    
    r1 = check_endswith(txt, 'll.')
    print("Ends with 'll.':", r1)

    r2 = check_endswith(txt, 'fantastic football.', 6, 15)
    print("Ends with 'fantastic football.' (6..15):", r2)

    r3 = check_endswith(txt, 'football.', 45, 55)
    print("Ends with 'football.' (45..55):", r3)

    msg = 'Welcome to the Europe to watch the fantastic Basketball.'
    r4 = check_endswith(msg, ('football.', 'Basketball.'))
    print("Ends with tuple ('football.', 'Basketball.'):", r4)

    return {
        "ends_ll": r1,
        "ends_slice_1": r2,
        "ends_slice_2": r3,
        "ends_tuple": r4
    }


if __name__ == '__main__':
    run_demo()


