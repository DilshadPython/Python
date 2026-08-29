"""Building Floor Navigation & Elevator Simulator.

Simulates an elevator ascending through floors using a 'for' loop, validating
user-specified target floors against building constraints.

Import Notes:
    - 'from typing import Tuple, List, Optional': Standard library typing module imports
      used for returning structured tuple, list, and optional type annotations.
"""

from typing import Tuple, List, Optional


def navigate_elevator(target_floor: int, total_floors: int = 12) -> Tuple[bool, List[int]]:
    """Simulate elevator movement floor by floor to reach a target floor.

    Args:
        target_floor: The requested destination floor number.
        total_floors: Total number of floors in the building (default: 12).

    Returns:
        Tuple containing a success boolean and a list of visited floor numbers.
    """
    if target_floor < 1 or target_floor > total_floors:
        print(f"Invalid floor: {target_floor}. Please enter a floor between 1 and {total_floors}.")
        return False, []

    visited_floors: List[int] = []
    print(f"Elevator starting ascent to floor {target_floor} (Building total: {total_floors} floors)...")

    for current_floor in range(1, total_floors + 1):
        visited_floors.append(current_floor)
        print(f"Elevator passing floor {current_floor}...")
        if current_floor == target_floor:
            print(f"You have reached your destination floor: {current_floor}")
            break

    return True, visited_floors


def demo_elevator(input_floor: Optional[int] = 5) -> Tuple[bool, List[int]]:
    """Run demonstration of elevator floor navigation.

    Args:
        input_floor: Optional target floor number for demo execution (default: 5).

    Returns:
        Tuple containing destination reach status and visited floor numbers.
    """
    print("--- Elevator Floor Navigation Simulation ---")
    target = input_floor if input_floor is not None else 5
    return navigate_elevator(target, 12)


if __name__ == "__main__":
    demo_elevator()
