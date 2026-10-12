"""
Integer Input Conversion (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: `input()` returns a string. `int(input())` converts to int.
- Python 2.7 Comparison: `input()` evaluated expressions automatically; `raw_input()` was required for string input.
"""

from __future__ import print_function

try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def read_and_parse_int(val_str):
    """Parses a string input into an integer."""
    return int(val_str)


def main():
    """Interactive execution for integer parsing."""
    try:
        user_val = get_input('Enter a number: ')
        number = read_and_parse_int(user_val)
        print("Parsed Number: {}".format(number))
    except ValueError:
        print("Invalid integer input.")


if __name__ == '__main__':
    main()