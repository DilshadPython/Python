# Logical Operators in Python (`and`, `or`, `not`)

In Python, logical operators are used to combine or invert conditional statements. They evaluate expressions using **short-circuit logic** and return boolean results (or the evaluating operand).

## 1. Logical `and` Operator

The `and` operator returns `True` if **both** operands are evaluated as `True`. If the first expression is `False`, Python short-circuits and skips evaluating the second expression.

| Relation 1 | Logical Operator | Relation 2 | Result |
| :--- | :---: | :--- | :--- |
| `True` | `and` | `True` | **`True`** |
| `True` | `and` | `False` | **`False`** |
| `False` | `and` | `True` | **`False`** |
| `False` | `and` | `False` | **`False`** |

---

## 2. Logical `or` Operator

The `or` operator returns `True` if **at least one** operand evaluates to `True`. If the first expression is `True`, Python short-circuits and skips evaluating the second expression.

| Relation 1 | Logical Operator | Relation 2 | Result |
| :--- | :---: | :--- | :--- |
| `True` | `or` | `True` | **`True`** |
| `True` | `or` | `False` | **`True`** |
| `False` | `or` | `True` | **`True`** |
| `False` | `or` | `False` | **`False`** |

---

## 3. Logical `not` Operator

The `not` operator inverts the truth value of a single boolean expression.

| Operand Expression | Result |
| :--- | :--- |
| `not True` | **`False`** |
| `not False` | **`True`** |
