# Python Sequence Slicing Master Guide

Welcome to the **Python Slicing Tutorial Module**. This guide explains sequence slicing notation `[start:stop:step]`, boundary behaviors, negative indices, reverse steps, and practical URL parsing techniques.

---

## 1. Slicing Syntax Overview

In Python, all sequence types (strings, lists, tuples, bytes) support the slicing operator:

$$\text{sequence}[\text{start} : \text{stop} : \text{step}]$$

* **`start`**: Index where the slice begins (inclusive). Defaults to `0` when `step > 0`, or the end of the sequence when `step < 0`.
* **`stop`**: Index where the slice ends (**exclusive**). Defaults to sequence length when `step > 0`, or before the beginning when `step < 0`.
* **`step`**: Stride or interval between elements. Defaults to `1`. A negative step traverses the sequence backwards.

---

## 2. Common Slicing Recipes

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sub-range (start at index 1, stop before index 8)
numbers[1:8]        # [1, 2, 3, 4, 5, 6, 7]

# Striding (every 2nd item from index 2 to 10)
numbers[2:10:2]     # [2, 4, 6, 8]

# Reverse the entire sequence
numbers[::-1]       # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Negative indices (count from the right end)
numbers[-5:]        # [6, 7, 8, 9, 10]
numbers[-8:-2]      # [3, 4, 5, 6, 7, 8]
```

---

## 3. Module Overview

| File | Description | Core Concept |
| :--- | :--- | :--- |
| `example.py` | Slicing patterns and generic helper | Positive/negative strides & bounds |
| `url_slicing.py` | String slicing on URLs vs `urllib.parse` | Slicing vs standard library parsers |
| `test_slicing.py` | Automated unit tests (`unittest`) | Boundary conditions and verification |

---

## 4. The `slice` Object

Under the hood, `sequence[start:stop:step]` translates to `sequence[slice(start, stop, step)]`. You can create named, reusable slice objects:

```python
FIRST_THREE = slice(0, 3)
LAST_TWO = slice(-2, None)

data = ["a", "b", "c", "d", "e"]
print(data[FIRST_THREE])  # ['a', 'b', 'c']
print(data[LAST_TWO])     # ['d', 'e']
```

---

## 5. Running the Unit Tests

Execute the test suite from the repository root:

```bash
python3 -m unittest slicing/test_slicing.py
```
Expected output:
```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
