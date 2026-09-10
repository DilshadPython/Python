# JavaScript Object Notation (JSON) Master Guide (`json`)

Welcome to the **JSON Standard Library Master Guide**, a production-grade educational reference detailing JSON string parsing (`json.loads`), formatting (`json.dumps`), file I/O (`json.load`, `json.dump`), custom `JSONEncoder` subclassing, `object_hook` deserialization, unit testing via `unittest`, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & Architectural Architecture](#-overview--architectural-architecture)
2. [Python-to-JSON Type Mapping Matrix](#-python-to-json-type-mapping-matrix)
3. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
4. [Directory Structure & Module Overview](#-directory-structure--module-overview)
5. [How to Run the Code](#-how-to-run-the-code)
6. [Running Unit Tests](#-running-unit-tests)
7. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
8. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 📁 Overview & Architectural Architecture

**JSON (JavaScript Object Notation)** is a lightweight, human-readable data interchange format. The Python `json` standard library encodes Python data structures into JSON strings and decodes JSON payloads back into native Python types.

```text
[ Python dict / list / object ]  --- json.dumps() / json.dump() --->  [ JSON String / File ]
[ JSON String / File Payload ]  --- json.loads() / json.load() --->  [ Python dict / list ]
```

---

## 🔄 Python-to-JSON Type Mapping Matrix

| Python Type | JSON Equivalent | Encoding Notes |
| :--- | :--- | :--- |
| `dict` | `object` | Unpacked into key-value pairs (keys converted to strings) |
| `list`, `tuple` | `array` | Enclosed in square brackets `[...]` |
| `str` | `string` | Encoded with double quotes ` "..." ` |
| `int`, `float` | `number` | Serialized as numerical literal |
| `True` / `False` | `true` / `false` | Converted to lowercase JSON boolean literals |
| `None` | `null` | Converted to JSON `null` literal |

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_json.py`](file:///home/monika/PycharmProjects/Devel/Python/json_tutorial/beginner_json.py))
Focuses on standard string and file JSON parsing methods:
- **String Parsing**: `dict_obj = json.loads(raw_str)`.
- **String Formatting**: `formatted_str = json.dumps(dict_obj, indent=4)`.
- **File Read / Write**: `json.dump(obj, file)` and `json.load(file)`.

```python
# Beginner Example: loads() and dumps()
parsed_dict = json.loads('{"title": "Python", "year": 2026}')
formatted_json = json.dumps(parsed_dict, indent=4)
print(formatted_json)
```

---

### 🚀 Intermediate Level ([`intermediate_json.py`](file:///home/monika/PycharmProjects/Devel/Python/json_tutorial/intermediate_json.py))
Focuses on custom `JSONEncoder` subclassing for non-standard types (`datetime`, `@dataclass`) and sorted formatting:
- **Custom JSONEncoder**: Subclassing `json.JSONEncoder` and overriding `default(self, obj)`.
- **Sorted Keys & Formatting**: `json.dumps(obj, cls=CustomEncoder, sort_keys=True)`.

```python
# Intermediate Example: Custom JSONEncoder subclass
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, "__dataclass_fields__"):
            return asdict(obj)
        return super().default(obj)
```

---

### 🔥 Senior Level ([`senior_json.py`](file:///home/monika/PycharmProjects/Devel/Python/json_tutorial/senior_json.py))
Focuses on custom `JSONDecoder` `object_hook` transformations into domain classes, NDJSON (JSON-Lines) streaming, and async file I/O:
- **Object Hook Deserialization**: `json.loads(json_str, object_hook=user_hook)`.
- **NDJSON Streaming**: Line-by-line streaming of newline-delimited JSON files.
- **Async JSON I/O**: Non-blocking `asyncio` file reading.

```python
# Senior Example: object_hook transformation callback
def user_object_hook(dct: dict) -> Any:
    if "username" in dct and "role" in dct:
        return UserRecord(username=dct["username"], role=dct["role"])
    return dct

user_instance = json.loads(raw_json, object_hook=user_object_hook)
```

---

## 📁 Directory Structure & Module Overview

```text
json_tutorial/
├── README.md                # Master documentation and multi-tier guide
├── test_json_tutorial.py    # Multi-tier unit test suite
├── json_processor.py        # Core JSONProcessor utility wrapper class
├── beginner_json.py         # Beginner tier (loads, dumps, load, dump)
├── intermediate_json.py     # Intermediate tier (dataclasses & custom JSONEncoder)
├── senior_json.py           # Senior tier (object_hook, NDJSON streaming, async)
├── example.py               # Legacy wrapper script
├── read_json.py             # Legacy wrapper script
├── read_stack_to_json.py    # Legacy wrapper script
├── sample.py                # Legacy wrapper script
├── data_1.txt               # Sample JSON data file
├── stack.json               # Sample stack trace JSON file
└── stack.txt                # Sample text file
```

| File Name | Developer Tier | Key Concepts & Functions |
| :--- | :--- | :--- |
| `beginner_json.py` | 🌱 Beginner | `json.loads()`, `json.dumps()`, `json.load()`, `json.dump()` |
| `intermediate_json.py` | 🚀 Intermediate | `json.JSONEncoder` subclassing, `@dataclass`, `datetime` ISO |
| `senior_json.py` | 🔥 Senior | `object_hook`, NDJSON stream parsing, `asyncio` file reading |
| `json_processor.py` | All Tiers | `JSONProcessor.parse_string()`, `JSONProcessor.serialize_object()` |
| `test_json_tutorial.py` | All Tiers | `unittest` suite testing string/file loads, dumps, and hooks |

---

## 🚀 How to Run the Code

```bash
# Run core JSON processor
python3 json_tutorial/json_processor.py

# Run beginner tier examples
python3 json_tutorial/beginner_json.py

# Run intermediate tier examples
python3 json_tutorial/intermediate_json.py

# Run senior tier examples
python3 json_tutorial/senior_json.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_json_tutorial.py

# Run with pytest from repository root
pytest json_tutorial/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | JSON Engine Evolution | Syntax & System Behavior | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | `json` standard module introduced | Replaced third-party `simplejson` library; `dict.iteritems()` iteration. | `json.loads()` produced unicode strings `u'value'`. |
| **Python 3.6** | Preserved dict insertion order | JSON objects encode and decode with key order preservation. | Dictionary key order was arbitrary in Python 2.7. |
| **Python 3.8** | Binary JSON loads support | `json.loads()` accepts `bytes` and `bytearray` buffers directly. | Required manual UTF-8 decoding `json.loads(b_data.decode('utf-8'))`. |
| **Python 3.9** | Decoder performance optimization | Accelerated `json.decoder` C implementation. | Reduced string allocation overhead during large JSON parses. |
| **Python 3.11**| C-accelerated JSON parser (`_json`) | Faster C extension parsing for large floating-point arrays. | Significant parsing speed improvements over Python 3.6-3.10. |
| **Python 3.13**| Free-threaded GIL-free CPython | High-throughput concurrent JSON encoding/decoding. | Thread-safe parallel JSON deserialization without GIL locks. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Paging or chunking large JSON datasets frequently uses `range()` sequence objects:

```python
# Chunking a list of 100 JSON records into batches of 10 using range()
json_records = [{"id": i} for i in range(100)]
batch_size = 10

for i in range(0, len(json_records), batch_size):
    batch = json_records[i : i + batch_size]
    print(f"Batch {i // batch_size + 1}: {len(batch)} items")
```

### Range Performance & Memory Notes
1. **Python 2.7 vs Python 3.x**:
   - In Python 2.7, `range(1_000_000)` constructed an eager list of 1,000,000 integer objects in RAM (~8 MB).
   - In Python 3.0+, `xrange()` was removed, and `range()` became an immutable sequence object operating with constant $O(1)$ memory (48 bytes).
2. **$O(1)$ Containment Testing**:
   - Evaluating sequence containment `500 in range(0, 1000, 5)` computes in constant-time arithmetic evaluation without allocating memory arrays.

### Attributes and Methods Inspection (`dir(range)`)

Inspecting `dir(range)` shows standard sequence methods:

```python
r = range(0, 10, 2)
print(r.start)  # Output: 0
print(r.stop)   # Output: 10
print(r.step)   # Output: 2

print(r.index(6))  # Output: 3
print(r.count(4))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Range sequence boundaries.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
