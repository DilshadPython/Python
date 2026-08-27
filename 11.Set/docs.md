# Technical Documentation: Python Sets (`11.Set`)

## 1. Overview & Data Structure Architecture
A **set** in Python is an unordered, mutable collection of unique, hashable elements. Sets are implemented internally as dynamic open-address hash tables ($O(1)$ average time complexity for membership testing `in`, element insertion `add`, and removal `remove`/`discard`).

### Primary Set Operations & Algebraic Notation
| Method | Operator | Algebraic Name | Mathematical Description |
| :--- | :--- | :--- | :--- |
| `set.union(*others)` | `\|` | Union | $A \cup B$: Elements in $A$, $B$, or both |
| `set.intersection(*others)` | `&` | Intersection | $A \cap B$: Elements in both $A$ and $B$ |
| `set.difference(*others)` | `-` | Difference | $A \setminus B$: Elements in $A$ but not $B$ |
| `set.symmetric_difference(other)` | `^` | Symmetric Difference | $A \Delta B$: Elements in $A$ or $B$, but not both |
| `set.issubset(other)` | `<=` | Subset | $A \subseteq B$: True if all elements of $A$ are in $B$ |
| `set.issuperset(other)` | `>=` | Superset | $A \supseteq B$: True if $A$ contains all elements of $B$ |

---

## 2. Python Version Evolution (Python 3.3 – Python 3.13 & Python 2.7 Comparison)

### A. Evolution across Python 3.3 to Python 3.13
1. **Python 3.3 Hash Randomization (PEP 456)**:
   - Python 3.3 introduced randomized secret seed hashing to mitigate Denial-of-Service attacks targeting hash collision algorithm complexities ($O(N^2)$ degradation). As a result, set iteration order is non-deterministic across different Python interpreter invocations.
2. **Python 3.7+ CPython Hash Table Refactoring**:
   - Compaction of set header sizes reduced memory overhead per set instance by up to 20%.
3. **Python 3.9 Pattern Matching & Set Operators**:
   - Standardized set operators (`|`, `&`, `-`, `^`) across set and dictionary view objects (`dict.keys()`, `dict.items()`).

### B. Python 2.7 Legacy Comparison
- **Set Literals Syntax**:
  - Python 2.7 introduced set literals `{1, 2, 3}` backported from Python 3.0. However, instantiating an empty set still requires `set()`, as `{}` unambiguously creates an empty `dict`.
- **Set Comparisons with Non-Set Types**:
  - In Python 2.7, operator expressions like `set1 == list1` evaluated to `False`. In Python 3.x, standard set method arguments (e.g. `set1.union([1, 2])`) accept any iterable, whereas bitwise operator overloads (`set1 | [1, 2]`) strictly require set operands (`TypeError`).

---

## 3. Discard vs. Remove Behavior
- `set.remove(x)`: Removes item `x` from set; raises `KeyError` if item is missing.
- `set.discard(x)`: Removes item `x` if present; silently does nothing if item is missing (ideal for safe idempotent removal).
