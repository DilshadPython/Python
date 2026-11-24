# 🔄 Python Iterator Master Module

Welcome to the definitive master tutorial module for **Python Iterators & Iterable Protocols**. This directory features a **3-step sequential curriculum**—guiding students step-by-step from fundamental `iter()` and `next()` calls and built-in container iterators, to custom classes (`__iter__` / `__next__`), two-argument sentinel iterators, and $O(1)$ memory range iterator performance benchmarks.

---

## 📁 Repository Directory Architecture

```
iterator/
├── 01-Iterator-Fundamentals/
│   ├── iterator_protocol_basics.py  # iter(), next(), StopIteration exception handling & defaults
│   ├── container_iterators.py       # list, tuple, dict, str, and file line (TextIOWrapper) iterators
│   └── test_fundamentals.py         # 6 Unit tests for iterator fundamentals & container views
├── 02-Custom-Iterators-and-Classes/
│   ├── custom_class_iterator.py     # Custom AlphabetIterator & BoundedFibonacciIterator classes
│   ├── infinite_and_sentinel_iter.py# Two-argument iter(callable, sentinel) & counter iterators
│   └── test_custom_iterators.py     # 4 Unit tests for custom iterator classes & sentinel calls
├── 03-Range-Iterators-and-Performance/
│   ├── range_iterator_performance.py# iter(range(n)), O(1) space benchmarks, dir(range) introspection
│   └── test_range_iterators.py      # 4 Unit tests for range iterators & reflection matrix
├── dictionary_iterator_demo.py      # Refactored PEP 8 dictionary view iterator demonstration
├── file_iterator_demo.py            # Refactored PEP 8 lazy file line streaming demonstration
├── directory_iterator_demo.py       # Refactored PEP 8 cross-platform directory scanner demo
├── range_sequence_demo.py           # Refactored PEP 8 range iterator sequence demonstration
├── tuple_iterator_demo.py           # Refactored PEP 8 tuple iterator demonstration
├── custom_class_demo.py             # Standardized PEP 8 custom class iterator demonstration
├── manual_next_demo.py              # Standardized PEP 8 manual next() calls demonstration
├── iter.py                          # Master demonstration entrypoint script
├── test_iterator_master.py          # Master unittest suite runner executing all 14 unit tests
├── grade.txt                        # Sample text file used for file stream iteration demonstrations
├── README.md                        # Pedagogical overview & quickstart instructions
└── docs.md                          # Technical documentation, iterator protocol hooks & version matrices
```

---

## 🚀 Quickstart & Execution Guide

### 1. Running the Master Demonstration Entrypoint
```bash
python3 iterator/iter.py
```

### 2. Running Individual Curriculum Steps
```bash
# Step 1: Iterator Fundamentals
python3 iterator/01-Iterator-Fundamentals/iterator_protocol_basics.py
python3 iterator/01-Iterator-Fundamentals/container_iterators.py

# Step 2: Custom Iterators & Classes
python3 iterator/02-Custom-Iterators-and-Classes/custom_class_iterator.py
python3 iterator/02-Custom-Iterators-and-Classes/infinite_and_sentinel_iter.py

# Step 3: Range Iterators & Performance
python3 iterator/03-Range-Iterators-and-Performance/range_iterator_performance.py
```

### 3. Running Unit Test Suites
```bash
# Run Master Test Suite via unittest
python3 iterator/test_iterator_master.py

# Run Master Test Suite via pytest
pytest iterator/
```

---

## 💡 Key Pedagogical Concepts Covered

1. **Iterables vs. Iterators**: An Iterable defines `__iter__()` returning an Iterator. An Iterator defines `__iter__()` (returning `self`) and `__next__()` (returning values or raising `StopIteration`).
2. **Safe Iteration (`next(iterator, default)`)**: Preventing unhandled `StopIteration` exceptions by providing default fallback values.
3. **Custom Iterator Protocol**: Implementing custom stateful iteration logic inside user-defined classes (`AlphabetIterator`, `BoundedFibonacciIterator`).
4. **Two-Argument `iter(callable, sentinel)`**: Continuously evaluating callable objects until a sentinel boundary is reached.
5. **Range Iterator Performance**: Benchmarking $O(1)$ memory consumption of C-level `range_iterator` objects vs $O(N)$ materialized list iterators.
6. **Cross-Version Evolution**: Detailed breakdown from Python 2.7 (legacy `next()`, `xrange`, `.iterkeys()`) through Python 3.3 (`yield from`), 3.5 (async iterators), 3.11 (adaptive interpreter), and 3.13 (free-threaded CPython and JIT).
