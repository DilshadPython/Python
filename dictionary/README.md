# Modernized Python Dictionary Guide (Python 3.3 – 3.13 & Python 2.7 Comparison)

> [!NOTE]
> **Module Scope**: This directory (`12.Dictionary`) contains 20 modernized Python scripts along with an automated unit test suite (`test_dict.py`). All scripts detail dictionary key-value mapping, ordering, value sorting algorithms, and update patterns across Python 3.3 through Python 3.13.

---

## 📌 Summary of Completed Work

1. **Python Code Modernization (3.3 – 3.13 & 2.7 Comparison)**:
   - Refactored all scripts to PEP 8 standards with modular function structures and testable return values.
   - Handled non-interactive input shimming (`try: input = raw_input except NameError: pass`).
   - Corrected spellings (`December`, `Swedish`, `Victoria`, `lambda`, `sort`).

2. **Automated Unit Test Suite ([test_dict.py](file:///home/monika/PycharmProjects/Devel/Python/12.Dictionary/test_dict.py))**:
   - Comprehensive test runner using `unittest` verifying all 20 scripts.
   - 100% test pass rate (19/19 test cases passing in 0.001s).

3. **Documentation ([docs.md](file:///home/monika/PycharmProjects/Devel/Python/12.Dictionary/docs.md))**:
   - Detailed technical breakdown of compact hash tables (PEP 468), PEP 584 dictionary union operators (`|`, `|=`), dynamic view objects (`dict_keys`, `dict_values`), and value sorting algorithms.

---

## 🏛️ Executive Summary & Architecture Overview

Python dictionaries implement key-value mappings powered by CPython compact hash tables.

### Quick Status Matrix
| Aspect | Python 2.7 Legacy | Python 3.3 – 3.13 Standard | Status in Workspace |
| :--- | :--- | :--- | :--- |
| **Ordering** | Unordered (requires `OrderedDict`) | Preserves insertion order (Py3.7+) | Native order preservation |
| **Views vs Lists** | `keys()` returns list | `keys()` returns dynamic view object | Py3 View objects used |
| **Union Operators** | Method `.update()` only | Union operators `\|` and `\|= ` (Py3.9+) | Documented Py3.9+ operators |
| **Test Suite Coverage** | Manual execution | Automated `unittest` runner | 100% Pass Rate (19/19) |

---

## 🎓 Dual Learning Perspective: Beginner vs. Senior Developer

### 🟢 For Beginners (New to Python)
- **Key-Value Pairs**: Retrieve values by key `dict[key]` or safely with default fallback `dict.get(key, default)`.
- **Modifying & Deleting**: Update entries via `dict[key] = val` or remove using `pop(key)` or `del dict[key]`.
- **Iterating**: Loop over key-value pairs cleanly using `for key, value in my_dict.items():`.

### 0 For Senior Developers & System Architects
- **Compact Hash Tables (Py3.6+)**: Memory footprint reduced by up to 25% by separating indices array from entries array (`indices: array of int`, `entries: array of (hash, key, value)`).
- **Sorting by Value**: Use `operator.itemgetter(1)` with `sorted(dict.items(), key=...)` for high-performance C-level value sorting.
- **View Objects**: `dict.keys()`, `values()`, and `items()` are dynamic views that update automatically as the underlying dictionary mutates.

---

## 🛠️ Complete Inventory of Modernized Scripts (20 Files)

1. **`__init__.py`**: Module initialization metadata.
2. **`build_dict.py`**: Manual key assignment and key/value list extraction.
3. **`copy_to_dic.py`**: Shallow dictionary copying using `.copy()`.
4. **`count_words.py`**: File token frequency counting and sorting using dictionaries.
5. **`dict_.py`**: Value sorting using `lambda` functions.
6. **`dict_1.py`**: Basic dictionary creation, item retrieval, and string indexing.
7. **`dict_list.py`**: Handling collections of structured dictionary records.
8. **`dict_num.py`**: In-place numeric arithmetic operations on dictionary values.
9. **`dict_num_1.py`**: Aggregations (`sum`, `max`) over dictionary numerical values.
10. **`dict_update.py`**: In-place updates via `.update()` and deletion via `del`.
11. **`dict_update_func.py`**: Chained dictionary updates and length evaluations.
12. **`dir_dic.py`**: Introspecting public dictionary methods via `dir()`.
13. **`empty_dict.py`**: Empty dictionary instantiation and dynamic item addition.
14. **`lib_dict.py`**: Dictionary class method introspection.
15. **`my_calender.py`**: Lookup techniques using `.get()` with custom defaults.
16. **`nested_dict.py`**: Navigating multi-level nested dictionaries.
17. **`read_dict.py`**: Key iteration vs `.items()` tuple pair iteration.
18. **`remove_from_dic.py`**: Value extraction and key deletion via `.pop()`.
19. **`remove_from_dict.py`**: Safe deletion using `.pop()` and `.popitem()`.
20. **`sort_dict_by_value.py`**: Value sorting comparison: `lambda` vs `operator.itemgetter`.

---

## 🧪 Unit Testing Framework & Execution (`test_dict.py`)

Run the test suite from the terminal:
```bash
python3 -m unittest discover -s ~/PycharmProjects/Devel/Python/12.Dictionary -p "test_*.py"
```

### Execution Result
```text
----------------------------------------------------------------------
Ran 19 tests in 0.001s

OK
```

---

## 🔬 Detailed Version Comparison: Python 3.3 vs. Python 3.13 & Python 2.7 Legacy Notes

### 📊 Python 3.3 vs. Python 3.13 Feature Matrix

| Feature / Operation | Python 3.3 Standard | Python 3.13 Standard | Code Context & Performance Impact |
| :--- | :--- | :--- | :--- |
| **Insertion Order Preservation** | Unordered dictionary key storage | **Guaranteed insertion ordering (PEP 468 / Py3.7+)** | Iteration order in `dict_list.py`, `read_dict.py` |
| **Dictionary Merge/Update Operators** | Requires `.update()` method | **Union operators `\|` and `\|= ` (PEP 584 / Py3.9+)** | `dict_update.py`, `dict_update_func.py` |
| **Memory Architecture** | Dense hash array per entry | **Compact hash table design** (20-25% RAM reduction in Py3.6+) | Large record collections in `dict_list.py` |
| **Structural Pattern Matching** | Not supported | Mapping pattern matching `match ... case {'key': val}` (Py3.10+) | Deep mapping lookups in `nested_dict.py` |
| **Views vs Lists** | `dict_keys`, `dict_values`, `dict_items` views | Optimized set operations on `dict_keys` / `dict_items` | `dir_dic.py`, `lib_dict.py`, `read_dict.py` |

---

### 🚨 Python 2.7 Legacy Notifications & Warnings

> [!WARNING]
> **1. Unordered Iteration in Legacy Python 2.7**
> - **Python 2.7**: Dictionary keys were stored in non-deterministic pseudo-random hash order. Iterating over keys or `.keys()` produced unpredictable sequences. `collections.OrderedDict` was required for order preservation.
> - **Python 3.3 – 3.13**: Python 3.7+ guarantees key iteration order matches item insertion order.
> - **Script Relevance**: `read_dict.py`, `dict_list.py`, `build_dict.py`.

> [!WARNING]
> **2. `dict.keys()`, `values()`, `items()` Return Types**
> - **Python 2.7**: `d.keys()`, `d.values()`, and `d.items()` allocated and returned full standard `list` objects. Modifying the dictionary after calling `keys()` did NOT update the returned list.
> - **Python 3.3 – 3.13**: Returns dynamic `dict_keys`, `dict_values`, and `dict_items` view objects reflecting mutations to the underlying dictionary in real time.
> - **Script Relevance**: `build_dict.py`, `dir_dic.py`, `read_dict.py`.

> [!WARNING]
> **3. `dict.has_key(key)` Deprecation**
> - **Python 2.7**: Supported `d.has_key('name')`.
> - **Python 3.3 – 3.13**: `has_key()` was completely removed. The `in` membership operator (`'name' in d`) is mandatory.
> - **Script Relevance**: `dict_1.py`, `dict_update.py`.

> [!NOTE]
> **4. Safe Key Lookup with Defaults (`.get()`)**
> - **Python 2.7 & Python 3.3 – 3.13**: Directly accessing a missing key `d['missing']` raises a `KeyError`. Using `d.get('missing', default_value)` provides a non-crashing safe lookup mechanism.
> - **Script Relevance**: `my_calender.py`, `count_words.py`.