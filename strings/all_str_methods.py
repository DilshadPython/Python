"""
Comprehensive String Methods Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13: `str.casefold()` (PEP 3131 / Unicode case folding) introduced in Py3.3.
  `str.encode()` returns a `bytes` object (e.g. b'...').
- Python 2.7 Comparison: `str` was a byte string, `unicode` was a separate type. `casefold()` did not exist.
"""

from __future__ import print_function


def get_string_methods():
    """Returns a list of all method attributes on str."""
    return dir(str)


def demonstrate_casing(name='python', lang='JavaScript'):
    """Demonstrates capitalize() and casefold() string methods."""
    return {
        "capitalize": name.capitalize(),
        "casefold": lang.casefold() if hasattr(lang, 'casefold') else lang.lower()
    }


def center_text(txt='Welcome', width=30):
    """Centers string inside specified width."""
    return txt.center(width)


def count_substring(msg="I like oranges, but I don't likes bananas.", val='like', start=None, end=None):
    """Counts occurrences of a substring within optional bounds."""
    if start is not None and end is not None:
        return msg.count(val, start, end)
    return msg.count(val)


def encode_string(msg="I would love to visit Köln in Germany.", encoding="ascii", errors="replace"):
    """Encodes string with specified encoding and error handling mode."""
    return msg.encode(encoding=encoding, errors=errors)


def run_demo():
    """Runs comprehensive string methods demonstration."""
    print("Total String Methods:", len(get_string_methods()))
    casing = demonstrate_casing()
    print("Capitalize:", casing["capitalize"])
    print("Casefold:", casing["casefold"])

    centered = center_text()
    print("Centered String:", repr(centered))

    cnt = count_substring()
    print("Count 'like':", cnt)

    msg = "I would love to visit Köln in Germany."
    print("Default UTF-8 Encode:", msg.encode())
    
    error_modes = ["backslashreplace", "ignore", "namereplace", "replace", "xmlcharrefreplace"]
    for mode in error_modes:
        encoded = encode_string(msg, "ascii", mode)
        print("ASCII Encode ({0}): {1}".format(mode, encoded))


if __name__ == '__main__':
    run_demo()