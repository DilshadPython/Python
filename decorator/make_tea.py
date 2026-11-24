"""Beverage preparation timing decorator (Tea).

Demonstrates timing functions that return formatted future timestamps
using datetime and timedelta.
"""

import functools
import time
from datetime import datetime, timedelta
from typing import Any, Callable


def make_tea(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator timing the tea brewing process."""
    @functools.wraps(func)
    def mix_tea(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        ready = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Tea brew time: {elapsed:.4f} seconds.")
        return ready

    return mix_tea


@make_tea
def new_tea(type_tea: str = "Black Tea", time_needed: float = 0.05) -> str:
    """Brew a tea beverage."""
    print(f"Starting preparation of {type_tea}.")
    time.sleep(time_needed)
    ready_time = datetime.now() + timedelta(minutes=5)
    return f"{type_tea} ready by {ready_time.strftime('%H:%M:%S')} (infusing for 5 min)."


@make_tea
def match_tea(wait_time: float = 0.05) -> str:
    """Check tea brewing match."""
    time.sleep(wait_time)
    return "Tea steep match confirmed."


if __name__ == "__main__":
    result = new_tea("Earl Grey", 0.1)
    print(result)
    print("-" * 30)
    print(match_tea(0.1))
