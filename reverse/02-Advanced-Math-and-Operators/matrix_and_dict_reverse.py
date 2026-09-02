# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - from typing import Any, Dict, List, Tuple: PEP 484 type annotations.
# =========================================================================
from typing import Any, Dict, List, Tuple


def demonstrate_dictionary_reversing(
    sample_dict: Dict[str, int] = None
) -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> matrix_and_dict_reverse.py]
    Demonstrates reversing dictionaries and dict views (dict_keys, dict_values, dict_items).
    
    Since Python 3.7+, dictionaries preserve insertion order.
    In Python 3.8+, built-in reversed() was enabled directly on dict objects and views.

    Args:
        sample_dict (Dict[str, int], optional): Dictionary to reverse. Defaults to {"a": 1, "b": 2, "c": 3}.

    Returns:
        Dict[str, Any]: Reversed dictionary keys, values, items, and reconstructed dict.
    """
    if sample_dict is None:
        sample_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

    # 1. Reverse keys directly or via reversed(dict)
    reversed_keys = list(reversed(sample_dict))
    
    # 2. Reverse dict values view
    reversed_values = list(reversed(sample_dict.values()))

    # 3. Reverse dict items view (key-value tuples)
    reversed_items = list(reversed(sample_dict.items()))

    # 4. Construct a new dictionary with reversed insertion order
    reversed_ordered_dict = dict(reversed_items)

    return {
        "original_dict": sample_dict,
        "reversed_keys": reversed_keys,
        "reversed_values": reversed_values,
        "reversed_items": reversed_items,
        "reversed_ordered_dict": reversed_ordered_dict,
    }


def demonstrate_matrix_reversing(
    matrix: List[List[int]] = None
) -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Operators -> matrix_and_dict_reverse.py]
    Demonstrates 2D matrix manipulation: row reversal, column reversal, and 180-degree rotation.

    Args:
        matrix (List[List[int]], optional): 2D grid matrix. Defaults to [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

    Returns:
        Dict[str, Any]: Transformations of the 2D grid.
    """
    if matrix is None:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    # 1. Row Reversal (flip vertically)
    row_reversed = matrix[::-1]

    # 2. Column Reversal (flip horizontally)
    col_reversed = [row[::-1] for row in matrix]

    # 3. Full 180-Degree Rotation (flip vertically and horizontally)
    rotated_180 = [row[::-1] for row in matrix[::-1]]

    return {
        "original_matrix": matrix,
        "row_reversed_matrix": row_reversed,
        "col_reversed_matrix": col_reversed,
        "rotated_180_matrix": rotated_180,
    }


if __name__ == "__main__":
    print(demonstrate_dictionary_reversing())
    print(demonstrate_matrix_reversing())
