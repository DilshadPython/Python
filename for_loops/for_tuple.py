"""Tuple Iteration, Accumulation, and String Length Analysis in Python.

Demonstrates iterating over tuples, calculating total sums, and identifying the item
with the longest string length using range-based tuple index comparison. Corrects city names.

Import Notes:
    - 'from typing import Tuple, List': Standard library typing module imports
      used for static type hints on tuple sequences and return types.
"""

from typing import Tuple, List


def iterate_tuple_elements(elements: Tuple[int, ...]) -> List[int]:
    """Iterate through tuple elements and print them horizontally."""
    seen: List[int] = []
    for item in elements:
        seen.append(item)
        print(item, end=" ")
    print()
    return seen


def accumulate_tuple_sum(numbers: Tuple[int, ...]) -> int:
    """Calculate total sum of integers in a tuple using an accumulator loop."""
    total = 0
    print("Accumulating tuple elements:")
    for num in numbers:
        print(f"Adding {num:2d} -> Running Total: {total + num:3d}")
        total += num
    print(f"Total of all numbers: {total}")
    return total


def find_longest_string_in_tuple(names: Tuple[str, ...]) -> Tuple[str, int]:
    """Find the longest string item in a tuple using index length comparisons.

    Args:
        names: Tuple of strings.

    Returns:
        Tuple containing (longest_string, index_position).
    """
    longest_idx = 0
    for x in range(1, len(names)):
        if len(names[x]) > len(names[longest_idx]):
            longest_idx = x

    longest_name = names[longest_idx]
    print(f"The longest city name is: '{longest_name}' (Length: {len(longest_name)})")
    return longest_name, longest_idx


def demo_for_tuple() -> None:
    """Run tuple iteration, summation, and string analysis demonstration."""
    print("--- 1. Direct Literal Tuple Iteration ---")
    iterate_tuple_elements((2, 4, 6, 3, 7, 9, 1, 5, 8, 10, 15, 17, 21))

    print("\n--- 2. Tuple Variable Iteration ---")
    sample_numbers = (22, 14, 6, 3, 71, 9, 1, 5, 8, 18, 5, 17, 11)
    iterate_tuple_elements(sample_numbers)

    # Corrected spelling: 'Bruccel' -> 'Brussels', 'Roma' -> 'Rome'
    cities = ("Paris", "London", "Berlin", "Tokyo", "Brussels", "Rome")

    print("\n--- 3. City Tuple Iteration ---")
    for name in cities:
        print(name, end=" ")
    print()

    print("\n--- 4. Tuple Sum Accumulation ---")
    accumulate_tuple_sum((1, 2, 4, 6, 3, 7, 9, 1, 5, 8, 10, 15))

    print("\n--- 5. Finding Longest City Name ---")
    find_longest_string_in_tuple(cities)


if __name__ == "__main__":
    demo_for_tuple()
