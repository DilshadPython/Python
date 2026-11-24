"""
Demonstrates advanced bidirectional generator communication using .send(), .throw(), and .close().
Highlights generator state machine transitions and runtime error handling inside generators.
"""
# "from module import name" imports type annotation symbols directly into local scope.
from typing import Generator, List, Optional


def running_accumulator(initial_total: float = 0.0) -> Generator[float, float, float]:
    """
    Advanced generator accumulating values sent via .send().
    
    Yields:
        float: Current running accumulator total.
        
    Returns:
        float: Final accumulated sum when generator is closed or finished.
    """
    total = initial_total
    while True:
        value = yield total
        if value is None:
            break
        total += value
    return total


def echo_with_error_handling() -> Generator[str, str, str]:
    """Generator catching thrown exceptions via .throw() and performing cleanup on .close()."""
    try:
        while True:
            received = yield "Ready"
            if received == "exit":
                break
    except ValueError as err:
        yield f"Caught error: {err}"
    finally:
        pass
    return "Closed"


if __name__ == '__main__':
    print("=== Running Accumulator Demonstration ===")
    acc = running_accumulator(10.0)
    # Prime the generator to reach first yield
    current = next(acc)
    print("Initial Yielded Total:", current)

    print("Sent 5.5 -> New Total:", acc.send(5.5))
    print("Sent 14.5 -> New Total:", acc.send(14.5))

    try:
        acc.send(None)  # Terminate accumulator loop
    except StopIteration as stop:
        print("Final Returned Accumulator Total:", stop.value)
