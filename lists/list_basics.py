# import built-in standard libraries that work with Python lists
import collections
import functools
import itertools
import operator
import random
from typing import List, Tuple, Union, Optional, Any, Dict

# Type Alias for numerical items in list processing
Number = Union[int, float]


def starter_list_examples() -> Dict[str, Any]:
    """Starter examples demonstrating Python Lists (list) for beginners.
    
    A list is an ordered, mutable collection of objects enclosed in square brackets [].
    """
    # 1. Creating lists
    fruits = ["apple", "banana", "cherry"]
    numbers = [10, 20, 30, 40, 50]

    # 2. Accessing by index & slicing
    first_fruit = fruits[0]           # Output: 'apple'
    sub_numbers = numbers[1:4]        # Output: [20, 30, 40]

    # 3. Modifying lists (mutable)
    fruits.append("orange")           # Adds to end
    fruits[1] = "blueberry"           # Modifies index 1
    removed_item = fruits.pop(0)      # Removes & returns index 0 ('apple')

    # 4. Membership testing & length
    has_cherry = "cherry" in fruits
    total_fruits = len(fruits)

    return {
        "remaining_fruits": fruits,
        "first_fruit_extracted": first_fruit,
        "sub_numbers_slice": sub_numbers,
        "removed_fruit": removed_item,
        "has_cherry": has_cherry,
        "total_fruits": total_fruits
    }


def manage_list_elements(
    elements: List[Any],
    item_to_add: Optional[Any] = None,
    remove_index: Optional[int] = None
) -> Tuple[List[Any], Optional[Any]]:
    """Appends new elements and pops elements by index with type & bound safety."""
    # Example Call: manage_list_elements([10, 20, 30], item_to_add=40, remove_index=0)
    # Explanation: Appends 40 to the end, then removes and returns item at index 0 (10).
    # Output Produced: ([20, 30, 40], 10)

    # Step 1: Validate input parameter types to ensure elements is a valid Python list.
    if not isinstance(elements, list):
        raise TypeError("First argument 'elements' must be a valid Python list")

    # Step 2: Make a shallow copy of the list to prevent mutating caller's original list in-place.
    working_list = elements.copy()
    popped_item = None

    # Step 3: Append new element if item_to_add is provided.
    if item_to_add is not None:
        working_list.append(item_to_add)

    # Step 4: Validate and perform pop operation if remove_index is specified.
    if remove_index is not None:
        if not isinstance(remove_index, int):
            raise TypeError("Index to remove must be an integer")
        if remove_index < -len(working_list) or remove_index >= len(working_list):
            raise IndexError("remove_index is out of range for the working list")
        popped_item = working_list.pop(remove_index)

    return working_list, popped_item


def slice_and_reverse_list(
    items: List[Any],
    start: Optional[int] = None,
    stop: Optional[int] = None,
    reverse: bool = False
) -> List[Any]:
    """Extracts a sub-list slice [start:stop] and optionally reverses the sequence."""
    # Example Call: slice_and_reverse_list(["Python", "Flask", "Django", "FastAPI"], start=0, stop=3, reverse=True)
    # Explanation: Slices elements from index 0 to 3 ('Python', 'Flask', 'Django'), then reverses them.
    # Output Produced: ['Django', 'Flask', 'Python']

    # Step 1: Validate input sequence type.
    if not isinstance(items, list):
        raise TypeError("Input 'items' must be a list")

    # Step 2: Extract sub-list slice using slice notation [start:stop].
    sliced_items = items[start:stop]

    # Step 3: Reverse slice using extended slice step [::-1] if requested.
    if reverse:
        return sliced_items[::-1]

    return sliced_items


def filter_and_transform_numbers(
    numbers: List[Number],
    threshold: Number = 0,
    multiplier: Number = 2
) -> List[Number]:
    """Filters numeric list elements above a threshold and multiplies them using list comprehension."""
    # Example Call: filter_and_transform_numbers([10, -5, 20, 0, 15], threshold=0, multiplier=2)
    # Explanation: Filters numbers > 0 ([10, 20, 15]) and multiplies each by 2.
    # Output Produced: [20, 40, 30]

    # Step 1: Validate input container type.
    if not isinstance(numbers, list):
        raise TypeError("Input 'numbers' must be a list")

    # Step 2: Validate numeric elements.
    for val in numbers:
        if not isinstance(val, (int, float)):
            raise TypeError("All elements in 'numbers' list must be int or float")

    # Step 3: Perform list comprehension [transform for item in collection if condition].
    return [num * multiplier for num in numbers if num > threshold]


def sort_elements_custom(
    items: List[Any],
    reverse: bool = False
) -> List[Any]:
    """Sorts list elements using built-in sorted() without modifying the original input list."""
    # Example Call: sort_elements_custom(["Python", "C", "JavaScript"], reverse=True)
    # Explanation: Returns a new sorted list in descending alphabetical order.
    # Output Produced: ['Python', 'JavaScript', 'C']

    # Step 1: Validate input list type.
    if not isinstance(items, list):
        raise TypeError("Input 'items' must be a list")

    # Step 2: Execute sorted() which uses CPython's Timsort algorithm O(N log N).
    return sorted(items, reverse=reverse)


def execute_all_dir_list_methods(initial_items: List[Any]) -> Dict[str, Any]:
    """Executes and returns results for all 11 built-in methods from dir(list)."""
    # Example Call: execute_all_dir_list_methods(["apple", "banana", "apple"])
    # Explanation: Runs append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort.
    if not isinstance(initial_items, list):
        raise TypeError("Input 'initial_items' must be a valid Python list")

    # Step 1: copy() - Shallow copy
    working = initial_items.copy()

    # Step 2: append() - Add element to tail
    working.append("cherry")

    # Step 3: extend() - Concatenate iterable elements
    working.extend(["date", "elderberry"])

    # Step 4: insert() - In-place insertion at index 1
    working.insert(1, "fig")

    # Step 5: count() - Count occurrences of an item
    cnt = working.count("apple")

    # Step 6: index() - Positional index lookup
    idx = working.index("fig")

    # Step 7: pop() - Remove & return element at index 0
    popped = working.pop(0)

    # Step 8: remove() - Remove first occurrence of value
    if "cherry" in working:
        working.remove("cherry")

    # Step 9: reverse() - Reverse list in-place
    working.reverse()

    # Step 10: sort() - In-place sort (convert elements to string for uniform comparison)
    str_list = [str(item) for item in working]
    str_list.sort()

    # Step 11: clear() - Empty list in-place
    cleared = working.copy()
    cleared.clear()

    return {
        "copy": initial_items.copy(),
        "modified_list": working,
        "count_apple": cnt,
        "index_fig": idx,
        "popped_first": popped,
        "sorted_strings": str_list,
        "cleared_list": cleared
    }


def process_list_with_standard_libraries(
    items: List[Any],
    numbers: List[int]
) -> Dict[str, Any]:
    """Demonstrates standard libraries (collections, itertools, functools, operator, random) working with lists."""
    # Example Call: process_list_with_standard_libraries(["apple", "banana", "apple"], [1, 2, 3, 4, 5])
    # Explanation: Integrates deque, Counter, chain, combinations, reduce, itemgetter, and random.
    if not isinstance(items, list) or not isinstance(numbers, list):
        raise TypeError("Arguments 'items' and 'numbers' must be valid Python lists")

    # 1. collections library: deque (O(1) fast appends/pops from left) & Counter (frequency map)
    dq = collections.deque(items)
    dq.appendleft("first_header")
    freq_map = dict(collections.Counter(items))

    # 2. itertools library: chain (iterables joining) & combinations (sub-group pairings)
    chained = list(itertools.chain(items, ["extra_1", "extra_2"]))
    combos = list(itertools.combinations(numbers[:3], 2))

    # 3. functools library: reduce (cumulative list summation)
    reduced_sum = functools.reduce(lambda a, b: a + b, numbers, 0)

    # 4. operator library: itemgetter (sort list of dicts by key)
    records = [{"name": "Dilshad", "score": 98}, {"name": "Monika", "score": 92}]
    sorted_recs = sorted(records, key=operator.itemgetter("score"), reverse=True)

    # 5. random library: sample & shuffle (using seeded RNG for reproducibility)
    rng = random.Random(42)
    sampled = rng.sample(items, min(2, len(items))) if items else []
    shuffled = items.copy()
    rng.shuffle(shuffled)

    return {
        "deque_left_append": list(dq),
        "counter_frequency": freq_map,
        "itertools_chain": chained,
        "itertools_combinations": combos,
        "functools_reduce_sum": reduced_sum,
        "operator_sorted_records": sorted_recs,
        "random_sample": sampled,
        "random_shuffled": shuffled
    }
