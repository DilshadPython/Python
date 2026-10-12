# Technical Documentation: Python Sequence & Range Reversal

## 📊 Reversal Technique Matrix

| Data Structure | Reversal Syntax | Mutation | Return Type | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **String (`str`)** | `text[::-1]` | Out-of-Place | `str` | $O(N)$ | $O(N)$ |
| **String (`str`)** | `"".join(reversed(text))` | Out-of-Place | `str` | $O(N)$ | $O(N)$ |
| **List (`list`)** | `lst.reverse()` | In-Place | `None` | $O(N)$ | $O(1)$ |
| **List (`list`)** | `lst[::-1]` | Out-of-Place | `list` | $O(N)$ | $O(N)$ |
| **List (`list`)** | `reversed(lst)` | Out-of-Place | `reverse_iterator` | $O(1)$ startup | $O(1)$ |
| **Deque (`deque`)** | `d.reverse()` | In-Place | `None` | $O(N)$ | $O(1)$ |
| **Dict Keys (`dict_keys`)**| `reversed(d.keys())` | Out-of-Place | `dict_reversekeyiterator` | $O(1)$ startup | $O(1)$ |
| **Range (`range`)** | `reversed(range(n))` | Out-of-Place | `range_iterator` | $O(1)$ startup | $O(1)$ |

---

## 🛠️ Internal Dunder Hooks & Reversal Protocol

To make a custom class compatible with built-in `reversed(obj)`:

1. **Explicit Protocol Hook (`__reversed__`)**:
   ```python
   def __reversed__(self):
       # Must return an iterator object
       for item in reversed(self._data):
           yield item
   ```

2. **Sequence Fallback Protocol**:
   If `__reversed__()` is not defined, Python attempts to call `len(obj)` and access indices in descending order `obj[len - 1]`, `obj[len - 2]`, ..., `obj[0]`. This requires implementing:
   - `__len__(self) -> int`
   - `__getitem__(self, index: int)`

---

## ⚡ Performance & Memory Notes (`reversed(range(n))`)

- **Range Iterator RAM Footprint**: `reversed(range(1_000_000))` returns a C-level `range_iterator` occupying **~48 bytes** in memory ($O(1)$ space).
- **Materialized List Footprint**: `list(range(1_000_000))[::-1]` materializes a 1M element list in RAM (~8 MB, $O(N)$ space).
