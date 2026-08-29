"""List Iteration and Slicing Patterns in Python 'for' Loops.

Demonstrates iterating through direct literal lists, list variables, and list slices
using positive, negative, and step indexing slice notation. Corrects city spellings.

Import Notes:
    - 'from typing import List, Any, Optional': Standard library typing imports for generic sequence
      and optional slicing parameter annotations.
"""

from typing import List, Any, Optional


def iterate_entire_list(items: List[Any]) -> List[Any]:
    """Iterate through all items in a list and return them as a sequence."""
    processed: List[Any] = []
    for item in items:
        processed.append(item)
        print(item, end=" ")
    print()
    return processed


def iterate_list_slice(
    items: List[str], start: Optional[int] = None, stop: Optional[int] = None
) -> List[str]:
    """Iterate through a specified slice of a string list.

    Args:
        items: Source list of strings.
        start: Optional slice start index.
        stop: Optional slice end index.

    Returns:
        Sublist of iterated elements.
    """
    slice_segment = items[start:stop]
    print(f"Slice items[{start}:{stop}] -> {slice_segment}:")
    for item in slice_segment:
        print(item, end=" ")
    print()
    return slice_segment


def demo_for_list() -> None:
    """Run list iteration and slice loop demonstration."""
    print("--- 1. Direct Literal List Iteration ---")
    iterate_entire_list([2, 4, 6, 3, 7, 9, 1, 5, 8, 10, 15, 17, 21])

    print("\n--- 2. Named List Variable Iteration ---")
    numbers = [22, 14, 6, 3, 71, 9, 1, 5, 8, 18, 5, 17, 11]
    iterate_entire_list(numbers)

    # Corrected spelling: 'Bruccel' -> 'Brussels', 'Roma' -> 'Rome'
    cities = ["Paris", "London", "Berlin", "Tokyo", "Brussels", "Rome"]

    print("\n--- 3. Full City List Iteration ---")
    iterate_entire_list(cities)

    print("\n--- 4. Slice Iteration [2:5] ---")
    iterate_list_slice(cities, 2, 5)

    print("\n--- 5. Slice Iteration [:4] ---")
    iterate_list_slice(cities, None, 4)

    print("\n--- 6. Negative Slice Iteration [:-5] ---")
    iterate_list_slice(cities, None, -5)

    print("\n--- 7. Negative Slice Iteration [-4:] ---")
    iterate_list_slice(cities, -4, None)

    print("\n--- 8. Negative Slice Range Iteration [-4:-1] ---")
    iterate_list_slice(cities, -4, -1)


if __name__ == "__main__":
    demo_for_list()
