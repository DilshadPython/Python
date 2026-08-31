# Technical Documentation: Python Tuples (`10.Tuple`)

## 1. Overview & Data Structure Properties
A **tuple** in Python is an immutable, ordered sequence of heterogenous elements. Because tuples are immutable, Python optimizes their memory allocation and execution overhead compared to dynamic lists.

### Primary Differences Between Tuples and Lists:
| Property | List (`list`) | Tuple (`tuple`) |
| :--- | :--- | :--- |
| **Mutability** | Mutable (can modify elements in-place) | Immutable (cannot alter elements after creation) |
| **Methods** | 11 public methods (`append`, `pop`, `sort`, etc.) | 2 public methods (`count`, `index`) |
| **Syntax** | Square brackets `[1, 2, 3]` | Parentheses `(1, 2, 3)` or comma separation `1, 2, 3` |
| **Memory Allocation** | Dynamic over-allocation for growth | Fixed minimal struct allocation |
| **Hashability** | Unhashable (cannot be used as dict keys) | Hashable (if all contained items are hashable) |

---

## 2. Python Version Evolution (Python 3.3 – Python 3.13 & Python 2.7 Comparison)

### A. Evolution across Python 3.3 to Python 3.13
1. **Python 3.8+ Namedtuple Enhancements**:
   - `collections.namedtuple` added support for default parameters via the `defaults` argument.
2. **Python 3.10+ Pattern Matching (PEP 634)**:
   - Sequence pattern matching allows structural matching directly on tuples:
     ```python
     match point:
         case (0, 0): print("Origin")
         case (x, y): print(f"Point: {x}, {y}")
     ```
3. **Python 3.11 – 3.13 Memory Allocation**:
   - Constant tuple literals (e.g. `(1, 2, 3)`) are frozen directly into bytecode code objects (`co_consts`), eliminating runtime allocation overhead entirely.

### B. Python 2.7 Legacy Comparison
- **Tuple Parameter Unpacking in Function Defs**:
  - Python 2.7 allowed automatic tuple unpacking in function signatures: `def foo(a, (b, c)): ...`
  - Python 3 removed automatic tuple parameter unpacking (PEP 3113) to clean up function signatures. In Python 3, explicit unpacking inside the function body is required:
    ```python
    def foo(a, b_c):
        b, c = b_c
    ```

---

## 3. Single Element Syntax Rule
A single item enclosed in parentheses without a trailing comma `('a')` is evaluated as a string parenthesis expression, NOT a tuple. To instantiate a 1-element tuple, a trailing comma is **mandatory**: `('a',)` or `1,`.