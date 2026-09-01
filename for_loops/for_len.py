"""Sequence Indexing using range(len()) vs Pythonic enumerate().

Demonstrates 1-based index listing of Python library names using range(len())
and contrasts it with Pythonic enumerate() iteration. Corrects library spelling.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing module imports
      used for static type annotations on library lists and output tuples.
"""

from typing import List, Tuple


def get_python_libraries() -> List[str]:
    """Return a curated list of Python data science and machine learning libraries."""
    # Corrected spelling: 'statesmodels' -> 'statsmodels'
    return [
        "pandas",
        "numpy",
        "scipy",
        "scikit-learn",
        "statsmodels",
        "NLTK",
        "seaborn",
        "matplotlib",
        "tensorflow",
        "keras",
    ]


def list_libraries_via_range_len(libraries: List[str]) -> List[Tuple[int, str]]:
    """Format and print libraries using range(len(libraries)) index lookup.

    Args:
        libraries: List of library names.

    Returns:
        List of tuples: (1-based_index, library_name).
    """
    results: List[Tuple[int, str]] = []
    print("--- Listing Libraries using range(len()) ---")
    for idx in range(len(libraries)):
        position = idx + 1
        lib_name = libraries[idx]
        results.append((position, lib_name))
        print(f"{position:2d}. {lib_name}")
    return results


def list_libraries_via_enumerate(libraries: List[str]) -> List[Tuple[int, str]]:
    """Format and print libraries using Pythonic enumerate(libraries, start=1).

    Args:
        libraries: List of library names.

    Returns:
        List of tuples: (1-based_index, library_name).
    """
    results: List[Tuple[int, str]] = []
    print("\n--- Listing Libraries using Pythonic enumerate() ---")
    for position, lib_name in enumerate(libraries, start=1):
        results.append((position, lib_name))
        print(f"{position:2d}. {lib_name}")
    return results


def demo_for_len() -> None:
    """Run demonstration comparing range(len()) vs enumerate()."""
    libraries = get_python_libraries()
    list_libraries_via_range_len(libraries)
    list_libraries_via_enumerate(libraries)


if __name__ == "__main__":
    demo_for_len()