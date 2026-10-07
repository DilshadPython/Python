"""cloud_app/tutorials/python_performance_basics.py

Python Performance, Optimization & Algorithmic Efficiency Masterclass
=======================================================================
Comprehensive tutorial module demonstrating:
1. Big-O Notation & Time/Space Complexity Benchmarks
2. Memory Usage Profiling & __slots__ Optimization
3. Caching Strategies (@lru_cache, TTL Cache)
4. Database Indexing & N+1 Query Problem Solutions
5. Efficient Algorithms (Binary Search O(log N) vs Linear Search O(N))
6. Lazy Evaluation & Generator Memory Optimization
"""

from dataclasses import dataclass
import functools
import sys
import time
import tracemalloc
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple


# ==============================================================================
# 1. BIG-O COMPLEXITY & EFFICIENT ALGORITHMS
# ==============================================================================


def linear_search(data: List[int], target: int) -> Tuple[Optional[int], int]:
    """O(N) Time Complexity: Linear search scanning sequentially."""
    comparisons = 0
    for idx, item in enumerate(data):
        comparisons += 1
        if item == target:
            return idx, comparisons
    return None, comparisons


def binary_search(sorted_data: List[int], target: int) -> Tuple[Optional[int], int]:
    """O(log N) Time Complexity: Binary search dividing search space in half."""
    left, right = 0, len(sorted_data) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        mid_val = sorted_data[mid]

        if mid_val == target:
            return mid, comparisons
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return None, comparisons


def benchmark_search_algorithms(
    size: int = 100_000, target: int = 99_999
) -> Dict[str, Any]:
    """Benchmark O(N) vs O(log N) search performance and comparison counts."""
    data = list(range(size))

    # O(N) Linear Search
    t0 = time.perf_counter()
    linear_idx, linear_comps = linear_search(data, target)
    t1 = time.perf_counter()
    linear_time = (t1 - t0) * 1000  # ms

    # O(log N) Binary Search
    t2 = time.perf_counter()
    binary_idx, binary_comps = binary_search(data, target)
    t3 = time.perf_counter()
    binary_time = (t3 - t2) * 1000  # ms

    return {
        "dataset_size": size,
        "target": target,
        "linear_search": {
            "time_ms": round(linear_time, 4),
            "comparisons": linear_comps,
            "complexity": "O(N)",
        },
        "binary_search": {
            "time_ms": round(binary_time, 4),
            "comparisons": binary_comps,
            "complexity": "O(log N)",
        },
        "speedup_factor": round(linear_time / max(binary_time, 1e-9), 2),
    }


# ==============================================================================
# 2. MEMORY USAGE & __slots__ OPTIMIZATION
# ==============================================================================


class StandardUser:
    """Standard Python class using default __dict__ for instance attributes."""

    def __init__(self, user_id: int, username: str, email: str) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email


class SlottedUser:
    """Memory-optimized Python class using __slots__ to eliminate __dict__ overhead."""

    __slots__ = ("user_id", "username", "email")

    def __init__(self, user_id: int, username: str, email: str) -> None:
        self.user_id = user_id
        self.username = username
        self.email = email


def compare_memory_usage(instance_count: int = 10_000) -> Dict[str, Any]:
    """Measure total heap memory allocated for standard vs __slots__ objects using tracemalloc."""
    # Measure Standard Instances
    tracemalloc.start()
    std_users = [
        StandardUser(i, f"user_{i}", f"user_{i}@teachcloud.dev")
        for i in range(instance_count)
    ]
    current_std, peak_std = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Measure Slotted Instances
    tracemalloc.start()
    slotted_users = [
        SlottedUser(i, f"user_{i}", f"user_{i}@teachcloud.dev")
        for i in range(instance_count)
    ]
    current_slotted, peak_slotted = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    std_kb = peak_std / 1024
    slotted_kb = peak_slotted / 1024
    savings_pct = (
        round(((std_kb - slotted_kb) / std_kb) * 100, 2) if std_kb > 0 else 0.0
    )

    return {
        "instance_count": instance_count,
        "standard_dict_memory_kb": round(std_kb, 2),
        "slotted_memory_kb": round(slotted_kb, 2),
        "memory_savings_percent": f"{savings_pct}%",
        "sample_slotted_user": f"User({slotted_users[0].username})",
    }


# ==============================================================================
# 3. CACHING STRATEGIES (@lru_cache & TTL CACHE)
# ==============================================================================


# A. Un-cached Fibonacci (Exponential O(2^N) Time Complexity)
def fibonacci_uncached(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_uncached(n - 1) + fibonacci_uncached(n - 2)


# B. LRU Cached Fibonacci (Linear O(N) Time Complexity)
@functools.lru_cache(maxsize=128)
def fibonacci_cached(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


# C. Custom Time-To-Live (TTL) Dictionary Cache
class TTLCache:
    """Time-To-Live Cache for expiring temporary data keys."""

    def __init__(self, ttl_seconds: float = 2.0) -> None:
        self.ttl_seconds = ttl_seconds
        self._store: Dict[str, Tuple[Any, float]] = {}

    def set(self, key: str, value: Any) -> None:
        expiry = time.time() + self.ttl_seconds
        self._store[key] = (value, expiry)

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
        val, expiry = self._store[key]
        if time.time() > expiry:
            del self._store[key]  # Expired
            return None
        return val


def benchmark_caching_performance(n: int = 32) -> Dict[str, Any]:
    """Compare execution time between uncached and LRU cached Fibonacci functions."""
    t0 = time.perf_counter()
    res_uncached = fibonacci_uncached(n)
    t1 = time.perf_counter()
    time_uncached_ms = (t1 - t0) * 1000

    t2 = time.perf_counter()
    res_cached = fibonacci_cached(n)
    t3 = time.perf_counter()
    time_cached_ms = (t3 - t2) * 1000

    cache_info = fibonacci_cached.cache_info()

    return {
        "n_term": n,
        "fibonacci_value": res_cached,
        "uncached_time_ms": round(time_uncached_ms, 4),
        "cached_time_ms": round(time_cached_ms, 4),
        "speedup_factor": round(time_uncached_ms / max(time_cached_ms, 1e-9), 2),
        "lru_cache_info": {
            "hits": cache_info.hits,
            "misses": cache_info.misses,
            "maxsize": cache_info.maxsize,
            "currsize": cache_info.currsize,
        },
    }


# ==============================================================================
# 4. DATABASE INDEXING & N+1 QUERY PROBLEM SOLUTIONS
# ==============================================================================


@dataclass
class Author:
    id: int
    name: str


@dataclass
class Book:
    id: int
    title: str
    author_id: int


class MockDatabase:
    """Mock database table simulating N+1 query penalty vs JOIN optimization."""

    def __init__(self) -> None:
        self.authors = {
            1: Author(1, "Guido van Rossum"),
            2: Author(2, "Martin Fowler"),
            3: Author(3, "Robert C. Martin"),
        }
        self.books = [
            Book(101, "Python Language Spec", 1),
            Book(102, "Refactoring 2nd Ed", 2),
            Book(103, "Clean Code", 3),
            Book(104, "Clean Architecture", 3),
            Book(105, "Patterns of Enterprise Arch", 2),
        ]
        self.query_log: List[str] = []

    def get_all_books(self) -> List[Book]:
        self.query_log.append("SELECT * FROM books;")
        return list(self.books)

    def get_author_by_id(self, author_id: int) -> Optional[Author]:
        self.query_log.append(f"SELECT * FROM authors WHERE id = {author_id};")
        return self.authors.get(author_id)

    def get_books_with_authors_joined(self) -> List[Dict[str, Any]]:
        """Eager Loading (JOIN): Fetches all books and authors in 1 single query."""
        self.query_log.append(
            "SELECT books.id, books.title, authors.name FROM books JOIN authors ON books.author_id = authors.id;"
        )
        results = []
        for book in self.books:
            author = self.authors.get(book.author_id)
            results.append(
                {
                    "book_title": book.title,
                    "author_name": author.name if author else "Unknown",
                }
            )
        return results


def demonstrate_n_plus_one_query_problem() -> Dict[str, Any]:
    """Compare N+1 queries anti-pattern vs 1 single optimized JOIN query."""
    db_n1 = MockDatabase()

    # N+1 Queries Problem
    books = db_n1.get_all_books()  # 1 Query
    n1_results = []
    for book in books:
        author = db_n1.get_author_by_id(book.author_id)  # N Queries
        n1_results.append(f"{book.title} by {author.name if author else 'Unknown'}")

    n1_query_count = len(db_n1.query_log)

    # Solution: Eager Loading JOIN Query
    db_joined = MockDatabase()
    joined_results = db_joined.get_books_with_authors_joined()  # 1 Query
    joined_query_count = len(db_joined.query_log)

    return {
        "book_count": len(books),
        "n_plus_one_queries": {
            "executed_queries_count": n1_query_count,
            "query_log_sample": db_n1.query_log,
        },
        "eager_join_solution": {
            "executed_queries_count": joined_query_count,
            "query_log_sample": db_joined.query_log,
        },
        "query_reduction": f"Reduced queries from {n1_query_count} to {joined_query_count}!",
    }


# ==============================================================================
# 5. LAZY EVALUATION & GENERATOR MEMORY OPTIMIZATION
# ==============================================================================


def eager_range_list(n: int) -> List[int]:
    """Eager Evaluation: Allocates full list of N items in memory at once."""
    return [i * 2 for i in range(n)]


def lazy_range_generator(n: int) -> Generator[int, None, None]:
    """Lazy Evaluation: Yields items one at a time on demand with O(1) memory space."""
    for i in range(n):
        yield i * 2


def benchmark_lazy_vs_eager(element_count: int = 500_000) -> Dict[str, Any]:
    """Compare memory consumption between eager list comprehension and lazy generator."""
    # Eager List
    tracemalloc.start()
    eager_list = eager_range_list(element_count)
    curr_eager, peak_eager = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Lazy Generator
    tracemalloc.start()
    gen = lazy_range_generator(element_count)
    curr_lazy, peak_lazy = tracemalloc.get_traced_memory()
    # Consume first 5 items from stream
    stream_sample = [next(gen) for _ in range(5)]
    tracemalloc.stop()

    eager_mb = round(peak_eager / (1024 * 1024), 2)
    lazy_mb = round(peak_lazy / (1024 * 1024), 4)

    return {
        "total_elements": element_count,
        "eager_list_memory_mb": eager_mb,
        "lazy_generator_memory_mb": lazy_mb,
        "stream_sample_first_5": stream_sample,
        "memory_saving_verdict": f"Generator saved {round(eager_mb - lazy_mb, 2)} MB of RAM!",
    }


# ==============================================================================
# DEMONSTRATION HELPER FUNCTIONS FOR INTERACTIVE STUDIO
# ==============================================================================


def demonstrate_all_performance_pillars() -> Dict[str, Any]:
    """Execute master summary benchmark across search, memory, caching, SQL, and generators."""
    return {
        "search_benchmark": benchmark_search_algorithms(50_000, 49_999),
        "slots_memory": compare_memory_usage(5_000),
        "caching": benchmark_caching_performance(30),
        "database_n1": demonstrate_n_plus_one_query_problem(),
        "lazy_generators": benchmark_lazy_vs_eager(100_000),
    }


if __name__ == "__main__":
    print("=== Python Performance & Optimization Masterclass ===")
    summary = demonstrate_all_performance_pillars()
    print("Search:", summary["search_benchmark"])
    print("Memory:", summary["slots_memory"])
    print("Caching:", summary["caching"])
    print("N+1 Queries:", summary["database_n1"])
    print("Generators:", summary["lazy_generators"])
