# Python Reflection & Introspection Master Guide (`reflection`)

Welcome to the **Python Reflection & Introspection Master Guide**, a production-grade educational reference detailing object introspection (`dir`, `getattr`, `setattr`, `hasattr`), sequence reflection algorithms, runtime signature inspection (`inspect.signature`), dynamic class creation (`type()`), unit testing via `unittest`, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & Architectural Architecture](#-overview--architectural-architecture)
2. [Reflection vs Introspection Concepts](#-reflection-vs-introspection-concepts)
3. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
4. [Directory Structure & Module Overview](#-directory-structure--module-overview)
5. [How to Run the Code](#-how-to-run-the-code)
6. [Running Unit Tests](#-running-unit-tests)
7. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
8. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 📁 Overview & Architectural Architecture

- **Introspection**: The ability of a program to examine the type, attributes, and signature of an object at runtime (`dir()`, `type()`, `isinstance()`, `inspect.signature()`).
- **Reflection**: The ability of a program to modify its own structure and behavior at runtime (`getattr()`, `setattr()`, dynamic class generation via `type()`, subclass registry via `__subclasses__()`).

```text
[ Python Object ] --- Introspection (dir, inspect) ---> [ Attributes & Signatures ]
                  --- Reflection (setattr, type)   ---> [ Dynamic Object Mutation ]
```

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_reflection.py`](file:///home/monika/PycharmProjects/Devel/Python/reflection/beginner_reflection.py))
Focuses on sequence reflection (reversal) using recursion, extended step slicing (`[::-1]`), and built-in `reversed()`:
- **Recursive Reversal**: Base-case sequence decomposition.
- **Slicing Reversal**: `seq[::-1]`.
- **Reversed Iterator**: `list(reversed(seq))`.

```python
# Beginner Example: Recursive sequence reflection preserving type
def reflect_recursive(seq):
    if not seq:
        return seq
    return reflect_recursive(seq[1:]) + seq[0:1]
```

---

### 🚀 Intermediate Level ([`intermediate_reflection.py`](file:///home/monika/PycharmProjects/Devel/Python/reflection/intermediate_reflection.py))
Focuses on runtime object attribute introspection and dynamic property mutation:
- **Attribute Access**: `getattr(obj, name)`, `setattr(obj, name, val)`.
- **Existence Verification**: `hasattr(obj, name)`.
- **Signature Introspection**: `inspect.signature(func)`.

```python
# Intermediate Example: Dynamic attribute inspection and setting
if hasattr(user, "age"):
    setattr(user, "age", getattr(user, "age") + 1)
```

---

### 🔥 Senior Level ([`senior_reflection.py`](file:///home/monika/PycharmProjects/Devel/Python/reflection/senior_reflection.py))
Focuses on subclass reflection registries (`__subclasses__()`), dynamic class generation (`type()`), and runtime method decoration/interception:
- **Subclass Registry**: `BaseClass.__subclasses__()`.
- **Dynamic Class Creation**: `NewClass = type("NewClass", (BaseClass,), attributes_dict)`.
- **Method Interception**: Dynamic decoration preserving metadata using `functools.wraps`.

```python
# Senior Example: Dynamic class creation via type() metaclass call
DynamicService = type(
    "DynamicService",
    (BasePlugin,),
    {"version": "1.0.0", "run": lambda self: "Dynamic execution"},
)
```

---

## 📁 Directory Structure & Module Overview

```text
reflection/
├── README.md                   # Master documentation and multi-tier guide
├── test_reflection.py          # Multi-tier unit test suite
├── sequence_reflection.py      # Core ReflectionEngine class module
├── beginner_reflection.py      # Beginner tier (recursion, slicing, reversed)
├── intermediate_reflection.py  # Intermediate tier (getattr, setattr, hasattr, inspect)
├── senior_reflection.py        # Senior tier (__subclasses__, type(), decorators)
└── reflection.py               # Legacy sequence reflection script
```

| File Name | Developer Tier | Key Concepts & Functions |
| :--- | :--- | :--- |
| `beginner_reflection.py` | 🌱 Beginner | Recursive sequence reversal, slicing `[::-1]`, `reversed()` |
| `intermediate_reflection.py` | 🚀 Intermediate | `getattr()`, `setattr()`, `hasattr()`, `dir()`, `inspect.signature()` |
| `senior_reflection.py` | 🔥 Senior | `__subclasses__()`, dynamic `type()` class creation, function wrappers |
| `sequence_reflection.py` | All Tiers | `ReflectionEngine.reflect_sequence()`, `invoke_dynamically()` |
| `test_reflection.py` | All Tiers | `unittest` suite verifying reflection across all developer tiers |

---

## 🚀 How to Run the Code

```bash
# Run core reflection engine
python3 reflection/sequence_reflection.py

# Run beginner tier examples
python3 reflection/beginner_reflection.py

# Run intermediate tier examples
python3 reflection/intermediate_reflection.py

# Run senior tier examples
python3 reflection/senior_reflection.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_reflection.py

# Run with pytest from repository root
pytest reflection/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | Introspection & Reflection Evolution | Syntax & System Behavior | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | Built-in `getattr`/`setattr`/`dir` | Object attribute inspection; `inspect.getargspec()` for signatures. | `xrange()` used for sequence indices; old-style vs new-style classes. |
| **Python 3.3** | `inspect.signature()` introduced | Standardized Callable signature inspection protocol (PEP 362). | Replaced deprecated `inspect.getargspec()`. |
| **Python 3.6** | Ordered `__dict__` attributes | Attribute dictionary ordering preserved in introspection calls. | Attribute order was non-deterministic in Python 2.7. |
| **Python 3.8** | Positional-only parameters in `inspect` | `inspect.Signature` handles `/` positional-only parameter indicators. | Manual argument inspection required in legacy versions. |
| **Python 3.10**| Type union reflection (`types.UnionType`) | `X | Y` type hint reflection in object annotations. | `typing.Union[X, Y]` required in Python 3.5-3.9. |
| **Python 3.12**| Optimized attribute lookup speed | C-level optimizations for `getattr()` and `dir()` lookups. | Reduced overhead during dynamic method reflection. |
| **Python 3.13**| Free-threaded GIL-free reflection | Thread-safe concurrent introspection across multiple threads. | Thread locks previously guarded attribute dict lookups. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Iterating sequence elements or bounds checking uses `range()` objects:

```python
# Reflecting elements using index bounds from range()
data = ["A", "B", "C", "D"]
for i in range(len(data)):
    print(f"Index {i}: {data[i]}")
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects in RAM (~8 MB).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Evaluating sequence containment `500 in range(0, 1000, 5)` computes in constant-time arithmetic evaluation without allocating memory arrays.

### Attributes and Methods Inspection (`dir(range)`)

Inspecting `dir(range)` demonstrates object introspection in action:

```python
r = range(0, 10, 2)
print(r.start)  # Output: 0
print(r.stop)   # Output: 10
print(r.step)   # Output: 2

print(r.index(6))  # Output: 3
print(r.count(4))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Range sequence boundaries.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
