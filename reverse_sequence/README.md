# 🔄 Python Sequence Reversal Master Module

Welcome to the definitive master tutorial module for **Python Sequence & Range Reversal**. This directory features a **3-step sequential curriculum**—guiding students step-by-step from fundamental string and in-place list reversal, to custom `__reversed__()` dunder protocols, dictionary view reversal, and $O(1)$ memory range iterator benchmarks.

---

## 📁 Repository Directory Architecture

```
reverse/
├── 01-Sequence-Reversal-Basics/
│   ├── string_reversal.py         # Slice [::-1], reversed() iterator, join(), word/sentence reversal
│   ├── list_in_place_reversal.py  # In-place list.reverse() vs out-of-place list copy & side effects
│   └── test_reversal_basics.py    # 8 Unit tests for string & list reversal techniques
├── 02-Advanced-Reversal-Protocols/
│   ├── custom_reversed_protocol.py# Custom __reversed__() protocol hook & __len__/__getitem__ fallback
│   ├── iterator_reversal_helpers.py# Dict view reversal (Python 3.8+), deque reversal & tuple slicing
│   └── test_reversal_protocols.py # 6 Unit tests for custom protocol hooks & container views
├── 03-Range-Reversal-and-Performance/
│   ├── range_reversal_evolution.py# reversed(range(n)), negative step range(), memory benchmarks & dir(range)
│   └── test_range_reversal.py     # 5 Unit tests for range reversal & memory footprint
├── reverse_text.py                # Standardized PEP 8 master demonstration entrypoint
├── test_reverse_master.py         # Master unittest suite runner executing all 19 unit tests
├── README.md                      # Pedagogical overview & quickstart instructions
└── docs.md                        # Technical documentation, dunder protocol hooks & version matrices
```

---

## 🚀 Quickstart & Execution Guide

### 1. Running the Master Demonstration Entrypoint
```bash
python3 reverse/reverse_text.py
```

### 2. Running Individual Curriculum Steps
```bash
# Step 1: Sequence Reversal Basics
python3 reverse/01-Sequence-Reversal-Basics/string_reversal.py
python3 reverse/01-Sequence-Reversal-Basics/list_in_place_reversal.py

# Step 2: Advanced Reversal Protocols & Containers
python3 reverse/02-Advanced-Reversal-Protocols/custom_reversed_protocol.py
python3 reverse/02-Advanced-Reversal-Protocols/iterator_reversal_helpers.py

# Step 3: Range Reversal & Performance
python3 reverse/03-Range-Reversal-and-Performance/range_reversal_evolution.py
```

### 3. Running Unit Test Suites
```bash
# Run Master Test Suite via unittest
python3 reverse/test_reverse_master.py

# Run Master Test Suite via pytest
pytest reverse/
```

---

## 💡 Key Pedagogical Concepts Covered

1. **String Immutability & Reversal**: Understanding why strings cannot be modified in-place and comparing extended slicing `text[::-1]` against `reversed()` iterator joining.
2. **Command-Query Separation (`list.reverse()`)**: Explaining why `list.reverse()` mutates the list in-place and returns `None`, contrasting with `list[::-1]` and `reversed(list)`.
3. **`__reversed__()` Dunder Hook (PEP 322)**: Implementing custom reverse iteration protocol hooks on user-defined classes and utilizing `__len__()` + `__getitem__()` fallbacks.
4. **Dictionary View Reversal (Python 3.8+ PEP 584)**: Leveraging ordered dictionaries to reverse `keys()`, `values()`, and `items()` views.
5. **Range Iterator Memory Benchmark**: Demonstrating $O(1)$ space memory efficiency of `reversed(range(n))` vs $O(N)$ space materialized lists.
