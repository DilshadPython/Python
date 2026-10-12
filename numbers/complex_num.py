"""
Complex Numbers Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Complex literals use `j` or `J` for imaginary part (e.g. 4+8+3j).
- Attributes: `.real` and `.imag` yield float components across all Python versions.
"""

from __future__ import print_function


def get_complex_details(val):
    """Returns a dictionary containing properties of a complex number."""
    return {
        "value": val,
        "type": type(val),
        "real": val.real,
        "imag": val.imag
    }


def demo_complex():
    """Demonstrates creation and inspection of complex numbers."""
    samples = [
        4 + 8 + 3j,
        9j,
        -8j
    ]
    results = []
    for item in samples:
        details = get_complex_details(item)
        results.append(details)
        print("Value: {0} | Type: {1} | Real: {2} | Imag: {3}".format(
            details["value"], details["type"].__name__, details["real"], details["imag"]
        ))
    return results


if __name__ == '__main__':
    demo_complex()