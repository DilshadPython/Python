"""
String Input & Type Inspection (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: `input()` returns type `str` (Unicode string).
- Python 2.7 Comparison: `raw_input()` returned `str` (byte string), while `input()` evaluated code.
"""

from __future__ import print_function

try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def get_name_details(name_val):
    """Returns a dictionary containing string value and its type."""
    return {
        "name": name_val,
        "type": type(name_val),
        "type_name": type(name_val).__name__
    }


def main():
    """Interactive execution for string input inspection."""
    default_name = '<NAME>'
    print("Default Name:", default_name)
    print('####################################')

    try:
        user_name = get_input('What is your name? ')
        details = get_name_details(user_name)
        print("Name: {}".format(details["name"]))
        print("Type: {}".format(details["type"]))
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")


if __name__ == '__main__':
    main()