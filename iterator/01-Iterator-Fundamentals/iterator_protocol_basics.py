"""
Iterator Protocol Basics Module.

This module demonstrates core Python iterator mechanics:
- Iterables vs Iterators (iter() and next() built-in functions)
- StopIteration exception handling in manual iteration loops
- Default values in next(iterator, default) to prevent StopIteration
- Verifying the Iterator protocol using isinstance() and collections.abc
"""
# "from collections.abc import Iterable, Iterator" imports abstract base classes for type checking.
from collections.abc import Iterable, Iterator
# "from typing import List, Any, Tuple" imports typing annotations.
from typing import List, Any, Tuple


def verify_iterable_and_iterator(obj: Any) -> Tuple[bool, bool]:
    """
    Check if an object implements the Iterable and Iterator abstract base classes.

    Args:
        obj (Any): Input Python object.

    Returns:
        Tuple[bool, bool]: Tuple of (is_iterable, is_iterator).
    """
    is_iterable = isinstance(obj, Iterable)
    is_iterator = isinstance(obj, Iterator)
    return is_iterable, is_iterator


def manual_iteration_with_stop_iteration(items: List[Any]) -> List[Any]:
    """
    Simulate Python's for-loop under the hood using explicit iter(), next(), and try-except StopIteration.

    Args:
        items (List[Any]): List of items to iterate over.

    Returns:
        List[Any]: Collected items extracted manually.
    """
    result: List[Any] = []
    iterator = iter(items)

    while True:
        try:
            item = next(iterator)
            result.append(item)
        except StopIteration:
            break

    return result


def fetch_next_with_default(items: List[Any], fetch_count: int, default_value: Any = "END") -> List[Any]:
    """
    Fetch elements from an iterator using next(iterator, default) to safely handle exhaustion.

    Args:
        items (List[Any]): Input sequence.
        fetch_count (int): Number of times to call next().
        default_value (Any): Default value returned when iterator is exhausted. Defaults to "END".

    Returns:
        List[Any]: List of fetched items including defaults if exhausted.
    """
    iterator = iter(items)
    fetched: List[Any] = []

    for _ in range(fetch_count):
        val = next(iterator, default_value)
        fetched.append(val)

    return fetched


if __name__ == "__main__":
    print("=== Step 1: Iterator Protocol Basics ===")
    sample_list = ["Paris", "London", "Berlin", "Tokyo"]

    is_iter, is_iterator = verify_iterable_and_iterator(sample_list)
    print(f"sample_list -> is_iterable: {is_iter}, is_iterator: {is_iterator}")

    list_iterator = iter(sample_list)
    is_iter2, is_iterator2 = verify_iterable_and_iterator(list_iterator)
    print(f"iter(sample_list) -> is_iterable: {is_iter2}, is_iterator: {is_iterator2}")

    manual_items = manual_iteration_with_stop_iteration(sample_list)
    print(f"Manual try-except StopIteration loop : {manual_items}")

    safe_fetched = fetch_next_with_default(sample_list, 6, default_value="<EXHAUSTED>")
    print(f"next(iter, default) safe fetches        : {safe_fetched}")

