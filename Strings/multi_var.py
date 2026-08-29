"""
Multiple Variable Assignment and Unpacking (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Unpacking sequences (lists, tuples) into variables requires
  matching length. Chained assignment `a = b = c = val` assigns same reference.
"""

from __future__ import print_function


def unpack_multiple_variables():
    """Demonstrates multiple variable assignments, chaining, and sequence unpacking."""
    a, b, c, d = 7, 4, 19, 0
    one, two, three = 'Linux', 'Apple', 'Windows'
    
    # Chained assignment
    x1 = x2 = x3 = 'Hello world'
    
    # List unpacking
    text_list = ['Linux', 'Apple', 'Windows']
    m, n, o = text_list

    # Tuple unpacking
    os_tuple = ('Linux', 'Apple', 'Windows')
    x, y, z = os_tuple

    return {
        "ints": (a, b, c, d),
        "os_strings": (one, two, three),
        "chained": (x1, x2, x3),
        "unpacked_list": (m, n, o),
        "unpacked_tuple": (x, y, z)
    }


def run_demo():
    """Runs multiple variable unpacking demonstration."""
    res = unpack_multiple_variables()
    for key, val in res.items():
        print("{0}: {1}".format(key, val))
    return res


if __name__ == '__main__':
    run_demo()