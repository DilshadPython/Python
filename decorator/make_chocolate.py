"""Beverage preparation timing decorator (Chocolate).

Demonstrates timing decorators that handle return values, datetime calculations,
and variable arguments.
"""

import functools
import time
from datetime import datetime, timedelta
from typing import Any, Callable


def make_chocolate(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator timing the chocolate preparation process."""
    @functools.wraps(func)
    def mix_chocolate(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        ready = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"Chocolate preparation time: {elapsed:.4f} seconds.")
        return ready

    return mix_chocolate


@make_chocolate
def new_chocolate(type_chocolate: str = "Hot Chocolate", time_needed: float = 0.05) -> str:
    """Prepare a chocolate beverage."""
    print(f"Starting preparation of {type_chocolate} at {datetime.now().strftime('%H:%M:%S')}.")
    time.sleep(time_needed)
    return f"{type_chocolate} is ready!"


@make_chocolate
def match_time(wait_time: float = 0.05) -> str:
    """Simulate a scheduled notification time for ready chocolate."""
    time.sleep(wait_time)
    ready_time = datetime.now() + timedelta(minutes=5)
    return f"Chocolate ready at approximately: {ready_time.strftime('%H:%M:%S')} (in 5 minutes)."


if __name__ == "__main__":
    status = new_chocolate("Hot Chocolate", 0.1)
    print(status)
    print("-" * 30)
    print(match_time(0.1))
