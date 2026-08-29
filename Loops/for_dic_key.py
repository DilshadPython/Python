"""Dictionary Keys, Values, and Item Iteration Patterns in Python.

Demonstrates iterating over dictionary keys directly, iterating via dict.keys(),
iterating over dict.values(), and looking up corresponding values by key.

Import Notes:
    - 'from typing import Dict, List, Tuple': Standard library typing module imports
      used for dict, list, and tuple type annotations.
"""

from typing import Dict, List, Tuple


def inspect_dictionary_keys(people: Dict[str, int]) -> List[str]:
    """Extract dictionary keys by direct iteration over the dictionary."""
    keys_list: List[str] = []
    for key in people:
        keys_list.append(key)
        print(key, end=" ")
    print()
    return keys_list


def inspect_dictionary_values(people: Dict[str, int]) -> List[int]:
    """Extract dictionary values using the dict.values() view object."""
    values_list: List[int] = []
    for age in people.values():
        values_list.append(age)
        print(age, end=" ")
    print()
    return values_list


def inspect_dictionary_key_value_pairs(people: Dict[str, int]) -> List[Tuple[str, int]]:
    """Iterate through keys using dict.keys() and lookup values by key indexing."""
    pairs: List[Tuple[str, int]] = []
    for key in people.keys():
        age = people[key]
        pairs.append((key, age))
        print(f"{key} is {age} years old.")
    return pairs


def demo_for_dic_key() -> Tuple[List[str], List[int], List[Tuple[str, int]]]:
    """Run demonstration of dictionary iteration techniques."""
    sample_people = {"Alan": 23, "Sara": 30, "Tom": 28, "Rachel": 27, "Anja": 25}

    print("--- 1. Direct Dictionary Key Iteration ---")
    keys = inspect_dictionary_keys(sample_people)

    print("\n--- 2. Dictionary Values View Iteration ---")
    values = inspect_dictionary_values(sample_people)

    print("\n--- 3. Dictionary Key Lookup Iteration ---")
    pairs = inspect_dictionary_key_value_pairs(sample_people)

    return keys, values, pairs


if __name__ == "__main__":
    demo_for_dic_key()
