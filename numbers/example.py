"""
Base Conversion Example (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `int(val_str, base)` parses string representation in any base (2 to 36).
"""

from __future__ import print_function


def parse_base_string(val_str, base):
    """Parses a string representing a number in a given base (2-36) into a decimal integer."""
    return int(val_str, base)


def demo_base_conversions():
    """Demonstrates base 3, base 2, and base 4 parsing for '10000'."""
    results = {
        "base_3": parse_base_string('10000', 3),  # 3^4 = 81
        "base_2": parse_base_string('10000', 2),  # 2^4 = 16
        "base_4": parse_base_string('10000', 4)   # 4^4 = 256
    }
    
    print("Base 3 ('10000'):", results["base_3"])
    print("Base 2 ('10000'):", results["base_2"])
    print("Base 4 ('10000'):", results["base_4"])
    
    return results


if __name__ == '__main__':
    demo_base_conversions()