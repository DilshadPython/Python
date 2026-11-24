# Technical Documentation: Python Iterators & Iterable Protocols

## 📊 Iterator Type & Protocol Matrix

| Container / Object | Iterable Method | Iterator Type | `__next__()` Behavior | Memory Footprint |
| :--- | :--- | :--- | :--- | :--- |
| **List (`list`)** | `iter(lst)` | `list_iterator` | Yields array elements sequentially | $O(N)$ list + $O(1)$ iterator |
| **Tuple (`tuple`)** | `iter(tpl)` | `tuple_iterator` | Yields tuple elements sequentially | $O(N)$ tuple + $O(1)$ iterator |
| **Dict (`dict`)** | `iter(d)` | `dict_keyiterator` | Yields dict keys in insertion order | $O(N)$ dict + $O(1)$ iterator |
| **String (`str`)** | `iter(s)` | `str_iterator` | Yields characters one-by-one | $O(N)$ str + $O(1)$ iterator |
| **File (`TextIOWrapper`)**| `iter(f)` | `TextIOWrapper` (Self) | Yields lines lazily without reading whole file | $O(1)$ buffer line memory |
| **Range (`range`)** | `iter(range(n))` | `range_iterator` | Calculates next int dynamically via C arithmetic | $O(1)$ space (~48 bytes) |

---

## 🛠️ Internal Dunder Hooks & Iterator Protocol

To implement a custom iterator class:

```python
class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        # Must return an iterator object (usually self)
        return self

    def __next__(self):
        # Must return next element or raise StopIteration
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val
```

---

## ⚡ Performance & Memory Notes (`iter(range(n))` vs List Iterators)

- **Range Iterator RAM Footprint**: `iter(range(1_000_000))` returns a `range_iterator` storing only 3 integers in C memory (**~48 bytes**, $O(1)$ space).
- **List Materialization Footprint**: `iter(list(range(1_000_000)))` materializes a 1M element list in RAM (~8 MB, $O(N)$ space).
