"""
Two-Argument Sentinel Iterator & Callable Iterator Module.

This module demonstrates advanced iter() function signatures:
- Two-argument iter(callable, sentinel): Calling a callable until sentinel value is produced
- File reading using iter(f.readline, '') sentinel loops
- Stateful counter functions with sentinel boundaries
"""
# "from typing import List, Callable, Any" imports typing annotations.
from typing import List, Callable, Any


class CounterCallable:
    """
    A stateful callable object that returns incrementing integers.
    """

    def __init__(self, start: int = 0) -> None:
        self.count = start

    def __call__(self) -> int:
        val = self.count
        self.count += 1
        return val


def iterate_until_sentinel(callable_func: Callable[[], Any], sentinel_value: Any) -> List[Any]:
    """
    Iterate using two-argument iter(callable, sentinel).

    iter(callable, sentinel) continuously calls callable_func() until the return value equals
    sentinel_value, whereupon StopIteration is raised and iteration terminates cleanly.

    Args:
        callable_func (Callable[[], Any]): Function or callable object taking 0 arguments.
        sentinel_value (Any): Value that signals end of iteration.

    Returns:
        List[Any]: List of values produced before hitting the sentinel.
    """
    sentinel_iterator = iter(callable_func, sentinel_value)
    return list(sentinel_iterator)


def simulate_file_sentinel_reading(lines_data: List[str]) -> List[str]:
    """
    Simulate sentinel-based line reading (similar to iter(f.readline, '')).

    Args:
        lines_data (List[str]): List of line strings ending with an empty string sentinel.

    Returns:
        List[str]: List of read line strings excluding the empty sentinel.
    """
    data_copy = list(lines_data)

    def read_line() -> str:
        if not data_copy:
            return ""
        return data_copy.pop(0)

    # Call read_line until it returns '' (empty string sentinel)
    line_iterator = iter(read_line, "")
    return list(line_iterator)


if __name__ == "__main__":
    print("=== Step 2: Two-Argument Sentinel Iterators ===")
    counter = CounterCallable(start=1)
    values = iterate_until_sentinel(counter, sentinel_value=6)
    print(f"iter(counter, 6) output : {values}")

    simulated_stream = ["First Line\n", "Second Line\n", "Third Line\n", ""]
    read_lines = simulate_file_sentinel_reading(simulated_stream)
    print(f"Sentinel file read lines : {read_lines}")
