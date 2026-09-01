"""Elevator Floor Simulation (Spelling Correction: 'exculator' -> 'elevator').

This module provides backwards compatibility for 'exculator.py', fixing the
original type error ('for floor in floors' where floors was an int) and delegating
execution to the corrected 'elevator.py' module.

Import Notes:
    - 'from typing import Tuple, List, Optional': Standard library typing module imports
      used for static type checking annotations.
    - 'from elevator import navigate_elevator, demo_elevator': Imports floor navigation
      functions from the corrected elevator module.
"""

from typing import Tuple, List, Optional
from elevator import navigate_elevator, demo_elevator


def run_exculator_simulation(target_floor: int = 5) -> Tuple[bool, List[int]]:
    """Execute corrected floor navigation simulation.

    Args:
        target_floor: Target floor number (1 to 12).

    Returns:
        Tuple of success status and list of visited floor numbers.
    """
    return navigate_elevator(target_floor, 12)


if __name__ == "__main__":
    demo_elevator()
