"""
Demonstrates fundamental Python generator functions using the 'yield' keyword.
Provides memory-efficient sequence generation and string pattern construction.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
# Generator[YieldType, SendType, ReturnType] specifies type signature for generator functions.
from typing import Generator, List


def generate_pattern(n: int = 5) -> Generator[str, None, None]:
    """
    Generate an ASCII string pattern using yield.
    
    Args:
        n (int): Number of pattern rows to generate.
        
    Yields:
        str: String containing repeated '#' characters corresponding to current iteration index.
    """
    if n < 0:
        raise ValueError("Pattern count 'n' must be non-negative.")
    for i in range(n):
        yield '#' * i


def generate_number_sequence(start: int = 0, stop: int = 10, step: int = 1) -> Generator[int, None, None]:
    """
    Generate an integer sequence lazily using yield.
    
    Args:
        start (int): Starting integer (inclusive).
        stop (int): Stopping integer bound (exclusive).
        step (int): Step increment.
        
    Yields:
        int: Next integer value in the sequence.
    """
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step
    else:
        raise ValueError("Step cannot be zero.")


def collect_generated_pattern(n: int = 5) -> List[str]:
    """Collect generated pattern strings into a list for output and testing."""
    return list(generate_pattern(n))


if __name__ == '__main__':
    print("=== Generator Pattern Output ===")
    for pattern in generate_pattern(5):
        print(repr(pattern))

    print("\n=== Lazy Number Sequence Output ===")
    for num in generate_number_sequence(1, 10, 2):
        print(num, end=' ')
    print()
