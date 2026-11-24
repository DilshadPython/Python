"""Execution timing decorator using time.perf_counter and functools.wraps.

This module demonstrates measuring function runtime using modern Python
decorator patterns with proper metadata preservation and return-value forwarding.
"""

import functools
import time
from typing import Any, Callable


def time_you_need(base_func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to measure and display elapsed execution time of a function.

    Preserves function docstrings and attributes via functools.wraps.
    """
    @functools.wraps(base_func)
    def enhance(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = base_func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[{base_func.__name__}] Execution took {elapsed:.4f} seconds")
        return result

    return enhance


@time_you_need
def walking_to_work(destination: str = "work", delay: float = 0.1) -> str:
    """Simulate walking to a work destination."""
    print(f"Walking to {destination}...")
    time.sleep(delay)
    return f"Arrived at {destination}"


@time_you_need
def walking_to_university(destination: str = "University", delay: float = 0.1) -> str:
    """Simulate walking to university."""
    print(f"Walking to {destination}...")
    time.sleep(delay)
    return f"Arrived at {destination}"


@time_you_need
def walking_home(destination: str = "home", delay: float = 0.1) -> str:
    """Simulate walking back home."""
    print(f"Walking to {destination}...")
    time.sleep(delay)
    return f"Arrived at {destination}"


# Backward compatibility alias
walking_to_works = walking_to_work


if __name__ == "__main__":
    walking_to_work("work")
    walking_to_university("University")
    walking_home("home")
