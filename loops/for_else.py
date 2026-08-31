"""Demonstrating the 'for-else' Loop Control Structure in Python.

In Python, a 'for' loop can have an optional 'else' clause. The 'else' block
executes ONLY if the loop completes all iterations normally (i.e. without encountering
a 'break' statement).

Import Notes:
    - 'from typing import List, Tuple': Standard library typing imports for list and tuple type hints.
"""

from typing import List, Tuple


def search_technology_stack(tech_list: List[str], target: str) -> Tuple[bool, str]:
    """Search for a target technology in a list using the 'for-else' loop construct.

    Args:
        tech_list: List of technology stack names.
        target: Technology name to search for.

    Returns:
        Tuple containing a boolean success flag and a status message string.
    """
    for name in tech_list:
        if name == target:
            msg = f"{target} is found"
            print(msg)
            return True, msg
    else:
        # Executed only if loop finishes without hitting 'break'
        msg = f"{target} not found"
        print(msg)
        return False, msg


def demo_for_else() -> Tuple[Tuple[bool, str], Tuple[bool, str]]:
    """Run demonstration of 'for-else' search behavior."""
    technologies = ["Python", "Java", "C++", "Django", "JavaScript"]

    print("--- 1. Searching for missing item ('DotNet') ---")
    res1 = search_technology_stack(technologies, "DotNet")

    print("\n--- 2. Searching for existing item ('Java') ---")
    res2 = search_technology_stack(technologies, "Java")

    return res1, res2


if __name__ == "__main__":
    demo_for_else()