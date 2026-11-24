"""
Demonstrates boolean state tracking during step accumulation trajectory.
"""
from typing import List, Tuple


def accumulate_with_status(target: int = 24) -> Tuple[List[Tuple[int, int]], bool]:
    """Accumulate steps and return trajectory along with final boolean status flag."""
    keep_going = True
    a = 0
    b = 0
    trajectory: List[Tuple[int, int]] = []

    while keep_going:
        a += 5
        b += 7
        trajectory.append((a, b))
        if a + b > target:
            keep_going = False

    return trajectory, keep_going


if __name__ == '__main__':
    traj, final_status = accumulate_with_status(24)
    print(f"Trajectory: {traj}, Final status: {final_status}")
