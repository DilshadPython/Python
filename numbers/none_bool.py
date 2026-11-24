"""
None Type & Boolean Truthiness Evaluation (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: `None`, `True`, `False` are built-in singleton constants and keywords.
- Truthiness Rules: 0, 0.0, empty collections ([], {}, ''), and None evaluate to False.
  All non-zero numbers, non-empty collections, and non-empty strings evaluate to True.
"""

from __future__ import print_function


def evaluate_truthiness(value):
    """Evaluates and returns the boolean truthiness of any object."""
    return bool(value)


def run_demo():
    """Evaluates and displays truthiness across different data types."""
    x = None
    y = 2
    print("x =", x)
    print("y =", y)

    test_cases = [
        ("a", 0),
        ("b", 1),
        ("c", 12),
        ("d", -1),
        ("e", 0.0),
        ("f", -3.4),
        ("g", 0.201),
        ("h", -0.201),
        ("i", []),
        ("j", [3, -1, 8]),
        ("k", ''),
        ("l", 'Hello'),
        ("m", 'False'),
        ("n", 'True'),
        ("o", {})
    ]

    results = {}
    for var_name, val in test_cases:
        res = evaluate_truthiness(val)
        results[var_name] = res
        print("{0} is {1}".format(var_name, res))

    return results


if __name__ == '__main__':
    run_demo()