"""
Floating Point Operations & Constants (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: IEEE 754 double-precision floats.
- Special float literals: float('nan'), float('inf'), float('-inf'), scientific notation (3e8).
- Math module functions `math.isnan()` and `math.isinf()` check special float conditions.
"""

from __future__ import print_function, division
import math

try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def float_operations(num1, num2):
    """
    Executes standard floating point arithmetic operations.
    Returns a dictionary of float operation results.
    """
    div_val = (num1 / num2) if num2 != 0.0 else float('inf')
    floor_div = (num1 // num2) if num2 != 0.0 else float('inf')
    mod_val = (num1 % num2) if num2 != 0.0 else float('nan')

    return {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "multiplication": num1 * num2,
        "division": div_val,
        "floor_division": floor_div,
        "power": num1 ** num2,
        "modulus": mod_val
    }


def inspect_special_floats():
    """Generates and returns special floating point representation values."""
    return {
        "scientific_3e8": 3e8,
        "float_9": float(9),
        "from_str_2548": float('2548'),
        "nan": float('nan'),
        "inf": float('inf'),
        "neg_inf": float('-inf'),
        "scientific_5e3": 5e3,
        "scientific_12e9": 12e9,
        "scientific_348e4": 348e4
    }


def main():
    """Interactive execution and demonstration of float features."""
    try:
        n1_str = get_input('Enter num1: ')
        n2_str = get_input('Enter num2: ')
        n1 = float(n1_str)
        n2 = float(n2_str)
        
        ops = float_operations(n1, n2)
        print('Sum: ', ops["sum"])
        print('Sub: ', ops["difference"])
        print('Multi: ', ops["multiplication"])
        print('Division: ', ops["division"])
        print('Division with no reminder only digit number: ', ops["floor_division"])
        print('Power: ', ops["power"])
        print('Modulus reminder: ', ops["modulus"])
    except (ValueError, TypeError):
        print("Using default values (10.5, 2.5) for interactive float ops:")
        ops = float_operations(10.5, 2.5)
        print('Sum: ', ops["sum"])

    print('\n===========================')
    specials = inspect_special_floats()
    for key, val in specials.items():
        print("{0}: {1} (type: {2})".format(key, val, type(val).__name__))


if __name__ == '__main__':
    main()



