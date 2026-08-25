"""
Advanced Indexing, Stepping, and String Reversal (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Step slicing `str[::step]` and reversal `str[::-1]` operate
  in $O(N)$ time, allocating a new string object.
"""

from __future__ import print_function

DEFAULT_TEXT = "Test that obj is (or is not) an instance of cls (which can be a class or a tuple of classes, as supported by"


def string_slicing_and_reversing(text=DEFAULT_TEXT):
    """
    Demonstrates indexing, stepping (step=1..4), and string reversal (step=-1).
    """
    return {
        "length": len(text),
        "index_6": text[6],
        "index_22": text[22],
        "slice_to_37": text[:37],
        "full_copy": text[:],
        "except_last": text[:-1],
        "step_1": text[::1],
        "step_2": text[::2],
        "step_3": text[::3],
        "step_4": text[::4],
        "reversed": text[::-1]
    }


def run_demo():
    """Runs slicing and stepping demonstration."""
    res = string_slicing_and_reversing()
    print("Length:", res["length"])
    print("Index 6:", res["index_6"])
    print("Slice to 37:", res["slice_to_37"])
    print("Step 2:", res["step_2"])
    print("Reversed (::-1):", res["reversed"])
    return res


if __name__ == '__main__':
    run_demo()

