"""
Built-in String Documentation Inspection (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `help(str)` displays docstrings for the string class and its methods.
"""

from __future__ import print_function


def get_str_help_doc(method_name=None):
    """Returns docstring for str class or a specific method on str."""
    if method_name and hasattr(str, method_name):
        return getattr(str, method_name).__doc__
    return str.__doc__


def main():
    """Demonstrates string docstring inspection."""
    str_doc = get_str_help_doc()
    islower_doc = get_str_help_doc('islower')
    print("str docstring length:", len(str_doc) if str_doc else 0)
    print("str.islower docstring:", islower_doc)
    return str_doc


if __name__ == '__main__':
    main()

