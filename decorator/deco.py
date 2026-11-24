"""Manual timing baseline vs Decorator comparison.

Demonstrates how manual before/after timing code can be abstracted cleanly
into reusable decorators.
"""

import time


def go_to_work(walk_duration: float = 0.05) -> float:
    """Simulate manual time measurement around a function block."""
    start_walk = time.perf_counter()
    print("Walking...")
    time.sleep(walk_duration)
    end_walk = time.perf_counter()
    elapsed = end_walk - start_walk
    print(f"Walking took: {elapsed:.4f} seconds")
    return elapsed


if __name__ == "__main__":
    go_to_work()
