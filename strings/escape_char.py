r"""
String Escape Characters Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Escape sequences (\', \", \\, \r, \b, \f, \ooo octal, \xHH hex)
  work consistently across all Python versions.
"""

from __future__ import print_function


def get_escaped_strings():
    """Returns a dictionary of sample strings containing escape sequences."""
    return {
        "double_quotes": 'Today is "Friday" cold, yesterday "Thursday" nice.',
        "single_quotes_escaped": 'Today is \'Friday\' cold, yesterday \'Thursday\' nice.',
        "single_quote_apostrophe": 'Today it\'s Friday which is very nice weather.',
        "backslash_escaped": 'Today it\'s Friday which is very nice \\(weather).',
        "carriage_return": 'Welcome to\rPython',
        "backspace": 'Welcome \bPython!',
        "form_feed": 'Welcome\fto\fPython!',
        "octal_hello": '\110\145\154\154\157 Java!',
        "hex_hello": "\x48\x65\x6c\x6c\x6f JavaScript"
    }


def run_demo():
    """Prints all escape character samples."""
    samples = get_escaped_strings()
    for key, val in samples.items():
        print("--- {0} ---".format(key))
        print(val)
    return samples


if __name__ == '__main__':
    run_demo()