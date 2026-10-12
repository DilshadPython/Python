"""
Intermediate Level Python Keywords Demonstration Module.

This module provides functional, generator, and scope keyword demonstrations designed for
intermediate developers (`with`, `as`, `yield`, `yield from`, `lambda`, `assert`, `nonlocal`, `global`, `pass`, `break`, `continue`, `raise`, `finally`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for exit code status.
# - `from pathlib import Path`: Object-oriented file handling in context managers.
# - `from typing import Generator, List, Callable`: PEP 484 type hint generics.
# =========================================================================
from pathlib import Path
import sys
from typing import Callable, Generator, List

# Global module counter variable for `global` keyword demonstration
GLOBAL_COUNTER: int = 0


def sub_generator(limit: int) -> Generator[int, None, None]:
    """Sub-generator yielding even numbers."""
    for i in range(limit):
        if i % 2 == 0:
            yield i


def demonstrate_generators(limit: int) -> Generator[int, None, None]:
    """Demonstrate generator keywords: `yield`, `yield from`.

    Args:
        limit (int): Upper bound integer for sequence generation.

    Yields:
        Generator[int, None, None]: Delegated sequence of even numbers.
    """
    # Delegate sequence generation to sub_generator via `yield from`
    yield from sub_generator(limit)


def demonstrate_scope_keywords() -> dict[str, int]:
    """Demonstrate scope modification keywords: `nonlocal`, `global`.

    Returns:
        dict[str, int]: Updated outer and global state counts.
    """
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 10

    outer_count = 5

    def inner_function() -> None:
        nonlocal outer_count
        outer_count += 15

    inner_function()

    return {
        "global_counter": GLOBAL_COUNTER,
        "outer_count": outer_count,
    }


def demonstrate_lambdas_and_assertions(numbers: List[int]) -> List[int]:
    """Demonstrate functional keywords: `lambda`, `assert`, `break`, `continue`, `pass`.

    Args:
        numbers (List[int]): Input integer list.

    Returns:
        List[int]: Transformed and filtered list.
    """
    assert len(numbers) > 0, "Input numbers list must not be empty"

    # Inline anonymous function using `lambda`
    square_func: Callable[[int], int] = lambda x: x * x

    processed: List[int] = []

    for num in numbers:
        if num < 0:
            continue  # Skip negative numbers
        elif num == 999:
            break  # Emergency break loop
        elif num == 0:
            pass  # Placeholder statement
        else:
            processed.append(square_func(num))

    return processed


def demonstrate_context_manager_and_finally(file_path: Path, content: str) -> str:
    """Demonstrate resource management keywords: `with`, `as`, `raise`, `finally`.

    Args:
        file_path (Path): File path to write and read.
        content (str): Content string.

    Returns:
        str: Content read from file.
    """
    read_text = ""
    try:
        # Resource management using `with` and `as`
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        with open(file_path, "r", encoding="utf-8") as f:
            read_text = f.read()

    finally:
        # `finally` block guaranteed execution cleanup
        if file_path.exists():
            file_path.unlink()

    return read_text


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate keywords demonstration."""
    print("=== Intermediate Level Python Keywords Demonstration ===")
    print("Generators (yield from):", list(demonstrate_generators(8)))
    print("Scope (nonlocal / global):", demonstrate_scope_keywords())
    print("Lambdas & Assertions:", demonstrate_lambdas_and_assertions([1, 2, 0, 3, -5, 4]))

    temp_file = Path("temp_demo.txt")
    print("Context Manager (with / finally):", demonstrate_context_manager_and_finally(temp_file, "Hello Intermediate!"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
