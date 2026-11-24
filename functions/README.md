# Python Function Modules — Pedagogical Reference Guide

The `Function/` directory contains a standardized set of PEP 8 compliant, type-hinted, and fully modularized Python tutorial scripts. Every script is standalone, executable, and free of function name duplications or redundant alias wrappers.

---

## Key Core Concepts Covered

### 1. Function Definition & Parameter Passing
- **Positional & Keyword Arguments**: `default_parameters.py`, `formatted_greeting.py`, `user_greeting.py`
- **Dynamic Argument Unpacking (`*args`, `**kwargs`)**: `args_unpacking.py`, `def_args_kwargs.py`
- **Lambda Expressions & Anonymous Functions**: `anonymous_func.py`
- **Multiple Return Values (Tuples & Dicts)**: `calculate_func.py`, `calculator_dict.py`, `tuple_arithmetic.py`

### 2. Lexical Scope & Variable Resolution (LEGB Rule)
- **Global Variable Modification (`global`)**: `def_and_global_var.py`, `global_keyword.py`, `global_variable.py`
- **Scope Shadowing & Access**: `global_scope_access.py`, `global_scope_shadowing.py`, `global_inner_local.py`
- **Nested Functions & Nonlocal Scope (`nonlocal`)**: `nested_function_scope.py`, `nested_scope_shadowing.py`, `nonlocal_scope_read.py`, `nonlocal_scope_modify.py`
- **Closure State Retention**: `closure_function.py`

### 3. Functional Patterns & Higher-Order Utilities
- **Mapping & Sequence Filtering**: `filter_func.py`, `higher_order_func.py`, `recursive_list_map.py`
- **Sequence Accumulation (`reduce`)**: `reduce_func.py`
- **Dispatch Tables (Emulating Switch/Case)**: `dispatch_dict.py`, `dispatch_if.py`
- **Function Object References**: `function_references.py`

### 4. Recursion Mechanics
All recursive functions define both a **base case** and a **recursive case**:
- `recursive_factorial.py` — Factorial computation via self-referential call stack.
- `recursive_count_letter.py` — Recursive sequence length calculation.
- `recursive_duplicate.py` — Recursive consecutive character deduplication.
- `recursive_explode.py` — Recursive string expansion.
- `recursive_string.py` — Recursive acronym extraction and transformation.

---

## Standardized Module Index (54 Unique Modules)

| Module Filename | Core Functionality | Key Function(s) |
| :--- | :--- | :--- |
| `absolute_values.py` | Compute absolute values for numeric/complex types | `calculate_abs_values()` |
| `add_int.py` | Basic addition operations and type hints | `add_int()`, `my_add()`, `add_me()` |
| `anonymous_func.py` | Lambda expression usage | `add`, `lambda_square` |
| `args_unpacking.py` | Unpacking positional argument lists | `calculate_sum()` |
| `boolean_func.py` | Boolean predicate evaluations | `is_even_boolean()`, `is_positive()` |
| `build_func.py` | Built-in `max()` and `min()` utilities | `get_max_and_min()` |
| `calculate_func.py` | Tuple return of arithmetic operations | `calculate()` |
| `calculator_dict.py` | Encapsulated calculator returning dictionary | `calculator()` |
| `call_return.py` | Return values and exponents | `calculate_exponent_square()`, `power()` |
| `cave_navigation.py` | Graph cave navigation data structure | `create_tunnel()`, `visit_cave()`, `choose_cave()` |
| `closure_function.py` | Closure multiplier state retention | `make_multiplier()` |
| `def_and_global_var.py` | Global variable modification | `bar()` |
| `def_args_kwargs.py` | Handling `*args` and `**kwargs` | `view()` |
| `def_calendar.py` | Standard library calendar output | `get_month_calendar()` |
| `def_str.py` | Case conversion and detail composition | `username()` |
| `default_parameters.py` | Required vs default parameters | `myfunc()` |
| `dispatch_dict.py` | Dictionary-based function dispatch table | `dispatch_dict()` |
| `dispatch_if.py` | Conditional branching function dispatch | `dispatch_if()` |
| `email_welcome.py` | Email verification and welcome composition | `view_email()`, `welcome_email()` |
| `factorial_func.py` | Iterative factorial calculation | `factorial()` |
| `filter_func.py` | Sequence filtering with predicates | `even_func()`, `get_even_numbers()` |
| `formatted_greeting.py` | Dynamic string formatting and varargs | `welcome_msg()`, `user_details()` |
| `function_references.py` | Dynamic function object references | `square_function_ref()` |
| `gender_translator.py` | Gender code translation | `translate_gender_code()` |
| `global_inner_local.py` | Inner function local scope declarations | `inner_local_scope()` |
| `global_keyword.py` | Modifying module-level global state | `test_global_modify()` |
| `global_scope_access.py` | Nested reading of outer global scope | `outer_global_access()` |
| `global_scope_shadowing.py` | Nested scope variable shadowing | `outer_scope_shadowing()` |
| `global_variable.py` | Global counter state management | `increment_global_counter()`, `get_counter_state()` |
| `greeting_welcome.py` | Multi-argument user greeting | `welcome_user()` |
| `higher_order_func.py` | Higher-order mapping using `map()` | `square_value()`, `apply_square()` |
| `if_func.py` | Predicates inside conditional blocks | `is_even_number()`, `check_number_parity()` |
| `metric_conversion.py` | Inches/feet to centimeter conversion | `centimeter()` |
| `multi_args_function.py` | Temperature conversions (F <-> C) | `fahrenheit_temp()`, `celsius_temp()`, `convert_temp_to()` |
| `nested_function_scope.py` | Distinct inner vs outer local scope | `outer_nested_scope()` |
| `nested_scope_shadowing.py` | Lexical scope shadowing in inner function | `outer_func_shadowing()` |
| `nonlocal_scope_modify.py` | Modifying enclosing variable with `nonlocal` | `outer_nonlocal_modify()` |
| `nonlocal_scope_read.py` | Reading enclosing variable via `nonlocal` | `outer_nonlocal_read()` |
| `number_square.py` | Simple number squaring computation | `square()` |
| `pay_tax.py` | Tax bracket and net pay calculations | `pay_tax()`, `neto_pay()` |
| `profile_formatter.py` | User profile summary formatting | `profile()` |
| `recursive_count_letter.py` | Recursive string sequence length | `count_letter()` |
| `recursive_duplicate.py` | Recursive character deduplication | `remove_duplicate()` |
| `recursive_explode.py` | Recursive string expansion | `recursive_explode()` |
| `recursive_factorial.py` | Recursive factorial calculation | `factorial_recur()` |
| `recursive_list_map.py` | Applying `map()` to list squaring | `square_element()`, `map_squares()` |
| `recursive_string.py` | Recursive acronym extraction | `pick_first_letter()`, `extract_acronym()`, `extract_acronym_uppercase()` |
| `reduce_func.py` | Sequence reduction via `functools.reduce` | `add_pair()`, `sum_sequence()` |
| `script_main_entry.py` | Standard main entry point pattern | `hello_entry()`, `main()` |
| `student_directory.py` | Student ID dictionary lookup table | `get_student_name()` |
| `triangle.py` | Triangle area computation | `calculate_triangle_area()` |
| `tuple_arithmetic.py` | Sum and difference tuple returns | `add_and_subtract_three()` |
| `user_greeting.py` | User greeting with default parameters | `greet_user()` |
| `vowel_counter.py` | Vowel counting in text strings | `vowels_count()` |

---

## Unit Testing

Execute all unit tests using CPython's test runner:

```bash
python3 -m unittest discover Function
```