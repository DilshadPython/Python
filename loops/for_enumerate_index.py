"""Enumerated Loop Iteration with 'enumerate()' in Python.

Demonstrates using built-in enumerate() to obtain both automatic index counters
and item values during sequence iteration, including nested iteration patterns.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing imports for list and tuple hints.
"""

from typing import List, Tuple


def generate_enumerated_pairs(
    names: List[str], numbers: List[int], alphas: List[str]
) -> List[Tuple[int, str, str]]:
    """Iterate through names and pair them with enumerated numbers and alphabets.

    Args:
        names: List of person names.
        numbers: List of numeric values.
        alphas: List of alphabet character strings.

    Returns:
        List of generated tuples containing (index, name, paired_item).
    """
    records: List[Tuple[int, str, str]] = []

    for name in names:
        for index, num in enumerate(numbers):
            records.append((index, name, str(num)))
            print(f"Index: {index} | Name: {name:<8s} | Number: {num}")

        for index, char in enumerate(alphas):
            records.append((index, name, char))
            print(f"Index: {index} | Name: {name:<8s} | Alpha: {char}")

    return records


def demo_for_enumerate_index() -> None:
    """Run demonstration of enumerate() index loop tracking."""
    sample_names = ["Tom", "Chris", "Julia", "Rob", "Claudio", "Sarah", "Amanda"]
    sample_numbers = [1, 2, 3, 4, 5, 6, 7]
    sample_alphas = ["A", "B", "C", "D", "E", "F", "G"]

    print("--- Running Enumerate Index Loop Demo ---")
    results = generate_enumerated_pairs(sample_names, sample_numbers, sample_alphas)
    print(f"Generated total enumerated records: {len(results)}")


if __name__ == "__main__":
    demo_for_enumerate_index()
