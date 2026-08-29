"""Sequence Lookup via Range-Based Index Iteration in Python.

Demonstrates searching through list elements using range(len(list)) indexing
versus fixed range(0, N) index iteration. Corrects vehicle name spellings.

Import Notes:
    - 'from typing import List, Tuple': Standard library typing module imports
      used for static type annotations on vehicle list and status tuple returns.
"""

from typing import List, Tuple


def search_car_inventory_fixed_range(
    cars: List[str], target: str = "Porsche"
) -> Tuple[bool, List[str]]:
    """Search list for a target car using a fixed range(0, 5) index loop.

    Args:
        cars: List of vehicle brand strings.
        target: Target car brand to search for (default: "Porsche").

    Returns:
        Tuple containing a boolean found flag and a list of output status strings.
    """
    statuses: List[str] = []
    found = False

    # Fixed range iteration
    for x in range(0, min(5, len(cars))):
        if cars[x] == target:
            msg = f"The {cars[x]} already exists"
            statuses.append(msg)
            print(msg)
            found = True
        else:
            msg = "Not found"
            statuses.append(msg)
            print(msg)

    return found, statuses


def search_car_inventory_dynamic_range(
    cars: List[str], target: str = "Fiat"
) -> Tuple[bool, List[str]]:
    """Search list for a target car using dynamic range(len(cars)) index loop.

    Args:
        cars: List of vehicle brand strings.
        target: Target car brand to search for (default: "Fiat").

    Returns:
        Tuple containing a boolean found flag and a list of output status strings.
    """
    statuses: List[str] = []
    found = False

    # Dynamic range(len()) iteration
    for x in range(len(cars)):
        if cars[x] == target:
            msg = f"The {cars[x]} already exists"
            statuses.append(msg)
            print(msg)
            found = True
        else:
            msg = "Not found"
            statuses.append(msg)
            print(msg)

    return found, statuses


def demo_for_index() -> None:
    """Run demonstration of fixed and dynamic range index searches."""
    # Corrected spelling: 'Alfa Romie' -> 'Alfa Romeo', 'Porsh' -> 'Porsche'
    cars = ["Audi", "Fiat", "Alfa Romeo", "Porsche", "Volvo"]

    print("--- 1. Fixed Range Index Search ('Porsche') ---")
    search_car_inventory_fixed_range(cars, "Porsche")

    print("\n--- 2. Dynamic range(len()) Index Search ('Fiat') ---")
    search_car_inventory_dynamic_range(cars, "Fiat")


if __name__ == "__main__":
    demo_for_index()
