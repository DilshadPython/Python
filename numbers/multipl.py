"""
Bitwise Left Shift Multiplication Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: Bitwise left shift `x << n` multiplies integer `x` by `2^n`.
  In Python 3, integers have arbitrary precision, preventing overflow errors.
"""

from __future__ import print_function


def shift_multiply(val, shift_bits):
    """
    Multiplies val by 2^shift_bits using bitwise left shift operator (val <<= shift_bits).
    """
    return val << shift_bits


def shift_sequence(start_val, shift_per_step, steps=5):
    """
    Generates a sequence by repeatedly left-shifting current value by shift_per_step bits.
    Returns the list of values generated across steps.
    """
    results = []
    current = start_val
    for _ in range(steps):
        current <<= shift_per_step
        results.append(current)
    return results


def run_bitwise_demo():
    """
    Executes the full bitwise shift multiplication demonstration.
    """
    res1_single = shift_multiply(10, 2)
    res1_seq = shift_sequence(1, 1, steps=5)

    res2_single = shift_multiply(15, 3)
    res2_seq = shift_sequence(2, 2, steps=5)

    res3_single = shift_multiply(20, 4)
    res3_seq = shift_sequence(3, 3, steps=5)

    print("Num 10 shifted 2 bits (10 * 4): {0}".format(res1_single))
    print("Num 1 shift 1 sequence: {0}".format(res1_seq))
    print("==========================")
    print("Num 15 shifted 3 bits (15 * 8): {0}".format(res2_single))
    print("Num 2 shift 2 sequence: {0}".format(res2_seq))
    print("**************************")
    print("Num 20 shifted 4 bits (20 * 16): {0}".format(res3_single))
    print("Num 3 shift 3 sequence: {0}".format(res3_seq))

    return {
        "section1": {"single": res1_single, "sequence": res1_seq},
        "section2": {"single": res2_single, "sequence": res2_seq},
        "section3": {"single": res3_single, "sequence": res3_seq}
    }


if __name__ == '__main__':
    run_bitwise_demo()
