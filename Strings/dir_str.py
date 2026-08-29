"""
String Attribute Directory Inspection (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `dir(obj)` lists available attributes and methods on string instances.
"""

from __future__ import print_function


def get_str_attributes(val='Adam as string'):
    """Returns directory list of attributes on given string object."""
    return dir(val)


def main():
    """Demonstrates string attribute inspection."""
    name = 'Adam as string'
    print("name: {}".format(name))
    attrs = get_str_attributes(name)
    print("Total Attributes & Methods: {}".format(len(attrs)))
    return attrs


if __name__ == '__main__':
    main()