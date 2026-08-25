"""
String Concatenation & Mixed Operations (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `+` concatenates strings. Mixing `str` and `int` via `+`
  raises `TypeError`. Use comma in `print()` or `str(num)` or `str.format()`.
"""

from __future__ import print_function


def concatenate_strings(a, b, c, separator=" "):
    """Concatenates three strings with an optional separator."""
    direct = a + b + c
    with_sep = a + separator + b + separator + c
    return {
        "direct": direct,
        "with_separator": with_sep
    }


def concatenate_mixed(number, name):
    """Formats mixed integer and string data safely."""
    return "{0} {1}".format(number, name)


def run_demo():
    """Runs concatenation demonstration."""
    a, b, c = 'Hello', 'Python', 'Language'
    res = concatenate_strings(a, b, c)
    print("Direct Concatenation:", res["direct"])
    print('=========\n')
    print("With Separator:", res["with_separator"])

    y, z = 33, 81
    print("\nInteger Sum (33 + 81):", y + z)

    print('Add number with str has to use comma or format():')
    number, name = 1973, 'Dilshad'
    print(number, name)
    print("Formatted Mixed:", concatenate_mixed(number, name))
    return res


if __name__ == '__main__':
    run_demo()


