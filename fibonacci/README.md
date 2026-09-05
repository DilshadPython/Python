# 🌀 Fibonacci Algorithms & Dynamic Programming (`fibonacci`) Pedagogical Module

Welcome to the **`fibonacci` Pedagogical Module**. This module provides a complete reference suite for mastering Fibonacci sequence algorithms, dynamic programming, explicit dictionary memoization, standard library LRU caching (`@functools.lru_cache`), lazy generator evaluation (`yield`), custom iterator classes, and classic interview algorithms like FizzBuzz.

---

## 📂 Module Architecture

```
fibonacci/
├── fibonacci_iterative.py     # Iterative generation ($O(N)$ time, $O(1)$ space)
├── fibonacci_recursive.py     # Naive recursive algorithm ($O(2^N)$ exponential time)
├── fibonacci_memoization.py   # Explicit dictionary memoization (Dynamic Programming)
├── fibonacci_lru_cache.py     # Built-in @functools.lru_cache memoization & cache_info()
├── fibonacci_generator.py     # Lazy evaluation generator using yield ($O(1)$ memory)
├── fibonacci_iterator.py      # Custom iterator class overloading __iter__ and __next__
├── fizzbuzz_algorithm.py      # Modular FizzBuzz algorithm implementation
├── test_fibonacci.py          # Unittest suite validating all 7 algorithm modules
├── requirements.txt           # Dependency specification (Standard library footprint)
└── README.md                  # Module documentation and usage guide
```

---

## 🌟 What is New in This Module Update

1. **Fixing Typos & Renaming Legacy Files**: Fixed misspelled filenames (`fibanacci_2.py`, `fizz_buz.py`) and consolidated duplicate scripts into 7 clean, descriptive modules.
2. **Standardized Python Naming**: All module filenames are valid Python identifiers enabling clean imports (`from fibonacci.fibonacci_iterative import ...`).
3. **Complexity Benchmarking**: Added execution timing and complexity analysis comparing naive $O(2^N)$ recursion against $O(N)$ dynamic programming memoization.
4. **PEP 8 Compliance & Type Annotations**: Modernized code with standard Pythonic conventions, complete type hints (`List`, `Tuple`, `Generator`, `Iterator`), docstrings, and `if __name__ == "__main__":` entry points.
5. **Comprehensive Unittest Suite**: Introduced `test_fibonacci.py` covering all Fibonacci implementations and FizzBuzz using Python's `unittest` framework.

---

## 📊 Algorithmic Complexity Comparison

| Algorithm Module | Function / Class | Time Complexity | Space Complexity | Best Used For |
| :--- | :--- | :--- | :--- | :--- |
| [fibonacci_iterative.py](file:///home/monika/PycharmProjects/Devel/Python/fibonacci/fibonacci_iterative.py) | `get_fibonacci_nth(n)` | $O(N)$ | $O(1)$ | Production single-value computation without cache memory |
| [fibonacci_recursive.py](file:///home/monika/PycharmProjects/Devel/Python/fibonacci/fibonacci_recursive.py) | `fibonacci_recursive(n)` | $O(2^N)$ | $O(N)$ | Teaching recursion tree call stacks & exponential slowdown |
| [fibonacci_memoization.py](file:///home/monika/PycharmProjects/Devel/Python/fibonacci/fibonacci_memoization.py) | `fibonacci_memoized(n)` | $O(N)$ | $O(N)$ | Explicit dynamic programming dictionary caching |
| [fibonacci_lru_cache.py](file:///home/monika/PycharmProjects/Devel/Python/fibonacci/fibonacci_lru_cache.py) | `fibonacci_lru(n)` | $O(N)$ | $O(N)$ | Idiomatic standard library `@lru_cache` memoization |
| [fibonacci_generator.py](file:///home/monika/PycharmProjects/Devel/Python/fibonacci/fibonacci_generator.py) | `fibonacci_generator(limit)` | $O(N)$ | $O(1)$ | Memory-efficient lazy evaluation of massive sequences |
| [fibonacci_iterator.py](file:///home/monika/PycharmProjects/Devel/Python/fibonacci/fibonacci_iterator.py) | `FibonacciIterator(limit)` | $O(N)$ | $O(1)$ | Object-oriented iterator protocol (`__iter__`, `__next__`) |

---

## 🔍 Modules, Attributes & Methods Reference

### 1. `fibonacci_iterative.py` — Iterative Sequence Generation

Computes Fibonacci numbers iteratively using variable swapping (`a, b = b, a + b`), maintaining constant $O(1)$ space complexity.

```python
from fibonacci.fibonacci_iterative import get_fibonacci_nth, generate_fibonacci_sequence

# Compute 10th term
fib_10 = get_fibonacci_nth(10)  # Returns 55

# Generate sequence of 6 terms
seq = generate_fibonacci_sequence(6)  # Returns [0, 1, 1, 2, 3, 5]
```

---

### 2. `fibonacci_recursive.py` — Naive Recursive Subproblem Growth

Illustrates top-down recursive branching. Re-computes identical subproblems exponentially, showing why naive recursion scales as $O(2^N)$.

```python
from fibonacci.fibonacci_recursive import fibonacci_recursive, benchmark_recursive_execution

result, elapsed = benchmark_recursive_execution(30)
print(f"F(30) = {result} calculated in {elapsed:.4f} seconds")
```

---

### 3. `fibonacci_memoization.py` — Explicit Dictionary Cache

Caches subproblem solutions in an explicit module-level dictionary (`_fib_cache`), converting $O(2^N)$ time to linear $O(N)$ time.

```python
from fibonacci.fibonacci_memoization import fibonacci_memoized, get_cache_size, clear_cache

val = fibonacci_memoized(100)  # Calculated instantly
print("Cached terms count:", get_cache_size())
```

---

### 4. `fibonacci_lru_cache.py` — Built-in `@functools.lru_cache`

Decorates functions with Python's built-in Least Recently Used cache wrapper.

#### Methods & Introspection

- **`func.cache_info()`**: Returns `CacheInfo(hits, misses, maxsize, currsize)`.
- **`func.cache_clear()`**: Flushes cached entries from memory.

```python
from fibonacci.fibonacci_lru_cache import fibonacci_lru

val = fibonacci_lru(200)
info = fibonacci_lru.cache_info()
print(f"Hits: {info.hits}, Misses: {info.misses}")
```

---

### 5. `fibonacci_generator.py` — Lazy Evaluation Generator

Uses `yield` to stream Fibonacci terms on demand with $O(1)$ memory consumption.

```python
from fibonacci.fibonacci_generator import fibonacci_generator

gen = fibonacci_generator(5)
print(next(gen))  # 0
print(next(gen))  # 1
```

---

### 6. `fibonacci_iterator.py` — Custom Class Iterator

Implements the Python iterator protocol by defining `__iter__` and `__next__`.

```python
from fibonacci.fibonacci_iterator import FibonacciIterator

fib_iter = FibonacciIterator(5)
for term in fib_iter:
    print(term)  # 0 1 1 2 3
```

---

### 7. `fizzbuzz_algorithm.py` — Modular FizzBuzz Algorithm

Provides clean functions for single item evaluation and sequence array generation.

```python
from fibonacci.fizzbuzz_algorithm import fizzbuzz_item, generate_fizzbuzz_sequence

print(fizzbuzz_item(15))  # 'FizzBuzz'
print(generate_fizzbuzz_sequence(5))  # ['1', '2', 'Fizz', '4', 'Buzz']
```

---

## 🚀 Execution & Testing Guide

### 1. Run Individual Demonstration Scripts

Execute any script directly using `python3`:

```bash
python3 fibonacci/fibonacci_iterative.py
python3 fibonacci/fibonacci_recursive.py
python3 fibonacci/fibonacci_memoization.py
python3 fibonacci/fibonacci_lru_cache.py
python3 fibonacci/fibonacci_generator.py
python3 fibonacci/fibonacci_iterator.py
python3 fibonacci/fizzbuzz_algorithm.py
```

### 2. Run the Unittest Suite

Execute the complete test suite:

```bash
python3 -m unittest fibonacci/test_fibonacci.py
```

Or using `pytest`:

```bash
pytest fibonacci/test_fibonacci.py
```
