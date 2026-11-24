# 🔢 High-Performance NumPy Array Tutorial & Range Evolution Studio

Welcome to the **NumPy Array Tutorial & Range Evolution Studio**, a production-grade pedagogical curriculum designed to master scientific computing, N-dimensional array manipulation, vectorized operations, matrix linear algebra, and runtime performance analysis in Python.

---

## 📌 Table of Contents

1. [Overview & Project Architecture](#1-overview--project-architecture)
2. [3-Step Pedagogical Curriculum](#2-3-step-pedagogical-curriculum)
   - [Step 1: 01-Fundamentals](#step-1-01-fundamentals)
   - [Step 2: 02-Advanced-Math-and-Operators](#step-2-02-advanced-math-and-operators)
   - [Step 3: 03-Range-Evolution-and-Performance](#step-3-03-range-evolution-and-performance)
3. [Comprehensive NumPy ndarray Running Attributes & Methods](#3-comprehensive-numpy-ndarray-running-attributes--methods)
4. [Python 3.3 to Python 3.13 Evolution Matrix with NumPy](#4-python-33-to-python-313-evolution-matrix-with-numpy)
5. [Execution & Test Suite Instructions](#5-execution--test-suite-instructions)

---

## 1. Overview & Project Architecture

NumPy is the primary library for numerical computing in Python, offering contiguous C-level memory allocations (`np.ndarray`) and SIMD-vectorized operations that outperform standard Python loops by **10x–100x**.

### Workspace Layout

```
numpy_tutorial/
├── 01-Fundamentals/
│   ├── __init__.py
│   ├── array_creation_and_dtypes.py    # Basic ndarrays, ones, zeros, eye, empty
│   ├── array_shapes_and_dimensions.py # 1D/2D/3D shapes, ndim, reshape
│   └── test_fundamentals.py           # Unit tests for fundamentals
├── 02-Advanced-Math-and-Operators/
│   ├── __init__.py
│   ├── indexing_slicing_and_masking.py# Sub-arrays, row/col extraction, fancy indexing
│   ├── array_math_and_ufuncs.py        # Ufuncs, dot product, transposition, @ operator
│   ├── string_arrays_and_io.py        # Vectorized strings, binary/text I/O (.npy, .csv)
│   └── test_advanced_operations.py    # Unit tests for math & matrix ops
├── 03-Range-Evolution-and-Performance/
│   ├── __init__.py
│   ├── arange_vs_range.py             # range() vs np.arange() step comparisons
│   ├── range_performance_and_evolution.py # Memory footprint & speed benchmarks
│   ├── reflection_and_introspection.py  # dir(range) & dir(np.ndarray) attribute matrices
│   └── test_range_performance.py     # Unit tests for performance & reflection
├── numpy_tutorial_basics.py           # Executable master curriculum runner
├── test_numpy_master.py               # Master test runner (20 unit tests)
└── README.md                          # Project documentation
```

---

## 2. 3-Step Pedagogical Curriculum

### Step 1: 01-Fundamentals
- **Array Construction**: Using `np.array()`, `np.zeros()`, `np.ones()`, `np.eye()`, `np.empty()`.
- **Dimensional Inspection**: Analyzing `.ndim`, `.shape`, `.size`, `.dtype`, `.itemsize`, and `.nbytes`.
- **Reshaping**: Transforming 1D vectors into $M \times N$ matrices and 3D tensors.

### Step 2: 02-Advanced-Math-and-Operators
- **Indexing & Slicing**: 2D row/column extraction (`matrix[:, 2]`, `matrix[0, :]`), fancy indexing, and boolean masking (`arr[arr > mean]`).
- **Universal Functions (ufuncs)**: Element-wise `np.sqrt()`, `np.exp()`, `np.add()`, `np.maximum()`, `np.minimum()`.
- **Matrix Operations**: Transposition (`.T`), dot product (`np.dot`), and matrix multiplication operator (`@`).
- **Persistence**: File persistence via binary `.npy` (`np.save`, `np.load`) and delimited text `.csv` (`np.savetxt`, `np.loadtxt`).

### Step 3: 03-Range-Evolution-and-Performance
- **`np.arange()` vs `range()`**: Comparing parameter boundaries and floating-point step support (`np.arange(0.0, 2.0, 0.25)`).
- **Memory Benchmarks**: $O(1)$ RAM footprint for Python `range()` (~48 bytes) vs $O(N)$ contiguous buffer array memory for `np.ndarray`.
- **Runtime Introspection**: Using `dir(range)` and `dir(np.ndarray)` to introspect reflection attributes.

---

## 3. Comprehensive NumPy ndarray Running Attributes & Methods

Below is a complete matrix of running attributes and methods available on NumPy `ndarray` objects, contrasted with built-in Python `range()`:

### Introspection Matrix

| Attribute / Method | Category | Description | `range` | `np.ndarray` | Code Example |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `.start` / `.stop` / `.step` | Sequence | Boundary accessors | ✅ | ❌ | `r.start, r.stop, r.step` |
| `.count(x)` / `.index(x)` | Sequence | Value lookup and frequency | ✅ | ❌ | `r.count(5), r.index(10)` |
| `.ndim` | Structural | Number of array dimensions | ❌ | ✅ | `arr.ndim` (e.g. 2) |
| `.shape` | Structural | Dimensions tuple | ❌ | ✅ | `arr.shape` (e.g. `(3, 4)`) |
| `.size` | Structural | Total element count | ❌ | ✅ | `arr.size` (e.g. 12) |
| `.dtype` | Memory | Data type of array elements | ❌ | ✅ | `arr.dtype` (e.g. `int64`) |
| `.itemsize` | Memory | Length of one element in bytes | ❌ | ✅ | `arr.itemsize` (e.g. 8) |
| `.nbytes` | Memory | Total bytes consumed | ❌ | ✅ | `arr.nbytes` (e.g. 96) |
| `.T` | Linear Alg | Transposed array matrix view | ❌ | ✅ | `arr.T` |
| `.real` / `.imag` | Mathematical | Real and imaginary components | ❌ | ✅ | `arr.real, arr.imag` |
| `.reshape(shape)` | Transform | Returns array with new shape | ❌ | ✅ | `arr.reshape((2, 6))` |
| `.flatten()` | Transform | Returns 1D copy of array | ❌ | ✅ | `arr.flatten()` |
| `.ravel()` | Transform | Returns 1D flattened view | ❌ | ✅ | `arr.ravel()` |
| `.astype(dtype)` | Transform | Returns copy cast to dtype | ❌ | ✅ | `arr.astype(np.float64)` |
| `.copy()` | Transform | Creates explicit array copy | ❌ | ✅ | `arr.copy()` |
| `.tolist()` | Export | Converts array to Python list | ❌ | ✅ | `arr.tolist()` |
| `.sum()` / `.mean()` | Statistics | Sum and arithmetic mean | ❌ | ✅ | `arr.sum(), arr.mean()` |
| `.std()` / `.var()` | Statistics | Standard deviation & variance | ❌ | ✅ | `arr.std(), arr.var()` |
| `.min()` / `.max()` | Statistics | Minimum and maximum value | ❌ | ✅ | `arr.min(), arr.max()` |
| `.argmin()` / `.argmax()` | Statistics | Index of min and max value | ❌ | ✅ | `arr.argmin(), arr.argmax()` |
| `.clip(min, max)` | Manipulation | Limits values within range | ❌ | ✅ | `arr.clip(10, 50)` |
| `.repeat(repeats)` | Manipulation | Repeats elements of array | ❌ | ✅ | `arr.repeat(2, axis=0)` |

### Python Code Demonstration of Running Attributes & Methods

```python
import numpy as np

# Allocate a sample 2D NumPy array
arr = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.int32)

# --- 1. Running Attributes ---
print("ndim:    ", arr.ndim)       # 2
print("shape:   ", arr.shape)      # (2, 3)
print("size:    ", arr.size)       # 6
print("dtype:   ", arr.dtype)      # int32
print("itemsize:", arr.itemsize)   # 4 bytes
print("nbytes:  ", arr.nbytes)     # 24 bytes
print("T (transposed):\n", arr.T)  # Shape (3, 2)

# --- 2. Running Transformation Methods ---
reshaped = arr.reshape((3, 2))     # Shape (3, 2)
flattened = arr.flatten()          # 1D copy: [10, 20, 30, 40, 50, 60]
floated = arr.astype(np.float64)   # Float64 array copy
py_list = arr.tolist()             # [[10, 20, 30], [40, 50, 60]]

# --- 3. Running Statistical & Search Methods ---
print("Sum:    ", arr.sum())       # 210
print("Mean:   ", arr.mean())      # 35.0
print("Std:    ", arr.std())       # 17.078
print("Max:    ", arr.max(), "at index", arr.argmax()) # 60 at index 5
print("Min:    ", arr.min(), "at index", arr.argmin()) # 10 at index 0

# --- 4. Running Manipulation Methods ---
clipped = arr.clip(min=15, max=45) # Values clamped between 15 and 45
repeated = arr.repeat(2, axis=0)   # Repeated rows: shape (4, 3)
```

---

## 4. Python 3.3 to Python 3.13 Evolution Matrix with NumPy

Below is the complete version-by-version breakdown of Python enhancements from **Python 3.3 to Python 3.13**, detailing their interaction with NumPy scientific computing:

| Python Version | Core Feature Updates & Behavioral Evolution | NumPy Integration & Code Demonstration |
| :--- | :--- | :--- |
| **Python 3.3** | `range` sequence slicing ($O(1)$ lazy ranges); `yield from` generator delegation syntax. | ```python<br>r = range(100)[::2] # O(1) range slice<br>arr = np.fromiter(r, dtype=int)<br>``` |
| **Python 3.4** | `enum` module; `pathlib.Path` standard library integration for file system operations. | ```python<br>from pathlib import Path<br>np.save(Path('arr.npy'), np.array([1, 2]))<br>``` |
| **Python 3.5** | **PEP 465**: Dedicated matrix multiplication operator (`@`) for `ndarray.__matmul__`. | ```python<br>A = np.array([[1, 2], [3, 4]])<br>C = A.T @ A  # Clean matrix dot product<br>``` |
| **Python 3.6** | Formatted string literals (f-strings) for concise string interpolation and logging. | ```python<br>mat = np.eye(3)<br>print(f"Matrix shape: {mat.shape}, sum: {mat.sum()}")<br>``` |
| **Python 3.7** | Dataclasses (`@dataclass`); CPython bytecode optimizations for vector dispatching. | ```python<br>from dataclasses import dataclass<br>@dataclass<br>class Tensor:<br>    data: np.ndarray<br>``` |
| **Python 3.8** | **PEP 570**: Positional-only parameter syntax (`/`); **PEP 572**: Walrus operator (`:=`). | ```python<br>arr = np.array([10, 20, 30])<br>if (m := arr.mean()) > 15:<br>    filtered = arr[arr > m]<br>``` |
| **Python 3.9** | Dictionary union operators (`\|` & `\|=`); built-in generics type hints (`list[int]`). | ```python<br>meta = {"ndim": 2} \| {"shape": (3, 4)}<br>def get_arr() -> np.ndarray: ...<br>``` |
| **Python 3.10** | **PEP 634**: Structural Pattern Matching (`match / case`) over shapes & dimensions. | ```python<br>match arr.shape:<br>    case (N,): print("1D Vector of size", N)<br>    case (M, N): print(f"2D Matrix {M}x{N}")<br>``` |
| **Python 3.11** | **PEP 659**: Specializing Adaptive Interpreter accelerates CPython loop dispatching by **10–25%**. | ```python<br># Faster loop dispatching over NumPy arrays<br>for item in np.arange(1_000): ...<br>``` |
| **Python 3.12** | Per-interpreter GIL; fine-grained error location indicators in tracebacks. | ```python<br># Tracebacks point directly to failing matrix slice:<br># arr[row_idx, col_idx]<br>``` |
| **Python 3.13** | **PEP 703**: Free-threaded CPython (GIL removal) and Tier 2 JIT compilation engine. | ```python<br># Multi-threaded parallel execution of NumPy<br># operations without GIL lock bottlenecks.<br>``` |

---

## 5. Execution & Test Suite Instructions

### Running the Standalone Master Curriculum
To execute the interactive 3-step curriculum demonstration:
```bash
python3 numpy_tutorial_basics.py
```

### Running the Master Unit Test Suite
To execute all 20 unit tests across all curriculum modules:
```bash
python3 test_numpy_master.py
```