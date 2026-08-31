# 🧰 Python Built-in Functions & Reflection (`built_ins`) Pedagogical Module

Welcome to the **`built_ins` Built-in Functions & Reflection Module**. This module provides a complete 3-tier pedagogical architecture for mastering core built-in functions (`abs()`, `len()`, `sum()`, `min()`, `max()`, `all()`, `any()`), dynamic reflection using `dir()`, `getattr()`, and `hasattr()`, namespace introspection via `globals()` and `locals()`, Newton's Square Root method using `abs()` convergence loops, range-driven sequence iteration, $O(1)$ memory benchmarking, `dir(range)` runtime introspection, and historical version evolution notes from Python 2.7 to 3.13.

---

## 📂 Module Architecture

```
built_ins/
├── 01_fundamentals/
│   ├── builtin_functions_basics.py      # abs(), len(), sum(), min(), max(), all(), any(), docstrings
│   └── test_fundamentals.py             # Unittest suite for mathematical & iterable built-in functions
├── 02_advanced_reflection_and_namespaces/
│   ├── advanced_reflection_and_namespaces.py # dir() type inspection, getattr/hasattr, Newton's method
│   └── test_advanced.py                 # Unittest suite for reflection, namespaces, and Newton's solver
├── 03_range_evolution_and_performance/
│   ├── range_builtin_performance.py     # range() sequence iteration, O(1) memory benchmarking, dir(range) matrix
│   └── test_range_evolution.py         # Unittest suite for range sequence generator & reflection
├── test_builtins_master.py              # Master unittest runner executing all 3 sub-tier test suites
└── README.md                            # Module documentation & usage guide
```

---

## 🚀 Execution & Usage Guide

### 1. Basic Built-in Functions (`01_fundamentals`)

Run basic built-in numerical and iterable demonstrations:

```bash
python3 built_ins/01_fundamentals/builtin_functions_basics.py
```

### 2. Advanced Reflection & Newton's Method (`02_advanced_reflection_and_namespaces`)

Execute type reflection via `dir()` and Newton's method square root solver:

```bash
python3 built_ins/02_advanced_reflection_and_namespaces/advanced_reflection_and_namespaces.py
```

### 3. Built-in Range Performance & Benchmarks (`03_range_evolution_and_performance`)

Simulate range stepping sequence iteration loops and memory benchmarks:

```bash
python3 built_ins/03_range_evolution_and_performance/range_builtin_performance.py
```

---

## 🧪 Unit Test Execution

Run the master test runner from the root repository directory:

```bash
python3 built_ins/test_builtins_master.py
```

Or execute individual test suites:

```bash
python3 -m unittest discover -s built_ins/01_fundamentals -p "test_*.py"
python3 -m unittest discover -s built_ins/02_advanced_reflection_and_namespaces -p "test_*.py"
python3 -m unittest discover -s built_ins/03_range_evolution_and_performance -p "test_*.py"
```

---

## 📊 Summary of Pedagogical Features

| Sub-Tier | Primary Features Covered | Code File | Unit Test File |
| :--- | :--- | :--- | :--- |
| **01_fundamentals** | `abs()` complex numbers & floats, `len()`, `sum()`, `min()`, `max()`, `all()`, `any()`, `builtins` docstrings | [`builtin_functions_basics.py`](01_fundamentals/builtin_functions_basics.py) | [`test_fundamentals.py`](01_fundamentals/test_fundamentals.py) |
| **02_advanced** | `dir()` attribute filtering, `getattr()`, `hasattr()`, `globals()`, `locals()`, Newton's method | [`advanced_reflection_and_namespaces.py`](02_advanced_reflection_and_namespaces/advanced_reflection_and_namespaces.py) | [`test_advanced.py`](02_advanced_reflection_and_namespaces/test_advanced.py) |
| **03_range & evolution** | Built-in `range()` stepping sequence, $O(1)$ memory footprint, `dir(range)` matrix, Py 2.7 to 3.13 history | [`range_builtin_performance.py`](03_range_evolution_and_performance/range_builtin_performance.py) | [`test_range_evolution.py`](03_range_evolution_and_performance/test_range_evolution.py) |
