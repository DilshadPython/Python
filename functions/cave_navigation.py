"""
Demonstrates graph-like cave navigation data structure manipulation via functions.
"""
# "import module" imports the full standard library "random" module into local scope.
import random
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Dict, List, Optional


def create_tunnel(caves: Dict[int, List[int]], cave_from: int, cave_to: int) -> None:
    """Create a bidirectional tunnel between cave_from and cave_to."""
    caves.setdefault(cave_from, []).append(cave_to)
    caves.setdefault(cave_to, []).append(cave_from)


def visit_cave(visited_caves: List[int], unvisited_caves: List[int], cave_number: int) -> None:
    """Mark a cave as visited and remove from unvisited list."""
    visited_caves.append(cave_number)
    if cave_number in unvisited_caves:
        unvisited_caves.remove(cave_number)


def choose_cave(caves: Dict[int, List[int]], cave_list: List[int], rng_seed: Optional[int] = None) -> int:
    """Pick a cave from a list that has fewer than 3 tunnels."""
    if rng_seed is not None:
        random.seed(rng_seed)
    candidates = [c for c in cave_list if len(caves.get(c, [])) < 3]
    return random.choice(candidates) if candidates else cave_list[0]


if __name__ == '__main__':
    caves_dict: Dict[int, List[int]] = {1: [], 2: [], 3: []}
    create_tunnel(caves_dict, 1, 2)
    create_tunnel(caves_dict, 2, 3)
    print("Cave graph:", caves_dict)
