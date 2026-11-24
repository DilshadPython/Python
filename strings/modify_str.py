"""
String Modifications and Transformations (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Built-in string methods (`upper()`, `lower()`, `strip()`,
  `replace()`, `split()`) return transformed string objects without altering the original string.
"""

from __future__ import print_function


def modify_string(message=' Welcome to the Python '):
    """
    Applies upper, lower, strip, replace, and split transformations.
    """
    return {
        "original": message,
        "upper": message.upper(),
        "lower": message.lower(),
        "stripped": message.strip(),
        "replaced": message.replace('e', 'E'),
        "words": message.split()
    }


def run_demo():
    """Runs string modification demonstration."""
    res = modify_string()
    print("Original:", repr(res["original"]))
    print("Upper:", res["upper"])
    print("Lower:", res["lower"])
    print("Stripped:", repr(res["stripped"]))
    print("Replaced 'e' -> 'E':", res["replaced"])
    print("Split Words:", res["words"])
    return res


if __name__ == '__main__':
    run_demo()

