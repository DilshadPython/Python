# Pedagogical Reference: Python `range` Deep Dive & Version Evolution

This document provides an in-depth technical reference for Python's `range` sequence object, detailing its architecture, internal performance characteristics, method introspection via `dir()`, and behavioral changes across Python versions from 2.7 to 3.13.

---

## 1. Overview of Python `range`

In Python, `range` is an immutable sequence type that represents an arithmetic progression of integers. Unlike lists or tuples, a `range` object does not store every individual value in memory. Instead, it calculates sequence values dynamically on demand using its `start`, `stop`, and `step` parameters.

### Constructor Forms
```python
range(stop)               # Starts at 0, steps by 1, ends before 'stop'
range(start, stop)        # Starts at 'start', steps by 1, ends before 'stop'
range(start, stop, step)  # Starts at 'start', steps by 'step', ends before 'stop'
```

---

## 2. Python Version Evolution Matrix (2.7 to 3.13)

| Python Version | Change / Feature Introduced | Key Impact & Description |
| :--- | :--- | :--- |
| **Python 2.7** | `range()` vs `xrange()` | `range()` returned an eager `list` ($O(N)$ RAM). `xrange()` returned a specialized generator object for memory efficiency. |
| **Python 3.0** | `xrange()` Removal & Range Unification | `xrange()` was removed. `range()` became an immutable $O(1)$ sequence object replacing `xrange()`. |
| **Python 3.2** | $O(1)$ Containment Checking | `val in range(...)` was optimized from an $O(N)$ iterator scan to $O(1)$ constant-time step bounds math. |
| **Python 3.3** | `.index()`, `.count()`, & Equality | Range objects gained support for `.index()` and `.count()` sequence methods and value-based equality (`==`). |
| **Python 3.10**| Structural Pattern Matching | Range objects can be matched in `match ... case` sequence patterns. |
| **Python 3.13**| CPython Tier-2 / JIT & Fixed Overhead | Range objects maintain a fixed 48-byte footprint in CPython with optimized bytecode dispatch under PEP 659/703. |

---

## 3. Python 2.7 (`xrange`) vs Python 3 (`range`)

### Memory Footprint Comparison
In Python 2.7, constructing `range(1_000_000)` instantly allocated 1,000,000 integer pointers in memory (~8 MB).

```python
# Python 2.7 Behavior (Eager Allocation)
nums = range(1000000)  # Returns a list of 1,000,000 elements in memory

# Python 3 Behavior (Lazy Evaluation)
nums = range(1000000)  # Returns range(0, 1000000), consuming 48 bytes
```

### Comparative Code Example
```python
import sys

# Python 3 constant O(1) memory size
r = range(1_000_000)
print(type(r))             # <class 'range'>
print(sys.getsizeof(r))    # 48 bytes

# Converting to list demonstrates eager allocation cost
lst = list(r)
print(sys.getsizeof(lst))  # ~8,000,000 bytes
```

---

## 4. Performance & Documentation Notes

### A. $O(1)$ Memory Overhead
Because `range` instances store only three integer attributes (`start`, `stop`, `step`), the memory footprint is constant ($O(1)$):
$$\text{Memory Complexity} = O(1)$$
Whether the range spans 10 items or 10,000,000,000 items, the object size remains 48 bytes on standard 64-bit CPython builds.

### B. $O(1)$ Membership Testing (`in` Operator)
Prior to Python 3.2, checking `x in range(start, stop, step)` required iterating through elements sequentially ($O(N)$ time). In Python 3.2+, CPython performs arithmetic calculation:
1. Is `x >= start` (for positive step) or `x <= start` (for negative step)?
2. Is `x < stop` (for positive step) or `x > stop` (for negative step)?
3. Is `(x - start) % step == 0`?

If all three conditions are satisfied, `in` returns `True` in $O(1)$ constant time.

### C. Range Slicing
Slicing a `range` object produces another `range` object in $O(1)$ time:
```python
r = range(0, 100, 2)
sub_r = r[5:20:2]  # Returns range(10, 40, 4) in O(1) time
```

---

## 5. Attribute & Method Introspection (`dir(range)`)

Executing `dir(range)` reveals the public attributes and magic (dunder) methods supported by range objects:

### Public Attributes & Methods

| Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `start` | Attribute (`int`) | Starting boundary integer of range | `range(2, 10).start` $\rightarrow$ `2` |
| `stop` | Attribute (`int`) | Ending boundary integer (exclusive) | `range(2, 10).stop` $\rightarrow$ `10` |
| `step` | Attribute (`int`) | Increment or decrement step value | `range(2, 10, 2).step` $\rightarrow$ `2` |
| `index(value)` | Method | Returns zero-based index of `value` | `range(10, 50, 5).index(20)` $\rightarrow$ `2` |
| `count(value)` | Method | Returns `1` if `value` is present, `0` otherwise | `range(10).count(5)` $\rightarrow$ `1` |

### Key Dunder (`__*__`) Methods

- `__contains__(val)`: Implements $O(1)$ `val in range` containment test.
- `__getitem__(key)`: Supports indexing (`r[0]`) and slicing (`r[1:5]`) in $O(1)$ time.
- `__len__()`: Returns item count `len(r)` in $O(1)$ time without iterating.
- `__iter__()`: Returns an iterator object for loop execution.
- `__reversed__()`: Returns a reverse range iterator in $O(1)$ time (`reversed(r)`).
- `__eq__(other)`: Checks if two ranges produce identical integer sequences (e.g., `range(0) == range(2, 1, 3)` returns `True`).
- `__repr__()`: Returns formal string representation like `"range(0, 10, 2)"`.

---

## 6. Example Introspection Script Output

```python
rng = range(2, 20, 3)

print("Attributes:", rng.start, rng.stop, rng.step)  # 2 20 3
print("Length:", len(rng))                           # 6
print("Index of 11:", rng.index(11))                 # 3
print("Contains 14?:", 14 in rng)                    # True
print("Reversed:", list(reversed(rng)))              # [17, 14, 11, 8, 5, 2]
```
