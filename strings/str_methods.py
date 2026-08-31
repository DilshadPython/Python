"""
Common String Methods Inspection (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `title()`, `isupper()`, `split()`, `replace()`, `find()` operate
  identically on standard ASCII strings.
"""

from __future__ import print_function


def inspect_string_methods(msg='How many years you have Python experiences?'):
    """
    Applies and returns common string method evaluations.
    """
    return {
        "length": len(msg),
        "upper": msg.upper(),
        "lower": msg.lower(),
        "isupper": msg.isupper(),
        "split_comma": msg.split(','),
        "replace_js": msg.replace('Python', 'JavaScript'),
        "find_python": msg.find('Python'),
        "in_case_sensitive": 'Python' in msg,
        "in_case_insensitive": 'python' in msg,
        "title": msg.title()
    }


def run_demo():
    """Runs string methods inspection."""
    res = inspect_string_methods()
    for key, val in res.items():
        print("{0}: {1}".format(key, val))
    return res


if __name__ == '__main__':
    run_demo()