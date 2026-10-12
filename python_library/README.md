# Object-Oriented Filesystem Path Operations Master Guide (`pathlib.Path`)

Welcome to the **Python `pathlib` Master Guide**, a production-grade educational reference detailing object-oriented path manipulation (`pathlib.Path`, PEP 428), replacing legacy string-based `os.path` operations, unit testing via `unittest`, and structured learning paths for **Beginner**, **Intermediate**, and **Senior** developers.

---

## 📌 Table of Contents

1. [Overview & Architectural Architecture](#-overview--architectural-architecture)
2. [Developer Tier Learning Roadmap](#-developer-tier-learning-roadmap)
   - [🌱 Beginner Level](#-beginner-level)
   - [🚀 Intermediate Level](#-intermediate-level)
   - [🔥 Senior Level](#-senior-level)
3. [Directory Structure & Module Overview](#-directory-structure--module-overview)
4. [Legacy `os.path` vs Modern `pathlib.Path` Syntax Comparison](#-legacy-ospath-vs-modern-pathlibpath-syntax-comparison)
5. [How to Run the Code](#-how-to-run-the-code)
6. [Running Unit Tests](#-running-unit-tests)
7. [Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)](#-python-33-to-313-version-evolution-matrix-with-python-27-context)
8. [Python `range()` Sequence Mechanics & Introspection (`dir(range)`)](#-python-range-sequence-mechanics--introspection-dirrange)

---

## 📁 Overview & Architectural Architecture

Introduced in **PEP 428 (Python 3.4)**, `pathlib` provides an object-oriented hierarchy representing filesystem paths for different operating systems (`PosixPath` and `WindowsPath`).

```text
               PurePath (Base)
               /          \
       PurePosixPath   PureWindowsPath
             |                |
         PosixPath       WindowsPath
```

---

## 🎓 Developer Tier Learning Roadmap

### 🌱 Beginner Level ([`beginner_pathlib.py`](file:///home/monika/PycharmProjects/Devel/Python/python_library/beginner_pathlib.py))
Focuses on basic `Path` object creation, path joining using the `/` operator, path status inspection, and text I/O methods:
- **Path Construction**: `p = Path("data") / "file.txt"`.
- **Status Inspection**: `p.exists()`, `p.is_file()`, `p.is_dir()`.
- **File Text I/O**: `p.write_text("hello")`, `content = p.read_text()`.

```python
# Beginner Example: Path joining and reading/writing text
data_dir = Path("data")
file_path = data_dir / "sample.txt"

file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.write_text("Hello, Pathlib!", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))
```

---

### 🚀 Intermediate Level ([`intermediate_pathlib.py`](file:///home/monika/PycharmProjects/Devel/Python/python_library/intermediate_pathlib.py))
Focuses on recursive glob search (`rglob`), path extension transformation (`with_suffix`), metadata inspection (`stat()`), and nested directory creation:
- **Recursive Globbing**: `for f in path.rglob("*.py"):`.
- **Extension Transformation**: `new_path = path.with_suffix(".pdf")`.
- **File Metadata Stats**: `stats = path.stat()` (`st_size`, `st_mtime`).

```python
# Intermediate Example: Recursive glob search and metadata stats
for py_file in Path(".").rglob("*.py"):
    size = py_file.stat().st_size
    print(f"File: {py_file}, Size: {size} bytes")
```

---

### 🔥 Senior Level ([`senior_pathlib.py`](file:///home/monika/PycharmProjects/Devel/Python/python_library/senior_pathlib.py))
Focuses on path traversal security sanitization (`.resolve()`, `is_relative_to`), non-blocking asynchronous file reading (`asyncio`), and generator pipeline path filtering:
- **Traversal Security**: Preventing `../../etc/passwd` escaping sandbox root.
- **Relative Path Bounds**: `target.relative_to(sandbox)` verification (PEP 619).
- **Generator Stream Pipeline**: Filtering file iteration streams dynamically.

```python
# Senior Example: Secure path traversal sanitization
def sanitize_user_path(sandbox: Path, user_str: str) -> Path:
    resolved_root = sandbox.resolve()
    target = (resolved_root / user_str).resolve()
    target.relative_to(resolved_root)  # Raises ValueError if outside sandbox
    return target
```

---

## 📁 Directory Structure & Module Overview

```text
python_library/
├── README.md                   # Master documentation and multi-tier guide
├── required.txt                # Dependency specification file
├── test_pathlib_tutorial.py    # Multi-tier unit test suite
├── pathlib_tutorial.py         # Core tutorial module
├── path_lib.py                 # Legacy wrapper script
├── beginner_pathlib.py         # Beginner tier (Path creation, /, read_text, write_text)
├── intermediate_pathlib.py     # Intermediate tier (rglob, with_suffix, stat)
└── senior_pathlib.py           # Senior tier (sanitization, is_relative_to, async)
```

| File Name | Developer Tier | Key Concepts & Functions |
| :--- | :--- | :--- |
| `beginner_pathlib.py` | 🌱 Beginner | `Path()`, `/` operator, `.exists()`, `.read_text()`, `.write_text()` |
| `intermediate_pathlib.py` | 🚀 Intermediate | `.rglob()`, `.with_suffix()`, `.stat()`, `st_size` |
| `senior_pathlib.py` | 🔥 Senior | `.resolve()`, `relative_to`, Directory Traversal Sanitization, `asyncio` |
| `pathlib_tutorial.py` | All Tiers | `decompose_path()`, `list_directory_contents()`, `get_current_directory_info()` |
| `test_pathlib_tutorial.py` | All Tiers | `unittest` suite covering all 3 developer tiers |

---

## 🔄 Legacy `os.path` vs Modern `pathlib.Path` Syntax Comparison

| Operation | Legacy `os.path` Syntax | Modern `pathlib.Path` Syntax |
| :--- | :--- | :--- |
| **Join Paths** | `os.path.join(dir, file)` | `Path(dir) / file` |
| **Get Absolute Path** | `os.path.abspath(path)` | `Path(path).resolve()` |
| **Get Parent Dir** | `os.path.dirname(path)` | `Path(path).parent` |
| **Get Filename** | `os.path.basename(path)` | `Path(path).name` |
| **Get Extension** | `os.path.splitext(path)[1]` | `Path(path).suffix` |
| **Check Exists** | `os.path.exists(path)` | `Path(path).exists()` |
| **Check File** | `os.path.isfile(path)` | `Path(path).is_file()` |
| **Create Dir** | `os.makedirs(path, exist_ok=True)` | `Path(path).mkdir(parents=True, exist_ok=True)` |
| **Read Text File** | `with open(p) as f: text = f.read()` | `text = Path(p).read_text()` |
| **Write Text File**| `with open(p, 'w') as f: f.write(t)` | `Path(p).write_text(t)` |

---

## 🚀 How to Run the Code

```bash
# Run core tutorial
python3 python_library/pathlib_tutorial.py

# Run beginner tier examples
python3 python_library/beginner_pathlib.py

# Run intermediate tier examples
python3 python_library/intermediate_pathlib.py

# Run senior tier examples
python3 python_library/senior_pathlib.py
```

---

## 🧪 Running Unit Tests

Execute unit tests via `unittest` or `pytest`:

```bash
# Run unittest suite directly
python3 -m unittest test_pathlib_tutorial.py

# Run with pytest from repository root
pytest python_library/
```

---

## ⚡ Python 3.3 to 3.13 Version Evolution Matrix (with Python 2.7 Context)

| Python Version | `pathlib` Evolution | Syntax & System Behavior | Python 2.7 Context Comparison |
| :--- | :--- | :--- | :--- |
| **Python 2.7** | No standard `pathlib` module | Manipulated paths using raw string operations (`os.path`). | Backport `pathlib2` required third-party installation via PyPI. |
| **Python 3.4** | Introduced `pathlib` (PEP 428) | Added `Path`, `PosixPath`, `WindowsPath` classes. | Object-oriented path navigation introduced to standard library. |
| **Python 3.6** | File system path protocol (PEP 519) | Functions like `open(Path(...))` accept Path objects natively. | Previously required explicit conversion `open(str(path_obj))`. |
| **Python 3.8** | Added `unlink(missing_ok=True)` | Simplified file deletion without catching `FileNotFoundError`. | Handled via explicit `if path.exists(): path.unlink()` in 3.4-3.7. |
| **Python 3.9** | Added `readlink()`, `is_relative_to()` | `path.is_relative_to(other)` returns boolean relative path check. | Exception handling `try: path.relative_to(other) except ValueError:`. |
| **Python 3.10**| Improved `with_stem()` method | `path.with_stem("new_name")` changes stem without losing extension. | Manual `path.with_name(f"new_name{path.suffix}")` in 3.4-3.9. |
| **Python 3.11**| `Path.glob()` recursive star-star support | `**` glob pattern matching syntax enhancements. | Improved symlink traversal options in directory searches. |
| **Python 3.12**| `Path.walk()` directory tree generator | `Path.walk()` yields `(dirpath, dirnames, filenames)` (PEP 680). | Replaced legacy `os.walk()` with native `Path` instances. |
| **Python 3.13**| Free-threaded GIL-free CPython | High-throughput concurrent file system operations. | Thread-safe `Path` operations across GIL-free worker threads. |

---

## 🔢 Python `range()` Sequence Mechanics & Introspection (`dir(range)`)

Batch processing directory files frequently utilizes `range()` sequence objects:

```python
# Batch processing 50 files at a time using range()
files = list(Path(".").glob("*.py"))
batch_size = 10

for i in range(0, len(files), batch_size):
    chunk = files[i : i + batch_size]
    print(f"Processing Batch {i // batch_size + 1}: {[f.name for f in chunk]}")
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
r = range(0, 100, 10)
print(r.start)  # Output: 0
print(r.stop)   # Output: 100
print(r.step)   # Output: 10

print(r.index(30))  # Output: 3
print(r.count(50))  # Output: 1
```

Public methods returned by `dir(range)`:
- **`start`**, **`stop`**, **`step`**: Range sequence boundaries.
- **`index(x)`**: Returns index of element $x$ in range ($O(1)$ calculation).
- **`count(x)`**: Returns count of occurrences of $x$ (0 or 1).
- **`__contains__(x)`**: Evaluates membership `x in range` in $O(1)$ time.
