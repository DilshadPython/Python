# 🔷 NumPy Mastery: Vectorized Computing & Memory Architecture Guide

> **Module Scope:** N-Dimensional Arrays, SIMD Vectorization, Stride Manipulation, Memory Layouts, and BLAS/LAPACK Linear Algebra.

---

## 📌 Table of Contents
1. [Core Mental Model: What Makes NumPy Fast?](#1-core-mental-model-what-makes-numpy-fast)
2. [Array Memory Layout: Contiguity, Strides & Dtypes](#2-array-memory-layout-contiguity-strides--dtypes)
3. [Views vs Copies: The Most Critical Pitfall in NumPy](#3-views-vs-copies-the-most-critical-pitfall-in-numpy)
4. [The Broadcasting Rules (Dimensional Alignment)](#4-the-broadcasting-rules-dimensional-alignment)
5. [Universal Functions (Ufuncs) & In-Place Execution](#5-universal-functions-ufuncs--in-place-execution)
6. [Linear Algebra & High-Performance Operations](#6-linear-algebra--high-performance-operations)
7. [Persistence & Binary File I/O](#7-persistence--binary-file-io)
8. [Benchmarks: Python Lists vs NumPy Arrays](#8-benchmarks-python-lists-vs-numpy-arrays)
9. [Common Developer Pitfalls & Anti-Patterns](#9-common-developer-pitfalls--anti-patterns)
10. [NumPy Quick-Reference Cheat Sheet](#10-numpy-quick-reference-cheat-sheet)

---

## 1. Core Mental Model: What Makes NumPy Fast?

Standard Python lists store **pointers** to discrete heap-allocated PyObject instances scattered throughout memory. Every arithmetic operation requires pointer dereferencing, type inspection, and dynamic dispatch overhead:

```
Python List of Integers (Scattered Heap Pointers):
[Ptr 0] ---> PyObject (28 bytes) at 0x7fa1...
[Ptr 1] ---> PyObject (28 bytes) at 0x7fa9...
[Ptr 2] ---> PyObject (28 bytes) at 0x7fb3...

NumPy ndarray (Dense, Contiguous C-Memory Block):
[ 8 bytes ][ 8 bytes ][ 8 bytes ][ 8 bytes ]... (SIMD Vectorized in L1/L2 CPU Cache)
```

### Why NumPy is 10x to 100x Faster:
1. **Contiguous Memory Buffers**: Elements sit sequentially in physical RAM, maximizing CPU L1/L2 cache line hits.
2. **Homogeneous Data Types**: Every element has the exact same fixed byte width (e.g. `int64` = 8 bytes), eliminating Python runtime type checks.
3. **SIMD Vectorization**: Single Instruction, Multiple Data instructions execute arithmetic on 4, 8, or 16 numbers in a single CPU clock cycle via AVX2 / AVX-512.
4. **BLAS / LAPACK Integration**: Low-level linear algebra links directly to multi-threaded Fortran/C libraries (OpenBLAS, Intel MKL).

---

## 2. Array Memory Layout: Contiguity, Strides & Dtypes

Every `np.ndarray` consists of a header pointing to a raw data buffer, described by **shape**, **strides**, and **dtype**:

```python
import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.int64)

print("Shape:   ", arr.shape)    # (2, 3) -> 2 rows, 3 columns
print("Strides: ", arr.strides)  # (24, 8) -> 24 bytes to next row, 8 bytes to next col
print("Dtype:   ", arr.dtype)    # int64 (8 bytes per integer)
print("Itemsize:", arr.itemsize) # 8 bytes
print("Total RAM:", arr.nbytes)  # 48 bytes (2 * 3 * 8)
```

### C-Order (Row-Major) vs Fortran-Order (Column-Major)
* **C-contiguous (`order='C'`)**: Default in NumPy and Python. Traversing row-by-row (`axis=1`) is cache-efficient.
* **Fortran-contiguous (`order='F'`)**: Default in MATLAB and Fortran. Traversing column-by-column (`axis=0`) is cache-efficient.

---

## 3. Views vs Copies: The Most Critical Pitfall in NumPy

> [!WARNING]
> Basic slicing creates a **view** (shared memory window), NOT a copy. Modifying a slice mutates the original array!

```python
original = np.array([1, 2, 3, 4, 5])
slice_view = original[1:4]  # [2, 3, 4]

slice_view[0] = 999  # In-place mutation!
print(original)      # Output: [  1, 999,   3,   4,   5] -> ORIGINAL MUTATED!

# Check memory sharing:
print(np.shares_memory(original, slice_view))  # True
```

### When Does NumPy Copy?
* **Fancy Indexing** (indexing with lists or integer arrays): Returns a **Copy**.
* **Boolean Masking** (`arr[arr > 20]`): Returns a **Copy**.
* **Explicit Copy** (`arr.copy()`): Returns a **Copy**.

---

## 4. The Broadcasting Rules (Dimensional Alignment)

Broadcasting allows arithmetic operations between arrays of different shapes without allocating redundant memory copies.

### The Two Broadcasting Rules:
1. Two dimensions are compatible if **they are equal**, OR
2. One of the dimensions is **equal to 1**.

```python
# Matrix (3, 3) + Row Vector (3,)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])      # Shape: (3, 3)

vector = np.array([10, 20, 30])      # Shape: (3,) -> broadcasted to (1, 3) -> (3, 3)

result = matrix + vector
# [[11, 22, 33],
#  [14, 25, 36],
#  [17, 28, 39]]
```

---

## 5. Universal Functions (Ufuncs) & In-Place Execution

A **ufunc** is a vectorized wrapper around a compiled C function that applies element-wise operations with SIMD speed.

### Eliminating Memory Allocation via `out=`:
In high-throughput loops, allocating new arrays destroys memory performance. Use the `out` parameter:

```python
a = np.ones(10_000_000, dtype=np.float64)
b = np.ones(10_000_000, dtype=np.float64)
output_buffer = np.empty_like(a)

# Zero temporary allocation:
np.add(a, b, out=output_buffer)
```

---

## 6. Linear Algebra & High-Performance Operations

NumPy provides dedicated BLAS-accelerated routines under `np.linalg`:

```python
import numpy as np

# System of Linear Equations: Ax = b
# 2x + 1y = 8
# 1x + 3y = 13
A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([8.0, 13.0])

# 1. Determinant
det = np.linalg.det(A)  # 5.0

# 2. Matrix Inverse A⁻¹
inv_A = np.linalg.inv(A)

# 3. Direct BLAS Solver (Much faster and more numerically stable than inv(A) @ b)
x = np.linalg.solve(A, b)  # [2.0, 3.0]

# 4. Matrix Multiplication with PEP 465 @ Operator
product = A @ inv_A  # Returns Identity Matrix I
```

---

## 7. Persistence & Binary File I/O

| Format | Extension | Speed | Portability | Compression |
| :--- | :--- | :--- | :--- | :--- |
| **`np.save()`** | `.npy` | ⚡ Fastest (Raw C-buffer dump) | Python / NumPy only | Uncompressed |
| **`np.savez_compressed()`** | `.npz` | ⚡ Fast (Compressed archive) | Python / NumPy only | GZIP Compressed |
| **`np.savetxt()`** | `.csv` | 🐢 Slow (ASCII text format) | Universal (Excel, R, C++) | Uncompressed |

```python
from pathlib import Path

data = np.arange(100).reshape((10, 10))

# 1. Binary save (instant, preserves exact dtypes and shape)
np.save("matrix.npy", data)
loaded = np.load("matrix.npy")

# 2. Delimited text save
np.savetxt("matrix.csv", data, delimiter=",", fmt="%.2f")
```

---

## 8. Benchmarks: Python Lists vs NumPy Arrays

Execution benchmark summing 10,000,000 integers:

| Technique | Execution Time | RAM Consumption | Speedup |
| :--- | :--- | :--- | :--- |
| Standard Python `sum(range(N))` | `142.5 ms` | ~48 bytes (Generator) | $1.0\times$ (Baseline) |
| Python List `sum([i for i in range(N)])` | `380.2 ms` | **~80 MB** (Heap Pointers) | $0.4\times$ (Slow) |
| NumPy Vectorized `arr.sum()` | **`5.2 ms`** | **~8 MB** (Dense `int64`) | **$27.4\times$ Faster** |

---

## 9. Common Developer Pitfalls & Anti-Patterns

### ❌ Anti-Pattern 1: Writing `for` loops over NumPy arrays
```python
# BAD: Defeats the entire purpose of NumPy
for i in range(len(arr)):
    arr[i] = arr[i] * 2

# GOOD: Vectorized compiled SIMD
arr *= 2
```

### ❌ Anti-Pattern 2: Using `np.append()` inside a loop
`np.append()` creates a **complete copy** of the entire array on every iteration ($O(N^2)$ catastrophe).
```python
# BAD:
arr = np.array([])
for x in range(1000):
    arr = np.append(arr, x)

# GOOD: Allocate once, or collect in a list and convert once
arr = np.empty(1000, dtype=np.int64)
# OR:
arr = np.array([x for x in range(1000)])
```

---

## 10. NumPy Quick-Reference Cheat Sheet

```python
# Array Creation
np.zeros((3, 3))              # All 0.0 floats
np.ones((2, 4), dtype=int)     # All 1 integers
np.eye(5)                     # 5x5 Identity matrix
np.arange(0, 100, 5)          # Step-wise integer sequence
np.linspace(0, 1, 50)         # 50 linearly spaced floats

# Introspection & Shaping
arr.shape                     # Dimensions tuple (e.g. (3, 4))
arr.ndim                      # Number of dimensions (e.g. 2)
arr.size                      # Total element count
arr.reshape((4, 3))           # Reshape without copying data
arr.flatten()                 # 1D copy of the array
arr.T                         # Matrix transposition

# Reductions
arr.sum(axis=0)               # Sum along columns (collapses rows)
arr.mean(axis=1)              # Mean along rows (collapses columns)
arr.argmax()                  # Index of maximum element
```

---

## 11. 3D Tensors, Einstein Summation & Batch Processing

Modern deep learning architectures (Transformers, CNNs) represent data as 3D or 4D tensors:

```python
import numpy as np

# 1. 3D Tensor: Batch=4, SequenceLength=6, EmbeddingDim=8
np.random.seed(42)
tensor_3d = np.random.randn(4, 6, 8).astype(np.float32)

# 2. Axis Permutation (Batch-First -> Sequence-First)
seq_first = np.transpose(tensor_3d, (1, 0, 2))  # Shape: (6, 4, 8)

# 3. Scaled Dot-Product Attention Scores via Einstein Summation
# (B, S, D) x (B, M, D) -> (B, S, M)
Q, K = tensor_3d, tensor_3d
attn_scores = np.einsum("bsd,bmd->bsm", Q, K) / np.sqrt(8)

# 4. Spatial 3D Reduction (Mean Pooling across sequence dimension)
sentence_embeddings = tensor_3d.mean(axis=1)  # Shape: (4, 8)

# 5. Volumetric Slicing: Extract first token across all batches
cls_tokens = tensor_3d[:, 0, :]  # Shape: (4, 8)
```

