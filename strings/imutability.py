"""
String Immutability and Core Operations (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Strings are immutable objects in Python. Direct item assignment
  `msg[i] = 'X'` raises `TypeError`. New string objects are created via concatenation or methods.
"""

from __future__ import print_function


def demonstrate_immutability(msg='Hello world'):
    """
    Demonstrates string immutability and common string operations.
    Returns results of length, upper, lower, split, count, find, and replace.
    """
    concat = msg + ' Hello London'
    upper_val = concat.upper()
    lower_val = upper_val.lower()
    split_val = msg.split('l')
    count_o = concat.count('o')
    find_world = msg.find('world')
    replace_val = msg.replace('world', 'Python')

    return {
        "length": len(msg),
        "concat": concat,
        "upper": upper_val,
        "lower": lower_val,
        "split": split_val,
        "count_o": count_o,
        "find_world": find_world,
        "replace": replace_val
    }


def verify_immutability_error(msg='Hello world'):
    """Verifies that attempting index assignment raises TypeError."""
    try:
        msg[0] = 'X'
        return False
    except TypeError:
        return True


def run_demo():
    """Runs immutability demonstration."""
    msg = 'Hello world'
    print("Is string immutable (raised TypeError on item assignment)?", verify_immutability_error(msg))
    res = demonstrate_immutability(msg)
    for key, val in res.items():
        print("{0}: {1}".format(key, val))
    return res


if __name__ == '__main__':
    run_demo()