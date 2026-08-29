"""Advanced Logical Compound Expressions ('and', 'or', 'not').

Demonstrates combining multiple relational expressions using logical operators
with short-circuit evaluation guarantees.

Import Notes:
    - 'from typing import Dict': Used for type annotating dictionary return values.
"""

from typing import Dict


def evaluate_compound_conditions(first_val: int, second_val: int, third_val: int) -> Dict[str, bool]:
    """Evaluate multiple logical rules against input numbers.
    
    Notes:
        - 'and' requires BOTH expressions to be True.
        - 'or' requires AT LEAST ONE expression to be True.
        - 'not' negates a boolean expression.
    """
    all_true = (first_val == second_val) and (third_val > first_val)
    at_least_one_true = (first_val == second_val) or (third_val < first_val)
    negated_check = not (third_val < second_val)

    return {
        "all_conditions_true": all_true,
        "at_least_one_true": at_least_one_true,
        "negated_check": negated_check,
    }


def demo_if_advance() -> None:
    """Run compound logical condition demonstration."""
    val_x, val_y, val_z = 100, 100, 300
    results = evaluate_compound_conditions(val_x, val_y, val_z)

    print(f"Inputs: first_val={val_x}, second_val={val_y}, third_val={val_z}")
    print(f"first_val == second_val and third_val > first_val -> {results['all_conditions_true']}")
    print(f"first_val == second_val or third_val < first_val  -> {results['at_least_one_true']}")
    print(f"not (third_val < second_val)                     -> {results['negated_check']}")


if __name__ == "__main__":
    demo_if_advance()
