# 🔄 Python Reverse Sequence & Traversal Master Tutorial

Welcome to the **Python Reverse Sequence & Traversal Tutorial**. This curriculum provides a complete pedagogical walkthrough of Python sequence reversal mechanisms—ranging from built-in `reversed()`, extended slicing `[::-1]`, and in-place `.reverse()`, to custom class `__reversed__()` hooks, 2D matrix transformations, dictionary view reversing, $O(1)$ range sequence reversal, memory profiling, and CPython interpreter version evolution (Python 2.7 ➔ 3.3 ➔ 3.13).

---

## 📌 Project Architecture & Subfolder Hierarchy

```
reverse_sequence/
├── 01-Fundamentals/
│   ├── reverse_sequence_basics.py      # reversed() iterator, list.reverse() in-place mutation
│   ├── reverse_slicing_conversions.py  # Sequence slicing [::-1], type casting, TypeError handling
│   └── test_fundamentals.py            # Step 1 unit tests
├── 02-Advanced-Math-and-Operators/
│   ├── custom_reversible_class.py      # Custom __reversed__() hooks & sequence protocol fallback
│   ├── matrix_and_dict_reverse.py      # Dict views reversal (keys, values, items) & 2D grid matrix ops
│   └── test_advanced_reverse.py       # Step 2 unit tests
├── 03-Range-Evolution-and-Performance/
│   ├── range_reverse_evolution.py     # Negative step range(), sys.getsizeof memory benchmarks, dir()
│   └── test_range_evolution.py        # Step 3 unit tests
├── reverse_sequence_basics.py          # Master entrypoint running all curriculum steps
├── test_reverse_tutorial.py           # Master unittest suite executing all tests
└── README.md                          # Comprehensive technical documentation & run guide
```

---

## 🚀 How to Run the Code & Execute Tests

### 1. Running standard Python entrypoints:
```bash
# Run master entrypoint
python3 reverse_sequence/reverse_sequence_basics.py

# Run individual subfolder modules
python3 reverse_sequence/01-Fundamentals/reverse_sequence_basics.py
python3 reverse_sequence/02-Advanced-Math-and-Operators/custom_reversible_class.py
python3 reverse_sequence/03-Range-Evolution-and-Performance/range_reverse_evolution.py
```

### 2. Running Unit Tests:
```bash
# Run master test suite via pytest
pytest reverse_sequence/test_reverse_tutorial.py -v

# Run subfolder tests via unittest
python3 -m unittest discover -s reverse_sequence -p "test_*.py"
```

---

## 💡 Key Features & Concepts Covered

1. **Built-in `reversed(seq)` Iterator**: Traverses lists, tuples, strings, and ranges in $O(1)$ lazy memory without mutating the original sequence.
2. **In-place `.reverse()`**: Mutates list objects directly in place and returns `None`.
3. **Extended Slicing `[::-1]`**: Constructs a shallow copy of sequence elements in reverse order.
4. **Custom Reversible OOP Classes**: Implements `__reversed__()` dunder method for customized reverse traversal logic, or relies on `__len__()` + `__getitem__()` sequence fallback.
5. **Dictionary & View Reversing**: Reverses dictionary keys, values, and key-value items maintaining insertion order (Python 3.8+).
6. **2D Matrix Reversing**: Vertical row reversal (`matrix[::-1]`), horizontal column reversal (`[r[::-1] for r in matrix]`), and 180-degree rotation.
7. **$O(1)$ Memory Overhead**: Benchmarks lazy `reversed(range(1_000_000))` (48 bytes) vs $O(N)$ linear memory of materialized list slices (`list(range(1_000_000))[::-1]`).
8. **CPython Version Evolution (2.7 ➔ 3.3 ➔ 3.13)**: Documents `xrange` replacement, `range_iterator` specializations, `dict` view reversing, and Python 3.13 `FOR_ITER` adaptive bytecode optimizations.

---

## 📜 License & Compliance

All code adheres strictly to PEP 8 standards with modern type hints (`typing`) and comprehensive docstrings.
