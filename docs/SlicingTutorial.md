# Master Guide: Python Sequence Slicing

> **Module**: `slicing/`  
> **Topic**: Sequence indexing, strides, bounds, step directions, and string URL parsing.

---

## 1. Syntax Specification

$$\text{sequence}[\text{start} : \text{stop} : \text{step}]$$

- `start`: Initial index (inclusive). Defaults to `0` for positive step, or end for negative step.
- `stop`: Upper index (exclusive). Defaults to sequence length.
- `step`: Increment per step. Positive values move forward; negative values move backward.

---

## 2. Practical Examples

```python
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sub-slice
data[2:6]      # [2, 3, 4, 5]

# Reverse
data[::-1]     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Every other element
data[::2]      # [0, 2, 4, 6, 8]

# Negative indices
data[-4:-1]    # [6, 7, 8]
```

---

## 3. Slice Objects

The Python built-in `slice()` creates reusable slice instances:

```python
ODD_INDICES = slice(1, None, 2)
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[ODD_INDICES])  # [20, 40, 60]
```

---

## 4. Testing

Run the unit tests:
```bash
python3 -m unittest slicing/test_slicing.py
```
