"""
String Slicing & Substring Extraction (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Slicing `str[start:stop:step]` supports positive and negative indices.
  Out-of-bound indices do not raise `IndexError`; they truncate cleanly.
"""

from __future__ import print_function

DEFAULT_TEXT = 'The gap between writing basic Python code and developing professional-grade systems is far wider than most devs realize.'


def slice_string(text=DEFAULT_TEXT):
    """
    Demonstrates positive, negative, and range string slicing.
    """
    return {
        "first_25": text[:25],
        "last_20": text[-20:],
        "except_last_15": text[:-15],
        "range_11_minus45": text[11:-45],
        "range_minus45_minus11": text[-45:-11]
    }


def run_demo():
    """Runs string slicing demonstration."""
    res = slice_string()
    print("First 25 chars:", res["first_25"])
    print("Last 20 chars:", res["last_20"])
    print("Except last 15 chars:", res["except_last_15"])
    print("Slice [11:-45]:", res["range_11_minus45"])
    print("Slice [-45:-11]:", res["range_minus45_minus11"])
    return res


if __name__ == '__main__':
    run_demo()