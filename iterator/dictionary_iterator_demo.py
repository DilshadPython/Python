"""
Dictionary Iterator Demonstration Module.

This module demonstrates key, value, and item view iteration mechanics in Python dictionaries.
"""
# "from typing import Dict, List, Any" imports type hint annotations.
from typing import Dict, List, Any


def demonstrate_dict_iterators(names: Dict[str, int]) -> Dict[str, Any]:
    """
    Extract dictionary keys and items using iterators and loops.

    Args:
        names (Dict[str, int]): Map of names to ages.

    Returns:
        Dict[str, Any]: Extracted keys and formatted strings.
    """
    key_iterator = iter(names)
    first_three_keys = [next(key_iterator) for _ in range(3)]

    all_entries = [f"{key}: {names[key]}" for key in names]

    return {
        "first_three_keys": first_three_keys,
        "all_entries": all_entries,
    }


if __name__ == "__main__":
    print("=== Dictionary Iterator Demonstration ===")
    sample_names = {"Alan": 23, "Sara": 30, "Tom": 28, "Raechel": 27, "Anja": 25}
    results = demonstrate_dict_iterators(sample_names)
    print(f"First three keys extracted via next(): {results['first_three_keys']}")
    print("All entries traversed via dictionary iterator:")
    for entry in results["all_entries"]:
        print(f"  {entry}")
