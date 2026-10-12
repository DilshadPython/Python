# 🐍 Python Standard Library Easter Eggs (`easter_eggs`) Pedagogical Module

Welcome to the **`easter_eggs` Pedagogical Module**. This module presents a comprehensive breakdown of the famous in-jokes, design declarations, frozen module mechanisms, and humor hidden inside the Python Standard Library and CPython runtime core.

---

## 📂 Module Architecture

```
easter_eggs/
├── import_this_zen_of_python.py    # The Zen of Python (`import this`) & string obfuscation inspection
├── import_antigravity_xkcd.py      # Flying with Python (`import antigravity`) & XKCD #426 geohashing
├── import_future_braces.py         # Block delimiter declaration (`from __future__ import braces`)
├── import_hello_world.py           # Frozen CPython modules (`import __hello__` & `__phello__.spam`)
├── import_future_flufl.py          # PEP 401 Barry Warsaw Easter Egg (`from __future__ import barry_as_FLUFL`)
├── test_easter_eggs.py             # Unittest suite testing all 5 Easter Egg scripts
├── requirements.txt                # Dependency specification (Standard library footprint)
└── README.md                       # Module documentation and usage guide
```

---

## 🌟 What is New in This Module Update

1. **Descriptive, Standardized Filenames**: Replaced ambiguous single-word filenames (`antigravity.py`, `easter.py`, `future.py`, `hello.py`) with explicit, descriptive filenames matching their functionality.
2. **PEP 8 Compliance & Type Annotations**: Modernized code with standard Pythonic conventions, complete type hints (`-> None`, `-> str`), module docstrings, and `if __name__ == "__main__":` entry points.
3. **Internal Attribute & Method Introspection**: Exposed and documented internal attributes (such as `this.s`, `this.d`, and `antigravity.geohash`) with runnable helper functions.
4. **PEP 401 Integration (`barry_as_FLUFL`)**: Added demonstration of Python's April Fool's PEP 401 syntax rule enforcing the `<>` operator over `!=`.
5. **Comprehensive Unit Testing**: Introduced `test_easter_eggs.py` covering all scripts using Python's `unittest` framework.

---

## 🔍 Easter Eggs: Attributes, Methods & Code Breakdown

### 1. `import_this_zen_of_python.py` — The Zen of Python

Importing `this` prints Tim Peters' 19 guiding principles of Python design. The module encrypts the text using a simple ROT13 substitution cipher to keep the source code intriguing.

#### Attributes & Methods

- **`this.s`** *(str)*: Contains the ROT13-encoded text of the 19 aphorisms.
- **`this.d`** *(dict[str, str])*: A cipher lookup dictionary mapping characters to their ROT13 counterparts (e.g. `'a' -> 'n'`).

#### Code Example

```python
import this
from easter_eggs.import_this_zen_of_python import (
    get_zen_text,
    get_encoded_text,
    get_cipher_map,
)

# 1. Access raw ROT13 encoded string
encoded = get_encoded_text()
print(f"Encoded prefix: {encoded[:21]!r}")  # 'Gur Mra bs Clguba, ol'

# 2. Access substitution dictionary
cipher = get_cipher_map()
print(f"ROT13 mapping for 'a': {cipher['a']!r}")  # 'n'

# 3. Obtain decrypted Zen text
print(get_zen_text())
```

---

### 2. `import_antigravity_xkcd.py` — Flying with Python & Geohashing

Importing `antigravity` triggers an automatic side-effect by invoking `webbrowser.open("https://xkcd.com/353/")`, bringing up Randall Munroe's famous comic about Python's ease of use.

#### Attributes & Methods

- **`antigravity.geohash(latitude: float, longitude: float, datedow: bytes) -> None`**: Calculates an algorithmically generated geohash coordinate based on user coordinates and the Dow Jones Industrial Average opening value (XKCD comic #426).

#### Code Example

```python
import antigravity
from easter_eggs.import_antigravity_xkcd import calculate_geohash

# 1. Importing opens browser to https://xkcd.com/353/
# import antigravity

# 2. Execute geohash coordinate calculation
latitude = 37.421542
longitude = -122.085589
datedow = b"2005-05-26-10458.68"

calculate_geohash(latitude, longitude, datedow)
# Output: 37.857713 -122.544543
```

---

### 3. `import_future_braces.py` — Rejecting Curly Brace Syntax

Python uses significant whitespace and indentation to enforce code readability. When developers asked for optional curly brace `{}` block delimiters, Python core developers added `from __future__ import braces` to reject the idea permanently.

#### Exceptions & Behavior

- **`SyntaxError: not a chance`**: Attempting to parse or execute `from __future__ import braces` raises a `SyntaxError`.

#### Code Example

```python
from easter_eggs.import_future_braces import demonstrate_braces_import

# Safely catch and verify the SyntaxError message
error_message = demonstrate_braces_import()
print(f"Exception message: {error_message!r}")  # 'not a chance'
```

---

### 4. `import_hello_world.py` — CPython Frozen Module Fixtures

`__hello__` is a CPython built-in frozen module compiled directly into the C runtime (`Python/frozenmodules/__hello__.h`). It exists as a test fixture for CPython's frozen module importer (`PyImport_ImportFrozenModule`).

#### Side Effects & Package Variations

- **`import __hello__`**: Prints `"Hello world!"` to stdout upon import.
- **`import __phello__.spam`** *(Python 3.11+)*: Demonstrates frozen package importing.

#### Code Example

```python
from easter_eggs.import_hello_world import capture_hello_output, capture_phello_output

# Capture printed output from frozen module import
output = capture_hello_output()
print(f"Captured output: {output!r}")  # 'Hello world!'
```

---

### 5. `import_future_flufl.py` — PEP 401 Barry Warsaw Easter Egg

PEP 401 (April Fool's Day PEP) designated Barry Warsaw as "Friendly Language Uncle For Life" (FLUFL). Importing `barry_as_FLUFL` replaces the standard inequality operator `!=` with the Python 2 diamond operator `<>`.

#### Syntax Rules & Behavior

- **`!=` operator**: Raises `SyntaxError: with FLUFL, Use '<>' instead of '!='`.
- **`<>` operator**: Re-enabled for inequality comparisons under FLUFL.

#### Code Example

```python
from easter_eggs.import_future_flufl import (
    demonstrate_flufl_ne_error,
    demonstrate_flufl_diamond_op,
)

# 1. Using != raises SyntaxError
error = demonstrate_flufl_ne_error()
print(f"Error: {error!r}")  # "with FLUFL, Use '<>' instead of '!='"

# 2. Using <> evaluates successfully
is_valid = demonstrate_flufl_diamond_op()
print(f"1 <> 2 evaluates to: {is_valid}")  # True
```

---

## 🚀 Execution & Testing Guide

### 1. Run Individual Scripts

Execute any script directly using `python3`:

```bash
python3 easter_eggs/import_this_zen_of_python.py
python3 easter_eggs/import_antigravity_xkcd.py
python3 easter_eggs/import_future_braces.py
python3 easter_eggs/import_hello_world.py
python3 easter_eggs/import_future_flufl.py
```

### 2. Run the Unittest Suite

Execute the complete test suite:

```bash
python3 -m unittest easter_eggs/test_easter_eggs.py
```

Or using `pytest`:

```bash
pytest easter_eggs/test_easter_eggs.py
```
