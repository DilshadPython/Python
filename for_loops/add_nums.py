"""Numeric List Accumulation and Set Deduplication in Python Loops.

Demonstrates accumulating values in a list using an explicit 'for' loop accumulator
versus Python's built-in sum() function, alongside set deduplication.

Import Notes:
    - 'from typing import List, Set, Tuple': Imports generic container type hints
      List, Set, and Tuple from standard library 'typing' to specify argument and return types.
"""

from typing import List, Set, Tuple


def accumulate_list_manually(numbers: List[int]) -> int:
    """Calculate the sum of integers using an explicit 'for' loop accumulator."""
    running_total = 0
    for num in numbers:
        running_total += num
        print(f"Current value: {num:2d} | Running Total: {running_total:3d}")
    return running_total


def accumulate_list_builtin(numbers: List[int]) -> int:
    """Calculate the sum of integers using Python's built-in sum() function."""
    return sum(numbers)


def deduplicate_numbers(numbers: List[int]) -> Set[int]:
    """Remove duplicate numbers by casting the input list to a set."""
    unique_set = set(numbers)
    print(f"Original List ({len(numbers)} items): {numbers}")
    print(f"Deduplicated Set ({len(unique_set)} unique items): {unique_set}")
    return unique_set


def demo_add_nums() -> Tuple[int, int, Set[int]]:
    """Execute loop accumulation and deduplication demonstration."""
    sample_numbers = [4, 5, 7, 5, 4, 8]
    
    print("--- 1. Manual Accumulation Loop ---")
    manual_sum = accumulate_list_manually(sample_numbers)
    
    print("\n--- 2. Built-in sum() Function ---")
    builtin_sum = accumulate_list_builtin(sample_numbers)
    print(f"Built-in sum() total: {builtin_sum}")
    
    print("\n--- 3. Set Deduplication ---")
    unique_numbers = deduplicate_numbers(sample_numbers)
    
    return manual_sum, builtin_sum, unique_numbers


if __name__ == "__main__":
    demo_add_nums()
