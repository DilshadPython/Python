"""
Python Operators: Assignment & Augmented Assignment Operators Module.

This module demonstrates:
- Basic Assignment: =
- Arithmetic Augmented Assignment: +=, -=, *=, /=, %=, //=, **=
- Bitwise Augmented Assignment: &=, |=, ^=, <<=, >>=
- Walrus Assignment Expression: := (Python 3.8+ PEP 572)
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Dict, List, Tuple


def demonstrate_augmented_arithmetic_assignment(initial_val: float) -> Dict[str, float]:
    """
    Demonstrate arithmetic augmented assignment operators mutating a local variable.

    Args:
        initial_val (float): Starting numeric value.

    Returns:
        Dict[str, float]: Record of mutated values after each augmented operation.
    """
    val = float(initial_val)
    history: Dict[str, float] = {"initial": val}

    val += 5
    history["add_5"] = val

    val -= 3
    history["sub_3"] = val

    val *= 4
    history["mul_4"] = val

    val /= 2
    history["div_2"] = val

    val %= 5
    history["mod_5"] = val

    val //= 2
    history["floor_div_2"] = val

    val **= 3
    history["pow_3"] = val

    return history


def demonstrate_augmented_bitwise_assignment(initial_int: int) -> Dict[str, int]:
    """
    Demonstrate bitwise augmented assignment operators mutating an integer value.

    Args:
        initial_int (int): Starting integer value.

    Returns:
        Dict[str, int]: Record of mutated values after each bitwise operation.
    """
    val = initial_int
    history: Dict[str, int] = {"initial": val}

    val &= 0b1111  # Bitwise AND
    history["and_mask"] = val

    val |= 0b0100  # Bitwise OR
    history["or_mask"] = val

    val ^= 0b0010  # Bitwise XOR
    history["xor_mask"] = val

    val <<= 2      # Bitwise Left Shift
    history["shift_left_2"] = val

    val >>= 1      # Bitwise Right Shift
    history["shift_right_1"] = val

    return history


def demonstrate_walrus_assignment_expression(words: List[str]) -> Tuple[List[str], int]:
    """
    Demonstrate the Walrus Operator (:=) for inline assignment within list comprehension.

    Args:
        words (List[str]): List of string elements.

    Returns:
        Tuple[List[str], int]: Processed uppercase words exceeding length 4 and total count.
    """
    # Walrus operator := assigns length 'n' inline and filters in a single pass
    long_words = [upper for word in words if (n := len(word)) > 4 for upper in [word.upper()]]
    return long_words, len(long_words)
