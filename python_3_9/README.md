# Python 3.9 Overview & Features

**Release Date:** October 5, 2020  
**Key Focus:** Dictionary Union Operators (`|`), Built-in Type Hint Generics (`list[str]`), String Prefix/Suffix Stripping, Standard Timezone Support (`zoneinfo`), and New PEG Parser.

---

## 🚀 Key Features & Syntax Additions

### 1. Dictionary Union Operators `|` and `|=` (PEP 584)
Introduced new binary operators for merging dictionaries:
- `d1 | d2`: Returns a new dictionary containing key-value pairs from `d1` and `d2` (right-side values override left-side keys).
- `d1 |= d2`: In-place dictionary update operator.

### 2. Built-in Generic Types for Type Annotations (PEP 585)
Native collections like `list`, `dict`, `tuple`, `set`, `type` can now be used directly as type generics without importing capitalized variants from `typing` (`from typing import List, Dict` is no longer needed).
- Example: `def get_names() -> list[str]: ...`

### 3. Prefix and Suffix String Methods (PEP 616)
Added `str.removeprefix(prefix)` and `str.removesuffix(suffix)` to conveniently remove a prefix or suffix from a string if present, replacing fragile slicing or `.startswith()` checks.

### 4. Standard IANA Timezone Support (`zoneinfo`) (PEP 615)
Introduced the `zoneinfo` module, incorporating system or IANA time zone database support directly into `datetime.datetime` without needing third-party libraries like `pytz`.

### 5. Relaxed Decorator Syntax (PEP 614)
Removed limitations on decorator expressions, allowing any valid Python expression returning a callable to be used directly as a decorator (e.g. `@buttons[0].on_click`).

### 6. New PEG-Based Parser for CPython (PEP 617)
Replaced Python's legacy LL(1) parser with a modern PEG (Parsing Expression Grammar) parser, removing structural grammar restrictions and paving the way for future syntax innovations like pattern matching.

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 584** | Dict Union (`|`, `|=`) | Merge dictionaries cleanly with operators |
| **PEP 585** | Built-in Generics | Standard types (`list[str]`, `dict[str, int]`) as type hints |
| **PEP 616** | `removeprefix`/`removesuffix` | String methods to safely strip leading/trailing strings |
| **PEP 615** | `zoneinfo` Module | Standard IANA time zone handling in `datetime` |
| **PEP 614** | Relaxed Decorators | Any valid expression as a decorator |
| **PEP 617** | PEG Parser | CPython parser architecture modernization |

---

## 💻 Pythonic Code Showcase

Check `main_3_9.py` in this directory for runnable code examples demonstrating:
- Merging and updating dictionaries using `|` and `|=`
- Writing native type annotations with `list[int]` and `dict[str, tuple[int, int]]`
- Clean string manipulation with `removeprefix()` and `removesuffix()`
- Creating localized `datetime` objects using `zoneinfo.ZoneInfo`
- Calculating least common multiple with `math.lcm()`
