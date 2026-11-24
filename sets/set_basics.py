import collections
import itertools
import operator
import sys
from typing import Set, FrozenSet, List, Dict, Any, Union

Number = Union[int, float]


def starter_set_examples() -> Dict[str, Any]:
    """Starter examples demonstrating Python Sets (set) for beginners.
    
    A set is an unordered collection of unique elements that automatically removes duplicates.
    """
    # 1. Creating sets & automatic deduplication
    numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
    unique_numbers = set(numbers_with_duplicates)
    fruit_set = {"apple", "banana", "cherry"}

    # 2. Adding and removing elements
    fruit_set.add("orange")
    fruit_set.discard("banana")  # Safe remove (no error if missing)

    # 3. Fast membership testing
    has_apple = "apple" in fruit_set
    has_banana = "banana" in fruit_set

    # 4. Basic set math operations for beginners
    set_a = {"python", "javascript", "c++"}
    set_b = {"python", "sql", "html"}
    common_skills = set_a & set_b  # Intersection
    all_skills = set_a | set_b     # Union

    return {
        "original_list": numbers_with_duplicates,
        "unique_numbers": sorted(list(unique_numbers)),
        "modified_fruit_set": sorted(list(fruit_set)),
        "has_apple": has_apple,
        "has_banana": has_banana,
        "common_skills_intersection": sorted(list(common_skills)),
        "all_skills_union": sorted(list(all_skills))
    }


def set_operations_and_math(set_a: Set[Any], set_b: Set[Any]) -> Dict[str, Any]:
    """Demonstrates set mathematical operations: Union (|), Intersection (&), Difference (-), Symmetric Difference (^)."""
    if not isinstance(set_a, set) or not isinstance(set_b, set):
        raise TypeError("Inputs must be Python sets")

    union_res = set_a | set_b
    intersection_res = set_a & set_b
    difference_res = set_a - set_b
    sym_diff_res = set_a ^ set_b

    return {
        "union": sorted(list(union_res)),
        "intersection": sorted(list(intersection_res)),
        "difference": sorted(list(difference_res)),
        "symmetric_difference": sorted(list(sym_diff_res)),
        "is_subset": set_a.issubset(union_res),
        "is_disjoint": set_a.isdisjoint({"non_existent_item_xyz"})
    }


def execute_all_dir_set_methods(initial_elements: List[Any]) -> Dict[str, Any]:
    """Executes ALL 17 built-in public methods from dir(set): add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset, pop, remove, symmetric_difference, symmetric_difference_update, union, update."""
    if not isinstance(initial_elements, list):
        raise TypeError("Input must be a list")

    # 1. add & copy
    s1 = set(initial_elements)
    s1.add("new_element")
    s2 = s1.copy()

    # 2. discard & remove
    s2.discard("non_existent")  # Safe remove (no error)
    rem_demo = s1.copy()
    if "new_element" in rem_demo:
        rem_demo.remove("new_element")

    # 3. clear & pop
    clear_demo = s1.copy()
    clear_demo.clear()
    pop_demo = s1.copy()
    popped = pop_demo.pop() if pop_demo else None

    # 4. difference & difference_update
    diff = s1.difference({"new_element"})
    diff_up = s1.copy()
    diff_up.difference_update({"new_element"})

    # 5. intersection & intersection_update
    inter = s1.intersection({"new_element", "item_x"})
    inter_up = s1.copy()
    inter_up.intersection_update({"new_element", "item_x"})

    # 6. isdisjoint, issubset, issuperset
    is_disj = s1.isdisjoint({"unknown_xyz"})
    is_sub = s1.issubset(s1 | {"extra"})
    is_super = s1.issuperset({"new_element"}) if "new_element" in s1 else False

    # 7. symmetric_difference & symmetric_difference_update
    sym_diff = s1.symmetric_difference({"item_x", "diff_val"})
    sym_up = s1.copy()
    sym_up.symmetric_difference_update({"item_x", "diff_val"})

    # 8. union & update
    union_set = s1.union({"union_item"})
    s1.update(["item_x", "item_y"])

    # Frozenset demonstration
    frozen = frozenset(["immutable_1", "immutable_2"])

    return {
        "dir_set_methods_count": len([m for m in dir(set) if not m.startswith("_")]),
        "modified_set": sorted([str(x) for x in s1]),
        "popped_element": popped,
        "cleared_set_len": len(clear_demo),
        "removed_set": sorted([str(x) for x in rem_demo]),
        "difference_set": sorted([str(x) for x in diff]),
        "difference_update_set": sorted([str(x) for x in diff_up]),
        "intersection_set": sorted([str(x) for x in inter]),
        "intersection_update_set": sorted([str(x) for x in inter_up]),
        "is_disjoint": is_disj,
        "is_subset": is_sub,
        "is_superset": is_super,
        "symmetric_difference": sorted([str(x) for x in sym_diff]),
        "symmetric_difference_update": sorted([str(x) for x in sym_up]),
        "union_set": sorted([str(x) for x in union_set]),
        "frozenset_instance": sorted(list(frozen))
    }


def process_set_with_standard_libraries(items: List[Any], target_item: Any) -> Dict[str, Any]:
    """Demonstrates standard libraries working with sets: frozenset, collections.Counter, itertools, operator, sys."""
    if not isinstance(items, list):
        raise TypeError("Input 'items' must be a valid Python list")

    # 1. frozenset (usable as dictionary keys)
    frozen_key = frozenset(items)
    dict_with_frozen_key = {frozen_key: "valid_dict_value"}

    # 2. collections.Counter multiset operations (& and |)
    c1 = collections.Counter(["a", "b", "a", "c"])
    c2 = collections.Counter(["a", "b", "b", "d"])
    multiset_intersection = c1 & c2  # Min counts
    multiset_union = c1 | c2         # Max counts

    # 3. itertools.combinations on set elements
    unique_set = set(items)
    set_combos = list(itertools.combinations(sorted([str(x) for x in unique_set]), 2)) if len(unique_set) >= 2 else []

    # 4. operator.contains functional check
    contains_target = operator.contains(unique_set, target_item)

    # 5. sys.getsizeof benchmark
    sample_list = list(range(1000))
    sample_set = set(sample_list)

    return {
        "frozen_key_dict": dict_with_frozen_key[frozen_key],
        "multiset_intersection": dict(multiset_intersection),
        "multiset_union": dict(multiset_union),
        "itertools_set_combinations": set_combos,
        "operator_contains_target": contains_target,
        "set_bytes_vs_list": {
            "list_bytes": sys.getsizeof(sample_list),
            "set_bytes": sys.getsizeof(sample_set)
        }
    }
