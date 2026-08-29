# Python Loops & Iteration Constructs (`Loops`)

A comprehensive, production-grade guide to Python iteration constructs, `for` and `while` loop mechanics, sequence indexing, dictionary traversal, control flow keywords (`break`, `continue`, `pass`, `for-else`), and cross-version compatibility across Python releases (**Python 2.7**, **Python 3.3** through **Python 3.13**).

---

## 📋 Directory File Index

| Script / Document | Core Topic / Feature | Key Functions & Concepts |
| :--- | :--- | :--- |
| [`_notused.py`](_notused.py) | Unused Loop Variables (`_`) | `execute_unused_variable_loop()`: Conventional throwaway loop counter `_`. |
| [`add_nums.py`](add_nums.py) | Accumulation & Deduplication | `accumulate_list_manually()`, `accumulate_list_builtin()`, `deduplicate_numbers()`: Summing and set casting. |
| [`big_word.py`](big_word.py) | File Analysis & Dict Traversal | `calculate_word_frequencies()`, `find_most_frequent_word()`: Reading `words.txt` and dict counter tracking. |
| [`def_for.py`](def_for.py) | Range Iteration Function | `generate_range_list()`: Generating bounded list sequences via `range(start, stop + 1)`. |
| [`def_while_for.py`](def_while_for.py) | Validation + Iteration | `validate_positive_integer()`, `repeat_python_greeting()`: Combining `while` validation with `for` loops. |
| [`double_def_for.py`](double_def_for.py) | Modular Function Delegation | `execute_repeated_greeting()`: Function orchestration passing input params to `for` loops. |
| [`elevator.py`](elevator.py) | Floor Navigation Simulator | `navigate_elevator()`: Simulating elevator floor-by-floor ascent and destination check. |
| [`end_py.py`](end_py.py) | Line Ending Customization | `format_horizontal_sequence()`, `demonstrate_print_end_parameter()`: Overriding `print()` default `end='\n'`. |
| [`exculator.py`](exculator.py) | Elevator Compatibility Wrapper | `run_exculator_simulation()`: Backwards compatibility wrapper for corrected elevator simulation. |
| [`for_bar.py`](for_bar.py) | File Reading Bar Chart | `generate_grade_bar()`, `process_grade_bars()`: Reading `grade.txt` and generating ASCII `#` grade bars. |
| [`for_dic_key.py`](for_dic_key.py) | Dict Keys & Values Traversal | `inspect_dictionary_keys()`, `inspect_dictionary_values()`, `inspect_dictionary_key_value_pairs()`. |
| [`for_dict.py`](for_dict.py) | Dict Sequence & Range Lookup | `display_user_summaries()`, `filter_users_by_social_platform()`, `search_users_by_id_range()`. |
| [`for_else.py`](for_else.py) | `for-else` Search Mechanics | `search_technology_stack()`: Executing `else` block when loop completes without hitting `break`. |
| [`for_enumerate_index.py`](for_enumerate_index.py) | Automatic Indexing | `generate_enumerated_pairs()`: Pairing items with 0-based indices via `enumerate()`. |
| [`for_factorial.py`](for_factorial.py) | Iterative Factorial Computation | `calculate_factorial()`: Calculating $n!$ iteratively using accumulator product loop. |
| [`for_factrorial.py`](for_factrorial.py) | Factorial Compatibility Wrapper | `run_legacy_factorial_demo()`: Backwards compatibility alias for factorial module. |
| [`for_index.py`](for_index.py) | Fixed vs Dynamic Index Lookup | `search_car_inventory_fixed_range()`, `search_car_inventory_dynamic_range()`: Corrected vehicle search. |
| [`for_len.py`](for_len.py) | Indexing vs `enumerate()` | `list_libraries_via_range_len()`, `list_libraries_via_enumerate()`: Comparing index loops to `enumerate()`. |
| [`for_list.py`](for_list.py) | List Traversal & Slicing | `iterate_entire_list()`, `iterate_list_slice()`: Looping over positive/negative list slices. |
| [`for_loop.py`](for_loop.py) | Control Flow & Nested Loops | `iterate_names_basic()`, `demonstrate_break()`, `demonstrate_continue()`, `demonstrate_nested_loops()`. |
| [`for_print.py`](for_print.py) | String Repetition Formatting | `repeat_string_horizontal()`, `repeat_string_vertical()`: Formatting string multipliers. |
| [`for_range.py`](for_range.py) | `range()` Signature Variants | `generate_single_arg_range()`, `generate_two_arg_range()`, `generate_stepped_range()`. |
| [`for_tuple.py`](for_tuple.py) | Tuple Traversal & Max Length | `iterate_tuple_elements()`, `accumulate_tuple_sum()`, `find_longest_string_in_tuple()`. |
| [`grade.txt`](grade.txt) | Sample Grade Dataset | Raw numerical grade dataset used by `for_bar.py`. |
| [`print_shape_forloop.py`](print_shape_forloop.py) | ASCII Hash Right Triangles | `generate_ascending_hash_triangle()`, `generate_descending_hash_triangle()`. |
| [`shape_code.py`](shape_code.py) | Complex Pyramid Patterns | `generate_numeric_pyramid_shape()`: Multi-loop nested shape generation. |
| [`stop.py`](stop.py) | Keyword Mechanics | `evaluate_loop_keywords()`: Demonstrating `break`, `continue`, and `pass` actions. |
| [`while_for.py`](while_for.py) | Interactive Validation Loop | `validate_positive_number()`, `repeat_greeting_loop()`: Robust `while True` validation. |
| [`words.txt`](words.txt) | Sample Word Corpus | Text file corpus used for dictionary frequency analysis in `big_word.py`. |
| [`test_loops.py`](test_loops.py) | Automated Unit Test Suite | 25 comprehensive `unittest` test cases covering all functions in this directory. |

---

## 📦 Understanding Python Import Statements (`import` vs `from ... import ...`)

Python provides two primary mechanisms for importing modules from the standard library or local packages:

### 1. `import module_name`
* **Syntax**: `import os`, `import sys`
* **Behavior**: Loads the entire module object into memory and binds it to the specified name in the current namespace.
* **Access Pattern**: Functions and attributes must be qualified with the module prefix (e.g., `os.path.exists()`, `sys.path`).
* **Advantages**: Prevents namespace pollution and avoids accidental function overwrites.

### 2. `from module_name import symbol_name`
* **Syntax**: `from typing import List, Tuple, Dict, Set, Optional, Any`
* **Behavior**: Extracts specific classes, functions, or constants from the target module directly into the local namespace.
* **Access Pattern**: Symbols are called directly without module prefixing (e.g., `List[int]` instead of `typing.List[int]`).
* **Advantages**: Concise, highly readable code when specifying static type annotations or frequently invoked utilities.

---

### 3. 📌 Script-by-Script Import Purpose Reference Table

The table below explains exactly what each `import` or `from ... import` statement does in every script in the `Loops` folder:

| Script Name | Import Statement(s) | Imported Module / Symbol | Purpose & Role in the Loop Script |
| :--- | :--- | :--- | :--- |
| [`_notused.py`](_notused.py) | `from typing import List` | `typing.List` | Type hint for `execute_unused_variable_loop()` returning a list of message strings (`List[str]`). |
| [`add_nums.py`](add_nums.py) | `from typing import List, Set` | `typing.List`, `typing.Set` | Type hints for iterating through integer lists (`List[int]`) and set deduplication (`Set[int]`). |
| [`big_word.py`](big_word.py) | `import os`<br>`from typing import Dict, Tuple, Optional` | `os`<br>`typing.Dict`, `Tuple`, `Optional` | `os.path.exists()` checks if dataset `words.txt` exists before loop processing.<br>`Dict`/`Tuple` annotate word frequency dictionary counts and top word result. |
| [`def_for.py`](def_for.py) | `from typing import List` | `typing.List` | Type hint annotating generated numeric range lists (`List[int]`). |
| [`def_while_for.py`](def_while_for.py) | `import sys`<br>`from typing import List` | `sys`<br>`typing.List` | `sys.stdin.isatty()` checks whether terminal execution is interactive or non-interactive.<br>`List` annotates output message lists. |
| [`double_def_for.py`](double_def_for.py) | `from typing import List` | `typing.List` | Type hint annotating repeated greeting string sequences. |
| [`elevator.py`](elevator.py) | `from typing import List, Tuple` | `typing.List`, `Tuple` | Type hints annotating floor navigation sequence history and status tuples (`Tuple[bool, List[int]]`). |
| [`end_py.py`](end_py.py) | `from typing import List` | `typing.List` | Type hint annotating formatted horizontal range sequence lists. |
| [`exculator.py`](exculator.py) | `from typing import List, Tuple`<br>`from elevator import navigate_elevator` | `typing`, `elevator` | Re-exports type annotations and delegates elevator navigation logic to `elevator.py` wrapper. |
| [`for_bar.py`](for_bar.py) | `import os`<br>`from typing import List, Tuple` | `os`<br>`typing.List`, `Tuple` | `os.path.exists()` verifies dataset file `grade.txt`.<br>`List`/`Tuple` annotate grade line processing and output bar strings. |
| [`for_dic_key.py`](for_dic_key.py) | `from typing import Dict, List, Tuple, Any` | `typing` module symbols | Type hints for dictionary keys, values, and key-value tuple pairs (`Dict[str, int]`, `List[Any]`). |
| [`for_dict.py`](for_dict.py) | `from typing import Dict, List, Tuple, Any` | `typing` module symbols | Type hints annotating nested user dictionary data structures, filtered user lists, and ID ranges. |
| [`for_else.py`](for_else.py) | `from typing import List, Tuple` | `typing.List`, `Tuple` | Type hints annotating technology stack arrays and search status result tuples (`Tuple[bool, str]`). |
| [`for_enumerate_index.py`](for_enumerate_index.py) | `from typing import List, Tuple` | `typing.List`, `Tuple` | Type hints annotating parallel inputs and enumerated tuple records (`List[Tuple[int, str, int]]`). |
| [`for_factorial.py`](for_factorial.py) | Built-in integer operations | Built-in types | Annotates positive integer parameters and iterative factorial product calculation. |
| [`for_factrorial.py`](for_factrorial.py) | `from for_factorial import calculate_factorial` | `for_factorial` module | Imports `calculate_factorial()` from `for_factorial.py` to maintain legacy filename compatibility. |
| [`for_index.py`](for_index.py) | `from typing import List, Tuple` | `typing.List`, `Tuple` | Type hints annotating car inventory arrays and search result tuples (`Tuple[bool, int]`). |
| [`for_len.py`](for_len.py) | `from typing import List` | `typing.List` | Type hint annotating Python library string list (`List[str]`). |
| [`for_list.py`](for_list.py) | `from typing import List, Any, Optional` | `typing` module symbols | Type hints annotating list slicing parameters (`Optional[int]`) and list item sequences. |
| [`for_loop.py`](for_loop.py) | `from typing import List, Tuple` | `typing.List`, `Tuple` | Type hints annotating name arrays, break/continue targets, and nested loop product pairs (`List[Tuple[str, int]]`). |
| [`for_print.py`](for_print.py) | `from typing import Tuple` | `typing.Tuple` | Type hint annotating formatted horizontal and vertical string output pairs (`Tuple[str, str]`). |
| [`for_range.py`](for_range.py) | `from typing import List, Tuple` | `typing.List`, `Tuple` | Type hints annotating single-arg, two-arg, and stepped range sequence arrays (`List[int]`). |
| [`for_tuple.py`](for_tuple.py) | `from typing import Tuple, List` | `typing.Tuple`, `List` | Type hints annotating tuple sequence inputs, running totals, and longest city name calculations. |
| [`print_shape_forloop.py`](print_shape_forloop.py) | `from typing import List` | `typing.List` | Type hint annotating generated right-triangle ASCII hash row strings (`List[str]`). |
| [`shape_code.py`](shape_code.py) | `from typing import List` | `typing.List` | Type hint annotating multi-loop nested numeric pyramid pattern line strings (`List[str]`). |
| [`stop.py`](stop.py) | `from typing import List, Tuple` | `typing.List`, `Tuple` | Type hints annotating sequence token lists and loop keyword execution state tuples (`Tuple[List[str], str]`). |
| [`while_for.py`](while_for.py) | `import sys`<br>`from typing import List, Optional` | `sys`<br>`typing` module symbols | `sys.stdin.isatty()` checks interactive terminal status to prevent non-interactive input blockages.<br>`List`/`Optional` annotate loop counts. |
| [`test_loops.py`](test_loops.py) | `import os, sys, unittest`<br>`from unittest.mock import patch` | `os`, `sys`, `unittest`, `patch` | `os` resolves path to dataset files (`words.txt`, `grade.txt`).<br>`sys` configures `sys.path` for importing local modules.<br>`unittest` provides test case framework.<br>`patch` mocks `builtins.input` for non-interactive test runs. |

---

## 🔄 `for` Loop vs. `while` Loop: Differences & Usage Guide

Understanding when to choose a `for` loop versus a `while` loop is fundamental to writing clean, Pythonic code.

### 1. Key Differences at a Glance

| Feature / Aspect | `for` Loop | `while` Loop |
| :--- | :--- | :--- |
| **Iteration Type** | **Definite Iteration** (Bounded) | **Indefinite Iteration** (Unbounded) |
| **Primary Purpose** | Traversal over collections, sequences, or fixed ranges | Repeating logic until a dynamic boolean condition becomes `False` |
| **Counter Control** | Managed automatically by Python's iterator protocol | Managed manually by the programmer (initialize & increment) |
| **Infinite Loop Risk** | Extremely low (bounded by iterable length) | High (if termination condition is missed or counter is not updated) |
| **Idiomatic Use Cases** | Lists, tuples, dicts, strings, file lines, `range()` | User input validation, server polling, game loops, state machines |

---

### 2. When to Use a `for` Loop

Use a `for` loop when you **know the sequence or number of iterations in advance** or when traversing data structures.

#### Example 1: Sequence Traversal
```python
cities = ["Paris", "London", "Brussels", "Tokyo"]
for city in cities:
    print(f"Destination: {city}")
```

#### Example 2: Fixed Repetition via `range()`
```python
# Execute an action exactly 5 times
for step in range(1, 6):
    print(f"Step {step} completed.")
```

---

### 3. When to Use a `while` Loop

Use a `while` loop when **iterations depend on a dynamic condition** that could change at runtime (such as user input, network status, or state flags), and the exact number of iterations is unknown in advance.

#### Example 1: User Input Validation (`while True` + `break`)
```python
while True:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        number = int(user_input)
        break  # Exit loop when valid input is received
    print("Invalid entry! Please try again.")
```

#### Example 2: Condition-Based Accumulation
```python
balance = 100
withdrawal_fee = 15

while balance >= withdrawal_fee:
    balance -= withdrawal_fee
    print(f"Fee deducted. Remaining balance: ${balance}")
```

---

### 4. Selection Guidelines (How to Choose)

1. **Ask: "Do I have a collection or fixed range of items to process?"**
   - **YES** $\rightarrow$ Use a **`for` loop**.
2. **Ask: "Am I waiting for an external event, user input, or dynamic condition?"**
   - **YES** $\rightarrow$ Use a **`while` loop**.
3. **Avoid mutating collections in `for` loops**: Modifying a list while iterating over it causes skipped elements. Iterate over a slice copy `for item in items[:]:` instead.
4. **Avoid infinite `while` loops**: Ensure the variable controlling the `while` condition is modified inside the loop body, or provide an explicit `break` mechanism.

---

## ⚡ Loop Constructs & Python Code Evolution (Python 3.3 to Python 3.13) & Python 2.7 Comparison

### Python 2.7 Legacy Comparison

In Python 2.7 (deprecated December 31, 2019):
1. **`xrange()` vs `range()`**: `range()` generated an immediate, in-memory `list` object, consuming memory proportional to range size. `xrange()` generated items lazily on demand. In Python 3, `xrange()` was removed and `range()` became an efficient lazy sequence generator.
2. **`print` Statement**: `print` was a keyword statement (`print "Hello",`), whereas Python 3 requires the `print()` function with keyword arguments like `end=" "` and `sep=", "`.
3. **Dictionary Traversal**: Python 2.7 provided `.iteritems()`, `.iterkeys()`, and `.itervalues()` for lazy iterator traversal alongside `.items()`, `.keys()`, `.values()` which returned lists. Python 3 replaced all dict methods with lightweight, dynamic dict view objects (`.items()`, `.keys()`, `.values()`).
4. **Loop Variable Leaking in List Comprehensions**: In Python 2.7, variables defined in list comprehensions leaked into the surrounding function or global scope. Python 3 isolates list comprehension variables into dedicated function scopes.
5. **Lazy Evaluation of `zip()` and `map()`**: In Python 2.7, `zip()` and `map()` returned full lists. In Python 3, they return lazy iterators.

```python
# ==============================================================================
# Python 2.7 Legacy Loop Sample
# ==============================================================================
# 1. Range memory consumption:
# In Python 2.7, range(1000000) creates a 1-million item list in RAM:
for i in xrange(1, 6):
    print "Iteration:", i,

print ""  # Print newline

# 2. Dictionary iteration:
user_ages = {"Alan": 23, "Sara": 30}
for name, age in user_ages.iteritems():
    print name, "is", age

# 3. Variable scope leak in Python 2.7:
[x for x in range(5)]
# In Python 2.7, 'x' remains in scope after the comprehension with value 4.
# In Python 3.x, 'x' is isolated and throws NameError if referenced outside.
```

---

### Code Evolution: Python 3.3 to Python 3.13

#### 1. Python 3.3 – Standard Memory-Efficient Iterators
Python 3.3 established lazy `range()`, `zip()`, and `map()` iterators, eliminating unnecessary memory allocations during loop traversal.

#### 2. Python 3.5 – Async Iteration (`async for`) & Matrix Multiplication (`@`)
PEP 492 introduced asynchronous iteration for handling asynchronous data streams:
```python
# Python 3.5+ Syntax:
async for data_chunk in async_data_stream():
    await process_chunk(data_chunk)
```

#### 3. Python 3.8 – Assignment Expressions (The Walrus Operator `:=`)
PEP 572 enabled values to be assigned and evaluated directly inside `while` loop conditions:
```python
# Python 3.8+ Syntax:
# Reading lines until an empty line is encountered:
while (line := file_handle.readline().strip()):
    print(f"Processing line: {line}")
```

#### 4. Python 3.10 – Structural Pattern Matching (`match-case`) inside Loops
PEP 634 introduced `match-case` statements, streamlining conditional branching within loops:
```python
# Python 3.10+ Syntax:
for command in commands_list:
    match command.split():
        case ["MOVE", direction]:
            print(f"Moving {direction}")
        case ["STOP"]:
            break
        case _:
            print("Unknown instruction")
```

#### 5. Python 3.11 – Adaptive Interpreter Specialization & Fast Loops
Python 3.11 introduced the **Faster CPython** initiative with specialized bytecode instructions like `FOR_ITER_LIST` and `FOR_ITER_RANGE`, accelerating list and range loops by up to 25-60%.

#### 6. Python 3.12 & 3.13 – Free-Threading & JIT Compiler Enhancements
Python 3.12 and 3.13 added preliminary JIT compilation and experimental support for free-threaded execution (`--disable-gil`), allowing parallel loop execution across CPU cores without Global Interpreter Lock contention.

---

## ⚡ Documentation & Performance Notes

### 1. Loop Performance Optimization Guidelines
* **Prefer Built-in Functions**: Avoid writing manual accumulator loops (`running_total += item`) when built-in functions like `sum()`, `min()`, `max()`, or `any()` are available. Built-ins execute directly in optimized C code.
* **Avoid `range(len(sequence))`**: Iterating directly over items (`for item in sequence:`) or using `enumerate(sequence)` is significantly faster and more Pythonic than indexing (`sequence[i]`).
* **Use List Comprehensions**: List comprehensions `[transform(x) for x in data]` are faster than repeatedly calling `.append()` inside explicit `for` loops due to bytecode optimization.

---

### 2. Python Version Updates for Conditional (`If`) Statements

Conditional branching (`if`, `elif`, `else`) forms the core of loop break/continue decisions and filtering logic. Key updates across Python versions include:

#### A. Boolean Truthiness Matrix
In Python, all objects evaluate to `True` or `False` in conditional contexts:
* **Falsy Values**: `False`, `None`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dict), `set()`.
* **Truthy Values**: Non-zero numbers, non-empty strings, collections, and custom objects.

#### B. The Walrus Operator in Conditions (Python 3.8+)
Allows inline assignment and comparison:
```python
if (word_count := len(text.split())) > 100:
    print(f"Long text document detected ({word_count} words).")
```

#### C. Structural Pattern Matching (Python 3.10+)
Replaces complex `if-elif-else` chains with pattern guards:
```python
def evaluate_status(status_code: int) -> str:
    match status_code:
        case 200 | 201:
            return "Success"
        case 400 | 404:
            return "Client Error"
        case 500 if server_available:
            return "Transient Server Error"
        case _:
            return "Unknown Status"
```

#### D. Short-Circuit Evaluation & Identity vs Equality
* **Short-Circuiting**: In `A and B`, if `A` is `False`, `B` is never evaluated. In `A or B`, if `A` is `True`, `B` is never evaluated.
* **Identity (`is`) vs Equality (`==`)**: `a is None` compares raw memory addresses in a single CPU instruction, whereas `a == None` invokes the `__eq__()` magic method lookup.

#### E. Python 3.12 & 3.13 Bytecode Branch Optimizations
Python 3.12 and 3.13 introduced optimized `TO_BOOL` and `POP_JUMP_IF_FALSE` interpreter opcodes, reducing conditional jump overhead by evaluating object truthiness directly at the bytecode level.

---

## 🧪 Executing Unit Tests

To execute the automated unit test suite across all 25 scripts in this directory:

```bash
python3 test_loops.py
```

Or run using standard library module discovery:

```bash
python3 -m unittest discover -s Loops -p "test_*.py"
```

All 25 test cases pass cleanly with 100% assertion coverage.
