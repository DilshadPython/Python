"""
Iterator Module: Master Demonstration Entrypoint.

This script demonstrates Python's built-in iterator mechanics across sequences, custom classes,
dictionary views, file handles, and range sequences.
"""
# "from typing import List, Tuple, Dict, Any" imports type hint annotations.
from typing import List, Tuple, Dict, Any


def demonstrate_basic_iteration() -> Tuple[List[str], List[int]]:
    """
    Demonstrate iterating over strings and integer sequences using iter() and next().

    Returns:
        Tuple[List[str], List[int]]: Extracted list elements.
    """
    cities = ["Paris", "London", "Berlin", "Tokyo"]
    city_iter = iter(cities)
    extracted_cities = [next(city_iter), next(city_iter)]

    numbers = range(1, 6)
    num_iter = iter(numbers)
    extracted_numbers = [next(num_iter), next(num_iter), next(num_iter)]

    return extracted_cities, extracted_numbers


def demonstrate_dict_iteration() -> Dict[str, Any]:
    """
    Demonstrate iterating over dictionary keys and key-value items.

    Returns:
        Dict[str, Any]: Dictionary of extracted keys and values.
    """
    grades = {"Alan": 23, "Sara": 30, "Tom": 28}
    key_iter = iter(grades)
    first_key = next(key_iter)

    return {
        "first_key": first_key,
        "first_value": grades[first_key],
        "all_keys": list(iter(grades)),
    }


if __name__ == "__main__":
    print("=== Python Iterator Master Demonstration ===")
    cities, nums = demonstrate_basic_iteration()
    print(f"  Extracted Cities  : {cities}")
    print(f"  Extracted Numbers : {nums}")

    dict_info = demonstrate_dict_iteration()
    print("\n=== Dictionary Iteration ===")
    print(f"  First Key/Value   : {dict_info['first_key']} -> {dict_info['first_value']}")
    print(f"  All Keys          : {dict_info['all_keys']}")
