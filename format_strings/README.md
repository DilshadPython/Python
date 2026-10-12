# Python String Formatting & Type Conversion Reference Suite

A comprehensive, production-grade Python reference suite demonstrating string formatting mechanisms: legacy `%` (printf-style) formatting, `str.format()`, modern f-strings (Python 3.6+), security-focused `string.Template`, and string type conversions.

---

## What is New

This directory has been refactored from disorganized and corrupted scripts (`convert_int_to_str.py`, `f_str.py`, `format.py`, `math.py`, `newformat.py`, `test.py`) into a structured, PEP 8-compliant 5-tier architecture:

1. **`percent_formatting_ops.py`**: `%`-style printf formatting (`%s`, `%r`, `%d`, `%f`, `%30.4f`, dictionary interpolation).
2. **`str_format_ops.py`**: `str.format()` method (`{0}`, `{key}`, `{pos[0]}`, `{obj.attr}`, alignment, padding, comma separator).
3. **`f_strings_ops.py`**: Modern f-string interpolation (`f"{fname} [{lname}]"`, `f"{a + b}"`, `f"{var=}"`, datetime formatting).
4. **`template_strings_ops.py`**: Security-focused `string.Template` interpolation (`substitute`, `safe_substitute`, custom delimiters).
5. **`type_conversion_ops.py`**: String type conversions (`str()`, `repr()`), numeric parsing (`int()`, `float()`), and type inspection (`type()`, `isinstance()`).
6. **`test_format_strings.py`**: Automated unittest test suite validating all 5 string formatting modules.

---

## Detailed Methods & Specifiers Reference

### 1. Legacy Percent (%) Formatting

#### `%s` vs `%r` Specifiers
- `%s`: Converts target object using `str(obj)` (human-readable format).
- `%r`: Converts target object using `repr(obj)` (canonical developer representation format).

```python
name = "Python"
version = 3.12
formatted = "Language: %s | Version (repr): %r" % (name, version)
# Result: 'Language: Python | Version (repr): 3.12'
```

#### Width & Precision Floating Point Specifiers (`%width.precisionf`)
Formats floating point numbers with specified total string width and decimal precision.

```python
val = 234.345678
# 1 decimal place
print("%1.1f" % val)  # '234.3'

# 30 width alignment with 4 decimal places
print("%30.4f" % val) # '                      234.3457'
```

#### Dictionary Key Interpolation (`%(key)s`)
Interpolates values from a dictionary into string placeholders matching dictionary keys.

```python
user_info = {"first_name": "Dilshad", "last_name": "Abdulla", "age": 30}
print("User %(first_name)s %(last_name)s is %(age)d" % user_info)
```

---

### 2. `str.format()` Method

#### Positional `{0}`, `{1}` & Named `{key}` Placeholders
Substitutes values using index order or explicit keyword names.

```python
print("Hello {0}! You live in {city}.".format("Dilshad", city="London"))
```

#### Indexing Sequences `{pos[0]}` & Accessing Attributes `{obj.attr}`
Accesses tuple/list elements or object attributes directly inside placeholders.

```python
import math

pos = (30, 175)
print("Age: {pos[0]} | Pi: {obj.pi}".format(pos=pos, obj=math))
```

#### Alignment & Padding Specifiers (`:<`, `:>`, `:^`)
Aligns string content within a minimum width.
- `:<10`: Left-aligned (padded right).
- `:>10`: Right-aligned (padded left).
- `:^10`: Center-aligned (padded both sides).

```python
print("{:<10}".format("Left"))    # 'Left      '
print("{:^10}".format("Center"))  # '  Center  '
print("{:>10}".format("Right"))   # '     Right'
```

#### Number Formatting (`:,.2f` and `:.1%`)
Formats numbers with comma thousand separators `,` or percentage notation `%`.

```python
print("${:,.2f}".format(1234567.89))  # '$1,234,567.89'
print("{:.1%}".format(0.755))          # '75.5%'
```

---

### 3. Modern F-Strings (Formatted String Literals)

#### Expression Evaluation
Evaluates any valid Python expression inside `{}` placeholders at runtime.

```python
a, b = 10, 20
print(f"Sum: {a + b} | Max: {max(a, b)}")
```

#### Self-Documenting Debug Syntax (`f"{var=}"`) - Python 3.8+
Prints the variable expression name alongside its evaluated value.

```python
x = 42
print(f"{x=}")  # 'x=42'
```

#### Datetime Formatting inside F-Strings
Formats datetime objects using standard `strftime` specifiers directly inside `{}`.

```python
from datetime import datetime

now = datetime.now()
print(f"Current Date: {now:%Y-%m-%d %H:%M}")
```

---

### 4. `string.Template` Operations

#### `substitute(mapping)`
Substitutes `$var` placeholders with values from dictionary. Raises `KeyError` if key is missing.

```python
from string import Template

tmpl = Template("Hello $name")
print(tmpl.substitute({"name": "Alice"}))  # 'Hello Alice'
```

#### `safe_substitute(mapping)`
Substitutes `$var` placeholders safely without raising errors for missing keys.

```python
tmpl = Template("Hello $name $missing")
print(tmpl.safe_substitute({"name": "Alice"}))  # 'Hello Alice $missing'
```

---

### 5. Type Conversions & Inspection

#### `str()` vs `repr()`
- `str()`: Returns readable string representation for end-users.
- `repr()`: Returns unambiguous canonical representation (with quotes, escape chars `\n`, `\t`).

```python
text = "Hello\nWorld"
print(str(text))   # Prints with actual newline
print(repr(text))  # Prints literal "'Hello\\nWorld'"
```

---

## File Structure Matrix

| Module | Primary Mechanisms | Description |
| :--- | :--- | :--- |
| `percent_formatting_ops.py` | `%s`, `%r`, `%d`, `%f`, `%(key)s` | C-style printf `%` formatting. |
| `str_format_ops.py` | `str.format()`, `{pos[0]}`, `{:,.2f}` | Flexible object method formatting. |
| `f_strings_ops.py` | `f"{var}"`, `f"{var=}"`, `f"{dt:%Y}"` | Modern runtime f-string interpolation. |
| `template_strings_ops.py` | `string.Template`, `safe_substitute` | Security-conscious safe variable template substitution. |
| `type_conversion_ops.py` | `str()`, `repr()`, `int()`, `isinstance()` | String type casting and runtime inspection. |
| `test_format_strings.py` | `unittest.TestCase` | Unit tests for all string formatting modules. |

---

## Running the Code & Unit Tests

### Run Individual Modules Directly

```bash
python3 percent_formatting_ops.py
python3 str_format_ops.py
python3 f_strings_ops.py
python3 template_strings_ops.py
python3 type_conversion_ops.py
```

### Run Unit Test Suite

```bash
python3 -m unittest test_format_strings.py
```

### Run Syntax Verification

```bash
python3 -m py_compile *.py
```
