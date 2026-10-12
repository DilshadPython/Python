"""
Container Reversal Helpers & Dictionary View Reversal Module.

This module demonstrates advanced sequence reversal across standard containers:
- Dictionary view reversal (dict.keys(), dict.values(), dict.items()) added in Python 3.8
- In-place deque reversal using collections.deque.reverse()
- Reversing tuples and converting iterators to reverse views
- Materializing non-reversible collections (sets, generator objects) before reversing
"""
# "from collections import deque" imports double-ended queue data structure.
from collections import deque
# "from typing import Dict, List, Tuple, Any" imports type hint annotations.
from typing import Dict, List, Tuple, Any


def reverse_dictionary_views(data_dict: Dict[str, Any]) -> Dict[str, List[Any]]:
    """
    Demonstrate dict key, value, and item reversal introduced in Python 3.8.

    Since Python 3.7+, standard dicts maintain insertion order. Python 3.8+ implemented
    the __reversed__() hook for dict_keys, dict_values, and dict_items views.

    Args:
        data_dict (Dict[str, Any]): Input dictionary.

    Returns:
        Dict[str, List[Any]]: Reversed keys, values, and key-value items lists.
    """
    reversed_keys = list(reversed(data_dict.keys()))
    reversed_values = list(reversed(data_dict.values()))
    reversed_items = list(reversed(data_dict.items()))

    return {
        "reversed_keys": reversed_keys,
        "reversed_values": reversed_values,
        "reversed_items": reversed_items,
    }


def reverse_deque_in_place(elements: List[Any]) -> List[Any]:
    """
    Demonstrate in-place double-ended queue reversal using collections.deque.reverse().

    Args:
        elements (List[Any]): List of elements to populate deque.

    Returns:
        List[Any]: List representation of reversed deque.
    """
    d = deque(elements)
    d.reverse()  # In-place reversal of deque
    return list(d)


def reverse_tuple_sequence(tpl: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """
    Reverse an immutable tuple sequence using extended slicing [::-1] or tuple(reversed(tpl)).

    Args:
        tpl (Tuple[Any, ...]): Original tuple.

    Returns:
        Tuple[Any, ...]: Reversed tuple instance.
    """
    return tpl[::-1]


def reverse_generator_or_set(unordered_obj: Any) -> List[Any]:
    """
    Safely reverse non-reversible or unordered objects (like sets or generator expressions).

    Sets and raw generators do NOT implement __reversed__() or sequence indexing.
    They must be materialized into a list or tuple before reversing.

    Args:
        unordered_obj (Any): Set, generator, or non-reversible iterator.

    Returns:
        List[Any]: Reversed list representation.
    """
    return list(reversed(list(unordered_obj)))


if __name__ == "__main__":
    print("=== Step 2: Advanced Container & Dict View Reversal ===")
    sample_dict = {"a": 1, "b": 2, "c": 3}

    print(f"Original Dict          : {sample_dict}")
    print(f"Reversed Dict Views    : {reverse_dictionary_views(sample_dict)}")
    print(f"Reversed Deque         : {reverse_deque_in_place([100, 200, 300])}")
    print(f"Reversed Tuple         : {reverse_tuple_sequence((1, 2, 3, 4))}")
    print(f"Reversed Set/Generator : {reverse_generator_or_set({10, 20, 30})}")
