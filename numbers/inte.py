"""
Integer Arithmetic Operations (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: Integers have arbitrary precision (`int` type handles any magnitude automatically).
  `sys.maxsize` exists, but there is no maximum value cap on `int`.
- Python 2.7 Comparison: Fixed-precision `int` (up to `sys.maxint`) automatically promoted to `long`
  type (with `L` suffix) on overflow. Python 3 merged `int` and `long` into a single `int` type.
"""

from __future__ import print_function, division

try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def integer_operations(num1, num2):
    """
    Performs core integer arithmetic operations.
    Returns a dictionary of results.
    """
    div_val = (num1 / num2) if num2 != 0 else None
    floor_div = (num1 // num2) if num2 != 0 else None
    mod_val = (num1 % num2) if num2 != 0 else None

    return {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "multiplication": num1 * num2,
        "division": div_val,
        "floor_division": floor_div,
        "power": num1 ** num2,
        "modulus": mod_val
    }


def main():
    """Interactive CLI execution."""
    try:
        n1 = int(get_input('Enter num1: '))
        n2 = int(get_input('Enter num2: '))
        
        ops = integer_operations(n1, n2)
        print('Sum ', ops["sum"])
        print('Sub ', ops["difference"])
        print('Multi ', ops["multiplication"])
        print('Divid ', ops["division"])
        print('Division with no reminder ', ops["floor_division"])
        print('Power ', ops["power"])
        print('Modulus reminder', ops["modulus"])
    except ValueError:
        print("Invalid integer input provided.")


if __name__ == '__main__':
    main()

