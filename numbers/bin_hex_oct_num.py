"""
Number Base Conversions & Complex Numbers (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: `bin()`, `hex()`, `oct()` return prefixes '0b', '0x', '0o'.
- Python 2.7 Comparison: `oct(8)` returned '010' (legacy octal syntax without 'o').
  `print` was a statement requiring `from __future__ import print_function`.
"""

from __future__ import print_function


def convert_number_bases(x):
    """
    Returns binary, hexadecimal, and octal string representations of an integer.
    Compatible across Python 2.7 and Python 3.3 - 3.13.
    """
    return {
        "number": x,
        "binary": bin(x),
        "hexadecimal": hex(x),
        "octal": oct(x)
    }


def to_complex(y):
    """Converts a number to a complex number representation."""
    return complex(y)


def run_demo(limit_bases=100, limit_complex=20):
    """Runs the base conversion and complex conversion loops."""
    print("=== Binary, Hexadecimal, and Octal Conversions (0 to {}) ===".format(limit_bases - 1))
    for x in range(limit_bases):
        info = convert_number_bases(x)
        print("Binary of {0} = {1} | Hexadecimal of {0} = {2} | Octal of {0} = {3}".format(
            info["number"], info["binary"], info["hexadecimal"], info["octal"]
        ))

    print("\n=== Number to Complex Conversions (0 to {}) ===".format(limit_complex - 1))
    for y in range(limit_complex):
        print("Number {0} changed to complex is {1}".format(y, to_complex(y)))


if __name__ == '__main__':
    run_demo(limit_bases=10, limit_complex=5)