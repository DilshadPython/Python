# Python Methods — Object Methods & Functional Transformation Reference

The `Methods/` tutorial module demonstrates Python method binding mechanics, built-in string/list method operations (`lower()`, `upper()`, `split()`, `strip()`, `len()`), higher-order functional transformers (`map()`, `filter()`, `reduce()`), dynamic attribute management (`delattr()`, `hasattr()`), and the fundamental distinction between standalone **Functions** and bound **Methods**.

---

## Standardized Module Index

| Module Filename | Functional Focus | Key Method / Function Signature |
| :--- | :--- | :--- |
| `class_attribute_deleter.py` | Dynamic class attribute deletion | `inspect_and_delete_attribute(cls_or_obj, attr_name)` |
| `object_vs_dict_deleter.py` | Object attribute vs dictionary key deletion | `delete_object_attribute(car_obj, attr_name)`<br>`delete_dictionary_key(car_dict, key_name)` |
| `factorial_calculator.py` | Iterative integer factorial computation | `calculate_factorial(num)` |
| `iterable_filter_mean.py` | Statistical mean filtering with `filter()` | `filter_numbers_by_mean(data)` |
| `falsy_value_filter.py` | Falsy element removal via `filter(None, ...)` | `remove_falsy_values(items)` |
| `string_length_calculator.py` | String length measurement using `len()` | `calculate_string_length(text)` |
| `temperature_map_converter.py` | Celsius to Fahrenheit mapping with `map()` | `convert_celsius_to_fahrenheit(cities_celsius)` |
| `string_lowercase_converter.py` | Lowercase transformation using `str.lower()` | `convert_to_lowercase(text)` |
| `string_uppercase_converter.py` | Uppercase transformation using `str.upper()` | `convert_to_uppercase(text)` |
| `string_splitter.py` | String splitting using `str.split()` | `split_string(text, delimiter)` |
| `string_whitespace_stripper.py` | Whitespace removal using `str.strip()` | `strip_whitespace(text)` |
| `circle_area_map_calculator.py` | Circle area sequence mapping with `map()` | `calculate_areas_for_radii(radii)` |
| `random_math_evaluator.py` | Random values with arithmetic evaluation | `evaluate_math_operations(x, y)` |
| `functional_reduce_product.py` | Sequence cumulative product via `reduce()` | `calculate_cumulative_product(numbers)` |
| `function_vs_method_comparison.py` | Comparative analysis: Functions vs Methods | `compare_function_and_method()` |

---

## Summary Comparison: Functions vs Methods

| Attribute / Feature | Standalone Function (`def`) | Bound Object Method (`def method(self)`) |
| :--- | :--- | :--- |
| **Namespace Binding** | Bound to module global namespace | Bound to a class instance (`self`) or class object (`cls`) |
| **Invocation Syntax** | Called directly: `func(arg1, arg2)` | Called on instance: `instance.method(arg)` |
| **Implicit Parameter** | No implicit parameter | Implicit `self` (instance) or `cls` (class) passed automatically |
| **Descriptor Binding** | Unbound `function` object | Wrapped `method` object via Python's descriptor protocol (`__get__`) |

---

## Running Unit Tests

Execute the comprehensive unit test suite from the repository root:

```bash
python3 -m unittest discover Methods
```

All 14 test cases verify dynamic attribute deletion, dict key deletion, string operations, higher-order transformations (`map`/`filter`/`reduce`), and method binding comparisons.
