"""Truth Value Testing (Truthiness and Falsiness in Python).

In Python, any object can be tested for truth value inside an 'if' condition.
The following values evaluate to False (Falsy):
1. 'False' and 'None'
2. Zero of any numeric type: 0, 0.0, 0j
3. Empty sequences and collections: '', (), [], {}, set(), range(0)

All other values evaluate to True (Truthy).

Import Notes:
    - 'from typing import Any, Dict': Standard library typing imports used for
      dynamic object type signatures and dictionary type hints.
"""

from typing import Any, Dict


def evaluate_truthiness(value: Any) -> bool:
    """Evaluate whether an arbitrary object is Truthy or Falsy in Python."""
    if value:
        return True
    else:
        return False


def get_falsy_examples() -> Dict[str, Any]:
    """Return a dictionary of canonical Falsy objects in Python."""
    return {
        "boolean_false": False,
        "none_object": None,
        "integer_zero": 0,
        "float_zero": 0.0,
        "empty_string": "",
        "empty_tuple": (),
        "empty_list": [],
        "empty_dict": {},
        "empty_set": set(),
    }


def demo_if_options() -> None:
    """Demonstrate truthiness evaluation for various Python objects."""
    print("--- Evaluating Falsy Values in Python ---")
    falsy_samples = get_falsy_examples()
    for name, sample_val in falsy_samples.items():
        is_truthy = evaluate_truthiness(sample_val)
        print(f"Name: {name:15s} | Value: {repr(sample_val):10s} -> Truthy: {is_truthy}")

    print("\n--- Evaluating Truthy Values in Python ---")
    truthy_samples = ["Hello", [1, 2], {"key": "val"}, 42, True]
    for sample_val in truthy_samples:
        is_truthy = evaluate_truthiness(sample_val)
        print(f"Value: {repr(sample_val):25s} -> Truthy: {is_truthy}")


if __name__ == "__main__":
    demo_if_options()
