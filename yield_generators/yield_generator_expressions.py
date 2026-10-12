"""
Demonstrates generator expressions versus list comprehensions in Python.
Highlights memory efficiency, lazy evaluation, and pipeline aggregation.
"""
# "import module" loads the sys standard library module for memory usage inspection.
import sys
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Generator, List, Tuple


def compare_memory_footprint(limit: int = 100000) -> Tuple[int, int]:
    """
    Compare in-memory sizes of a list comprehension vs a generator expression.
    
    Args:
        limit (int): Number of integers to generate.
        
    Returns:
        Tuple[int, int]: Tuple of (list_size_bytes, generator_size_bytes).
    """
    list_comp: List[int] = [x * 2 for x in range(limit)]
    gen_exp: Generator[int, None, None] = (x * 2 for x in range(limit))

    list_size: int = sys.getsizeof(list_comp)
    gen_size: int = sys.getsizeof(gen_exp)

    return list_size, gen_size


def filter_even_squares(limit: int = 20) -> Generator[int, None, None]:
    """
    Generator expression pipeline filtering even squares from range.
    
    Args:
        limit (int): Upper bound for range evaluation.
        
    Yields:
        int: Even square numbers.
    """
    return (x ** 2 for x in range(limit) if (x ** 2) % 2 == 0)


def aggregate_generator_sum(limit: int = 1000) -> int:
    """Compute sum of values using a generator expression without list allocation."""
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)


if __name__ == '__main__':
    list_bytes, gen_bytes = compare_memory_footprint(100000)
    print(f"List Comprehension Size: {list_bytes} bytes")
    print(f"Generator Expression Size: {gen_bytes} bytes")
    print(f"Generator is ~{list_bytes // gen_bytes}x more memory efficient for 100,000 items!")

    print("\nEven Squares:", list(filter_even_squares(10)))
    print("Aggregate Sum (3 or 5 multiples < 1000):", aggregate_generator_sum(1000))
