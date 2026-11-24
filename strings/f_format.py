"""
Float Formatting and String Precision (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `str.format()` and `format(val, spec)` format floating-point values
  with explicit decimal precision (`:.1f`, `:.2f`, `:.3f`).
- Python 3.6 - 3.13: F-strings `f"{val:.2f}"` also support format specifiers.
"""

from __future__ import print_function


def format_floats(hight=22.367453, width=778.98763):
    """Formats two floats using various precision format specifiers."""
    return {
        "raw": "{0} and {1}".format(hight, width),
        "float_default": "{:f} / {:f}".format(hight, width),
        "precision_1": "{:.1f} / {:.1f}".format(hight, width),
        "precision_2": "{:.2f} / {:.2f}".format(hight, width),
        "precision_3": "{:.3f} / {:.3f}".format(hight, width)
    }


def format_single_float(number=232.45678231, spec='.2f'):
    """Formats a single number using built-in format()."""
    return format(number, spec)


def run_demo():
    """Runs formatting demonstrations."""
    res = format_floats()
    for key, val in res.items():
        print("{0}: {1}".format(key, val))
    
    single = format_single_float()
    print("Single float format (.2f):", single)

    mult_msg = "Multiply 4 * 7: {0}".format(4 * 7)
    print(mult_msg)

    return res


if __name__ == '__main__':
    run_demo()

