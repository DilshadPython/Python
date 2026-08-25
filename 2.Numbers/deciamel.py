"""
Decimal / Integer Arithmetic Operations (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: Division `/` always returns a float (PEP 238).
- Python 2.7 Comparison: Division `/` performed floor truncation on ints unless float or `from __future__ import division`.
  `input()` in Python 2.7 evaluated input as python code; `raw_input()` was required for standard string input.
"""

from __future__ import print_function, division

try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def decimal_operations(num1, num2):
    """
    Performs standard arithmetic operations on two numbers.
    Returns a dictionary of operational results.
    """
    div_val = (num1 / num2) if num2 != 0 else None
    floor_div_val = (num1 // num2) if num2 != 0 else None
    mod_val = (num1 % num2) if num2 != 0 else None

    return {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "multiplication": num1 * num2,
        "division": div_val,
        "floor_division": floor_div_val,
        "exponent": num1 ** num2,
        "modulus": mod_val
    }


def main():
    """Interactive execution for decimal operations."""
    try:
        n1 = int(get_input('Enter num1 as decimal: '))
        n2 = int(get_input('Enter num2 as decimal: '))
        
        ops = decimal_operations(n1, n2)
        print('Sum ', ops["sum"])
        print('Sub ', ops["difference"])
        print('Multiplication ', ops["multiplication"])
        print('Division ', ops["division"])
        print('Floor Division (Display only digit not float number) ', ops["floor_division"])
        print('Exponent  ', ops["exponent"])
        print('Modulus or (remainder) ', ops["modulus"])
    except ValueError:
        print("Invalid integer input.")


if __name__ == '__main__':
    main()

