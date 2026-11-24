# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - from typing import Any, Dict, List, Tuple, Union: PEP 484 type hint definitions.
# =========================================================================
from typing import Any, Dict, List, Tuple, Union


def demonstrate_slicing_reversal(
    sample_list: List[int] = None,
    sample_str: str = "Developer"
) -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> reverse_slicing_conversions.py]
    Demonstrates extended sequence slicing [::-1] for list and string reversal.
    
    Slicing with a negative step value (-1) traverses items from right to left,
    creating a shallow copy of the sequence in reverse order.

    Args:
        sample_list (List[int], optional): Input list. Defaults to [100, 200, 300, 400].
        sample_str (str, optional): Input string. Defaults to "Developer".

    Returns:
        Dict[str, Any]: Slicing results for full reversal and stepped reversal.
    """
    if sample_list is None:
        sample_list = [100, 200, 300, 400]

    # Full sequence reversal via slice copy
    sliced_list_rev = sample_list[::-1]
    sliced_str_rev = sample_str[::-1]

    # Stepped reverse slice (every second item backwards)
    stepped_list_rev = sample_list[::-2]

    # Sub-range reverse slice [stop:start:-step]
    subrange_str_rev = sample_str[6:1:-1]

    return {
        "full_sliced_list": sliced_list_rev,
        "full_sliced_str": sliced_str_rev,
        "stepped_sliced_list": stepped_list_rev,
        "subrange_sliced_str": subrange_str_rev,
    }


def demonstrate_reversal_type_errors() -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> reverse_slicing_conversions.py]
    Demonstrates handling of TypeError when passing un-reversible types to reversed().
    
    Unordered collections (sets, dict_keys in older versions) or non-sequences (ints)
    do not support reversed() because they lack sequence indices or __reversed__ hooks.

    Returns:
        Dict[str, Any]: Results capturing expected TypeErrors.
    """
    set_error_caught = False
    int_error_caught = False

    # Attempting reversed() on set
    try:
        reversed({1, 2, 3})  # Sets are unordered and lack __reversed__ / __getitem__
    except TypeError:
        set_error_caught = True

    # Attempting reversed() on integer
    try:
        reversed(12345)  # Integers are non-iterable
    except TypeError:
        int_error_caught = True

    return {
        "set_type_error_caught": set_error_caught,
        "int_type_error_caught": int_error_caught,
    }


if __name__ == "__main__":
    print(demonstrate_slicing_reversal())
    print(demonstrate_reversal_type_errors())
