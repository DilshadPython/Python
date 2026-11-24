# Python Unpacking Operators Master Guide (`*`, `**`, `_`)

Welcome to the **Python Unpacking Master Guide**, a production-grade educational reference detailing sequence positional unpacking (`*`), mapping keyword unpacking (`**`), wildcard discard placeholders (`_`), unit testing via `unittest`, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & Unpacking Operators Architecture](#-overview--unpacking-operators-architecture)
2. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
3. [Directory Structure & Module Overview](#-directory-structure--module-overview)
4. [Positional (`*`) vs Keyword (`**`) Unpacking Rules](#-positional--vs-keyword--unpacking-rules)
5. [How to Run the Code](#-how-to-run-the-code)
6. [Running Unit Tests](#-running-unit-tests)
7. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
8. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 🎁 Overview & Unpacking Operators Architecture

Unpacking in Python refers to extracting individual elements from iterable containers (tuples, lists, sets, strings, generators) or mapping dictionaries directly into variables or function parameters.

```text
[ Sequence Container: [75, 40, 25] ]  --- * --->  Param 1: 75, Param 2: 40, Param 3: 25
[ Dictionary: {'l': 15, 'w': 10} ]    --- ** -->  Key length=15, Key width=10
```

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_unpacking.py`](file:///home/monika/PycharmProjects/Devel/Python/unpacking/beginner_unpacking.py))
Focuses on simple 1-to-1 tuple assignment, list unpacking, and discarding unwanted items using the underscore wildcard (`_`):
- **Tuple Assignment**: `first_name, last_name = "Dilshad Abdulla".split()`.
- **Wildcard Placeholder**: `first_name, _ = "Dilshad Abdulla".split()`.
- **Basic List Unpacking**: `a, b, c = [10, 20, 30]`.

```python
# Beginner Example: Tuple assignment and wildcard discard
first_name, last_name = full_name.split(" ", 1)
first_name, _ = full_name.split(" ", 1)
```

---

### 🚀 Intermediate Level ([`intermediate_unpacking.py`](file:///home/monika/PycharmProjects/Devel/Python/unpacking/intermediate_unpacking.py))
Focuses on Extended Iterable Unpacking (PEP 3132), variable argument function signatures (`*args`, `**kwargs`), and dictionary merging (`{**d1, **d2}`):
- **Extended Unpacking**: `head, *middle, tail = [1, 2, 3, 4, 5]`.
- **Function Delegation**: `def process(*args, **kwargs)`.
- **Dictionary Literal Unpacking**: `merged = {**defaults, **user_overrides}`.

```python
# Intermediate Example: Extended unpacking and dictionary merging
head, *middle, tail = numbers_list
merged_config = {**default_settings, **custom_settings}
```

---

### 🔥 Senior Level ([`senior_unpacking.py`](file:///home/monika/PycharmProjects/Devel/Python/unpacking/senior_unpacking.py))
Focuses on Structural Pattern Matching unpacking (`match/case`), TypedDict `Unpack` type hints (PEP 692 in Python 3.12+), and CPython AST unpacking inspection:
- **Structural Pattern Matching**: `case [first, *middle, last]:`.
- **TypedDict Kwargs Unpack**: `def func(**kwargs: Unpack[DimensionKwargs])`.
- **CPython AST Inspection**: Parsing `ast.Assign` and `ast.Starred` nodes.

```python
# Senior Example: Pattern matching sequence unpacking
match data:
    case [first, *middle, last]:
        print(f"Matched list: {first}, {middle}, {last}")
    case {"length": l, "width": w, "height": h}:
        print(f"Matched dict: {l}, {w}, {h}")
```

---

## 📁 Directory Structure & Module Overview

```text
unpacking/
├── README.md                 # Master documentation and multi-tier guide
├── test_unpacking.py         # Multi-tier unit test suite
├── sequence_unpacking.py     # Positional iterable unpacking (*)
├── dictionary_unpacking.py   # Mapping keyword unpacking (**)
├── beginner_unpacking.py     # Beginner tier (tuple assignment & wildcard _)
├── intermediate_unpacking.py # Intermediate tier (extended head/*middle/tail)
├── senior_unpacking.py       # Senior tier (match/case & TypedDict Unpack)
├── coins.py                  # Legacy wrapper script
├── coins_dict.py             # Legacy wrapper script
├── coins_error.py            # Legacy wrapper script
├── fixing_coins.py           # Legacy wrapper script
├── totals.py                 # Legacy wrapper script
└── unpack.py                 # Legacy wrapper script
```

| File Name | Developer Tier | Key Concepts & Functions |
| :--- | :--- | :--- |
| `beginner_unpacking.py` | 🌱 Beginner | Tuple assignment `a, b = pair`, wildcard placeholder `_` |
| `intermediate_unpacking.py` | 🚀 Intermediate | Extended unpacking `head, *middle, tail`, `{**d1, **d2}` |
| `senior_unpacking.py` | 🔥 Senior | Structural matching `match/case`, `Unpack[TypedDict]`, AST parsing |
| `sequence_unpacking.py` | All Tiers | Single asterisk `*` iterable expansion |
| `dictionary_unpacking.py` | All Tiers | Double asterisk `**` dictionary expansion |
| `test_unpacking.py` | All Tiers | `unittest` suite verifying unpacking functionality |

---

## ⚡ Positional (`*`) vs Keyword (`**`) Unpacking Rules

1. **Single Asterisk (`*`)**: Unpacks **Iterables** (lists, tuples, sets, strings, range objects, generators) into positional arguments or list elements.
   - Example: `func(*[10, 20, 30])` $\rightarrow$ `func(10, 20, 30)`
2. **Double Asterisk (`**`)**: Unpacks **Mappings** (dictionaries) into named keyword arguments.
   - Example: `func(**{"length": 15, "width": 10})` $\rightarrow$ `func(length=15, width=10)`
3. **Wildcard Placeholder (`_`)**: Replaces unused variable names during unpacking assignments to signal intent to linters and developers.

---

## 🚀 How to Run the Code

```bash
# Run sequence unpacking
python3 unpacking/sequence_unpacking.py

# Run dictionary unpacking
python3 unpacking/dictionary_unpacking.py

# Run beginner tier examples
python3 unpacking/beginner_unpacking.py

# Run intermediate tier examples
python3 unpacking/intermediate_unpacking.py

# Run senior tier examples
python3 unpacking/senior_unpacking.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_unpacking.py

# Run with pytest from repository root
pytest unpacking/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | Unpacking Language Feature | Syntax & Compiler Behavior | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | Basic 1-to-1 Unpacking | `a, b = (1, 2)` required exact length match. | `a, b, c = [1, 2]` raised `ValueError: too many values to unpack`. |
| **Python 3.0** | Extended Iterable Unpacking (PEP 3132) | `a, *b, c = range(5)` introduced star target assignment. | Mandatory loop appending or slicing `b = seq[1:-1]` in Python 2.7. |
| **Python 3.5** | Additional Unpacking Generalizations (PEP 448) | Allowed `[*a, *b]`, `func(*a, *b)`, `{**d1, **d2}` anywhere. | Python 2.7 restricted to a single `*args` and `**kwargs` at call site. |
| **Python 3.8** | Positional-only parameters (`/`) | Parameter unpacking enforced positional constraints. | Unpacking kwargs into `/` positional-only parameters raised `TypeError`. |
| **Python 3.9** | Dict Union Operator (`d1 \| d2`) | Dictionary merging syntax without unpacking `**`. | Unpacking `{**d1, **d2}` remained valid alongside `d1 \| d2`. |
| **Python 3.10**| Pattern Matching Sequence Unpacking (PEP 634) | `match seq: case [first, *rest]:` structural matching. | Extended `match` statement sequence unpacking capabilities. |
| **Python 3.11**| Exception Group Unpacking (`except*`) | Multi-exception group unpacking syntax. | Unpacking exceptions in asynchronous `TaskGroup` contexts. |
| **Python 3.12**| TypedDict `Unpack` Type Operator (PEP 692) | `def func(**kwargs: Unpack[TypedDict])` keyword validation. | Static type checkers validate dictionary unpacking structures. |
| **Python 3.13**| Free-threaded GIL-free CPython | High-throughput concurrent tuple/list unpacking. | Thread-safe sequence parameter unpacking without GIL lock contention. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Range sequence objects are frequently unpacked into lists or positional parameters:

```python
# Unpacking a range sequence into a list using *
range_list = [*range(0, 10, 2)]
print(range_list)  # Output: [0, 2, 4, 6, 8]
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects in RAM (~8 MB).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Evaluating sequence containment `500 in range(0, 1000, 5)` computes in constant-time arithmetic evaluation without allocating memory arrays.

### Attributes and Methods Inspection (`dir(range)`)

Inspecting `dir(range)` shows standard sequence methods:

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
