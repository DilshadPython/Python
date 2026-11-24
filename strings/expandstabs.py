"""
String expandtabs Method Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `str.expandtabs(tabsize=8)` replaces tab characters `\t` with spaces.
"""

from __future__ import print_function


def expand_tabs(msg='H\te\tl\tl\to \tPytho\tn', tabsize=8):
    """Replaces tab characters with spaces using tabsize step size."""
    return msg.expandtabs(tabsize)


def main():
    """Demonstrates tab expansion."""
    msg = 'H\te\tl\tl\to \tPytho\tn'
    expanded = expand_tabs(msg, 8)
    print("Original:", repr(msg))
    print("Expanded (tabsize=8):", repr(expanded))
    return expanded


if __name__ == '__main__':
    main()