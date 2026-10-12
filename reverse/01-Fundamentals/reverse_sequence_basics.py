# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - from typing import Any, Dict, List, Sequence, Tuple, Union: Type hints for PEP 484 compliance.
# =========================================================================
from typing import Any, Dict, List, Sequence, Tuple, Union


def demonstrate_reversed_builtin(
    sample_list: List[int] = None,
    sample_tuple: Tuple[str, ...] = None,
    sample_str: str = "Python"
) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> reverse_sequence_basics.py]
    Demonstrates the built-in reversed() function on lists, tuples, and strings.
    
    The reversed() function returns a lazy iterator that traverses the sequence in reverse
    without modifying the original sequence.
    
    Args:
        sample_list (List[int], optional): Integer list to reverse. Defaults to [10, 20, 30, 40].
        sample_tuple (Tuple[str, ...], optional): String tuple to reverse. Defaults to ("alpha", "beta", "gamma").
        sample_str (str, optional): String to reverse. Defaults to "Python".

    Returns:
        Dict[str, Any]: Dictionary containing original and reversed sequences.
    """
    if sample_list is None:
        sample_list = [10, 20, 30, 40]
    if sample_tuple is None:
        sample_tuple = ("alpha", "beta", "gamma")

    # 1. Reverse list using reversed() iterator -> materialize as list
    list_rev_iter = reversed(sample_list)
    reversed_list = list(list_rev_iter)

    # 2. Reverse tuple using reversed() iterator -> materialize as tuple
    tuple_rev_iter = reversed(sample_tuple)
    reversed_tuple = tuple(tuple_rev_iter)

    # 3. Reverse string using reversed() iterator -> join into new string
    str_rev_iter = reversed(sample_str)
    reversed_str = "".join(str_rev_iter)

    return {
        "original_list": sample_list,
        "reversed_list": reversed_list,
        "original_tuple": sample_tuple,
        "reversed_tuple": reversed_tuple,
        "original_str": sample_str,
        "reversed_str": reversed_str,
    }


def demonstrate_inplace_reverse(sample_list: List[int] = None) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> reverse_sequence_basics.py]
    Demonstrates the in-place list.reverse() method.
    
    Unlike reversed(), list.reverse() modifies the list in place and returns None.
    
    Args:
        sample_list (List[int], optional): Integer list to mutate. Defaults to [1, 2, 3, 4, 5].

    Returns:
        Dict[str, Any]: Dictionary containing the mutated list and method return value.
    """
    if sample_list is None:
        sample_list = [1, 2, 3, 4, 5]

    # Create a copy so we don't mutate external reference unexpectedly
    working_list = list(sample_list)

    # Execute in-place reverse
    return_value = working_list.reverse()

    return {
        "original_before_mutation": sample_list,
        "mutated_list": working_list,
        "method_return_value": return_value,  # Always None in Python
    }


if __name__ == "__main__":
    print(demonstrate_reversed_builtin())
    print(demonstrate_inplace_reverse())
