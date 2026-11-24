"""
String Length and Membership Testing (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `len(str)` returns character count.
  `in` and `not in` operators test substring membership.
"""

from __future__ import print_function


def check_string_length_and_membership(text, search_in, search_not_in):
    """
    Returns string length and substring membership results.
    """
    return {
        "length": len(text),
        "is_present": search_in in text,
        "is_absent": search_not_in not in text
    }


def run_demo():
    """Runs length and membership demonstration."""
    sample = 'Adam as string'
    print("Length of sample:", len(sample))

    text = 'The gap between writing basic Python code and developing professional-grade systems is far wider than most devs realize.'
    res = check_string_length_and_membership(text, 'professional-grade ', 'Java')

    print("Text length:", res["length"])
    print("'professional-grade ' in text:", res["is_present"])
    print("'Java' not in text:", res["is_absent"])

    return res


if __name__ == '__main__':
    run_demo()