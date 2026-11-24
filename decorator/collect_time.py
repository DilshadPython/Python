"""Timestamp logging decorator with local time inspection.

Demonstrates logging entry and exit timestamps for function execution.
"""

import functools
import time
from typing import Any, Callable


def collect_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that logs the start and completion timestamps of a call."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Start time: {start_str}")
        result = func(*args, **kwargs)
        end_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"End time:   {end_str}")
        return result

    return wrapper


@collect_time
def sample_task(duration: float = 0.05) -> str:
    """Simulate a task requiring execution time."""
    time.sleep(duration)
    return "Task completed"


# Legacy function alias
@collect_time
def func() -> None:
    time.sleep(0.05)


if __name__ == "__main__":
    sample_task(0.1)
