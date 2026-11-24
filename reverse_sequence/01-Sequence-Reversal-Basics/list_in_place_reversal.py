"""
List In-Place Reversal & Out-of-Place Iteration Module.

This module demonstrates mutable list reversal techniques in Python:
- In-place list reversal using list.reverse() (mutates original list, returns None)
- Out-of-place list reversal using extended slicing list[::-1] (returns a new list copy)
- Lazy reverse iteration using reversed(list) (returns a reverse iterator)
"""
# "from typing import List, Tuple, Dict, Any" imports typing annotations.
from typing import List, Tuple, Dict, Any


def reverse_list_in_place(items: List[Any]) -> None:
    """
    Reverse a list in-place using list.reverse().

    This operation mutates the input list directly in O(N) time and O(1) auxiliary RAM.
    It returns None following Python's Command-Query Separation principle.

    Args:
        items (List[Any]): List to mutate in-place.
    """
    items.reverse()


def reverse_list_out_of_place(items: List[Any]) -> List[Any]:
    """
    Return a new reversed copy of the list without modifying the original list.

    Args:
        items (List[Any]): Original list.

    Returns:
        List[Any]: New reversed list object.
    """
    return items[::-1]


def iterate_list_reversed(items: List[Any]) -> List[Any]:
    """
    Iterate over a list in reverse using built-in reversed() without mutating original list.

    Args:
        items (List[Any]): Original list.

    Returns:
        List[Any]: List constructed from the reverse iterator.
    """
    return list(reversed(items))


def compare_list_reversal_side_effects(original: List[int]) -> Dict[str, Any]:
    """
    Demonstrate side-effect differences between list.reverse(), list[::-1], and reversed().

    Args:
        original (List[int]): Sample integer list.

    Returns:
        Dict[str, Any]: Dictionary detailing returned values and list identity checks.
    """
    # Test 1: In-place reversal
    working_copy = list(original)
    return_val = working_copy.reverse()
    is_same_object_in_place = working_copy is original

    # Test 2: Extended slice
    slice_copy = original[::-1]
    is_same_object_slice = slice_copy is original

    # Test 3: Built-in reversed()
    iterator_obj = reversed(original)

    return {
        "original_unmodified": original,
        "in_place_mutated": working_copy,
        "in_place_return_value": return_val,  # None
        "slice_new_object": slice_copy,
        "is_same_object_in_place": is_same_object_in_place,
        "is_same_object_slice": is_same_object_slice,
        "iterator_type": type(iterator_obj).__name__,
    }


if __name__ == "__main__":
    print("=== Step 1: List Reversal & Memory Side Effects ===")
    sample_list = [10, 20, 30, 40, 50]

    print(f"Original List                  : {sample_list}")
    print(f"Out-of-place Slice [::-1]       : {reverse_list_out_of_place(sample_list)}")
    print(f"Lazy reversed() iterator list  : {iterate_list_reversed(sample_list)}")

    side_effects = compare_list_reversal_side_effects(sample_list)
    print(f"Side Effects Matrix            : {side_effects}")
