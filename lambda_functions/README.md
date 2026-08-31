# Python Lambda Expressions — Anonymous Functions Reference

The `Lambda/` tutorial module demonstrates Python's `lambda` syntax—small, unnamed, inline anonymous functions defined using the `lambda` keyword. Every script is PEP 8 compliant, type-hinted, and fully modularized.

---

## Core Syntax & Rules

```python
lambda arguments: expression
```

1. **Inline Single Expression**: A lambda function can accept any number of arguments, but can only evaluate a single expression.
2. **Implicit Return**: The evaluated result of the single expression is automatically returned without using an explicit `return` keyword.
3. **First-Class Object**: Lambdas are function objects (`types.LambdaType`) and can be assigned to variables, passed as key arguments to `sort()`, `map()`, `filter()`, or stored inside dictionary dispatch tables.

---

## Standardized Module Index

| Module Filename | Functional Focus | Key Function / Lambda Definition |
| :--- | :--- | :--- |
| `lambda_addition.py` | Addition operations | `add_eight = lambda num: num + 8`<br>`add_two_numbers = lambda x, y: x + y` |
| `lambda_division.py` | Division & zero checks | `divide_by_eight = lambda num: num / 8.0`<br>`divide_two_numbers = lambda a, b: a / b if b != 0 else nan` |
| `lambda_multiplication.py` | Multiplication operations | `multiply_by_82 = lambda num: num * 82`<br>`multiply_two_numbers = lambda a, b: a * b` |
| `lambda_subtraction.py` | Subtraction operations | `subtract_eight = lambda num: num - 8`<br>`subtract_two_numbers = lambda a, b: a - b` |
| `lambda_exponentiation.py` | Exponentiation operations | `power_of_nine = lambda num: num ** 9`<br>`power_base_exp = lambda base, exp: base ** exp` |
| `lambda_remainder.py` | Modulo & remainder operations | `remainder_by_eight = lambda num: num % 8`<br>`remainder_two_integers = lambda a, b: a % b if b != 0 else 0` |
| `lambda_string_concat.py` | String formatting & surname concatenation | `format_full_name_string = lambda name: f"{name.strip().title()} Smith"` |
| `lambda_name_formatter.py` | Title formatting & list sorting by last name | `format_full_name = lambda fname, lname: ...`<br>`sort_names_by_last_name(name_list)` |
| `lambda_calculator_dispatch.py` | Dictionary dispatch table of lambda ops | `CALCULATOR_OPS = {'+': lambda a, b: a + b, ...}` |

---

## Performance Notes & `range()` Functional Integration

- **Lazy Evaluation**: In Python 3.3+, standard functions like `map()` and `filter()` return lazy iterators when combined with `lambda` expressions, eliminating memory overhead.
- **Range Object Efficiency**: Modern `range(start, stop, step)` sequence objects maintain $O(1)$ memory complexity and constant-time $O(1)$ membership testing (`x in range(...)`).
- **Inspection via `dir()`**: Running `dir(lambda)` reveals internal dunder attributes (`__name__`, `__qualname__`, `__code__`, `__closure__`), while `dir(range)` lists sequence protocol attributes (`start`, `stop`, `step`, `count`, `index`).

---

## Python Version Evolutions (Python 2.7 ➔ Python 3.3 ➔ Python 3.13)

- **Python 2.7**: Allowed tuple parameter unpacking (`lambda (x, y): x + y`) and allocated full lists for `range()` and `map()`.
- **Python 3.3+**: Removed tuple unpacking (PEP 3113), introduced `__qualname__` for nested lambda inspection, and made `range` and `map` memory-efficient lazy sequence/iterator objects.
- **Python 3.13**: CPython interpreter specialization optimizes boolean ternary dispatch (`TO_BOOL`, `POP_JUMP_IF_FALSE`) and call frames for inline lambda execution.

---

## Running Unit Tests

Execute all unit tests using CPython's test runner from the root directory:

```bash
python3 -m unittest discover Lambda
```

All unit tests verify string formatting, arithmetic accuracy, division by zero edge cases, sequence operations, and dictionary dispatch table lookups.

