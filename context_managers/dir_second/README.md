# Dir-Second Subfolder Tutorial Module

Welcome to the **Dir-Second Subfolder Tutorial Module** inside `context_managers/dir_second`. This directory provides an isolated, subfolder-specific demonstration of multi-resource context managers (`ExitStack`), class-based context managers (`DirSecondResourceHandler`), and generator-based context managers (`@contextmanager`).

---

## 📁 Subfolder Directory Structure

```text
context_managers/dir_second/
├── README.md                      # Comprehensive pedagogical guide for dir_second
├── dir_second_context_manager.py  # Multi-resource context managers & stream safety
├── test_b.txt                     # Sample log file B for batch processing
├── test_c.txt                     # Sample log file C for multi-file ExitStack
└── test_dir_second.py             # Unit test suite verifying context safety
```

---

## 🚀 Key Context Manager Implementations

### 1. Multi-Resource Management (`contextlib.ExitStack`)
Manages a variable number of context managers dynamically, ensuring all resources are safely opened and cleaned up upon exit even if one throws an exception.

```python
from contextlib import ExitStack
from pathlib import Path

def read_multiple_dir_second_files(filenames: list[str]) -> list[list[str]]:
    dir_path = Path(__file__).resolve().parent
    results = []

    with ExitStack() as stack:
        handles = [
            stack.enter_context(open(dir_path / name, "r", encoding="utf-8"))
            for name in filenames if (dir_path / name).exists()
        ]
        for h in handles:
            results.append([line.rstrip("\n") for line in h])

    return results
```

### 2. Class-Based Context Manager (`DirSecondResourceHandler`)
Implements `__enter__()` and `__exit__()` dunder methods for deterministic cleanup and custom exception handling.

```python
from pathlib import Path
from typing import Optional, TextIO, Type

class DirSecondResourceHandler:
    def __init__(self, filename: str, mode: str = "r") -> None:
        self.filepath = Path(__file__).resolve().parent / filename
        self.mode = mode
        self.file_handle: Optional[TextIO] = None

    def __enter__(self) -> Optional[TextIO]:
        try:
            self.file_handle = open(self.filepath, self.mode, encoding="utf-8")
            return self.file_handle
        except FileNotFoundError:
            return None

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Any) -> bool:
        if self.file_handle and not self.file_handle.closed:
            self.file_handle.close()
        if exc_type is FileNotFoundError:
            return True  # Suppress missing file exception
        return False
```

### 3. Generator Context Manager (`@contextmanager`)
Converts a generator with `try ... yield ... finally` into a lightweight context manager.

```python
from contextlib import contextmanager
from pathlib import Path
from typing import Generator, Optional, TextIO

@contextmanager
def managed_dir_second_file(filename: str, mode: str = "r") -> Generator[Optional[TextIO], None, None]:
    filepath = Path(__file__).resolve().parent / filename
    stream: Optional[TextIO] = None
    try:
        if filepath.exists():
            stream = open(filepath, mode, encoding="utf-8")
        yield stream
    finally:
        if stream and not stream.closed:
            stream.close()
```

---

## 🐍 Python Version Evolution (Python 2.7 to Python 3.13)

| Feature / Version | Python 2.7 (Legacy) | Python 3.3 | Python 3.7 - 3.10 | Python 3.11 - 3.13 |
| :--- | :--- | :--- | :--- | :--- |
| **Multi-Resource Context** | `contextlib.nested()` (Deprecated/Flawed) | `contextlib.ExitStack` introduced | `ExitStack` standard for dynamic contexts | `AsyncExitStack` & `TaskGroup` enhancements |
| **Directory Context** | Manual `os.chdir()` with `try...finally` | Custom `@contextmanager` wrapper | Custom `@contextmanager` wrapper | `contextlib.chdir()` added in 3.11 |
| **Type Hints** | Not supported (Comments only) | Not supported | Standard PEP 484 annotations | Enhanced generics (`ParamSpec`, `Self`) |
| **File Encoding** | `io.open()` required for UTF-8 | `open(..., encoding="utf-8")` | Default `utf-8` in many environments | Enhanced encoding validation |
| **Exception Groups** | N/A | N/A | N/A | `ExceptionGroup` handled seamlessly in `ExitStack` |

### Legacy Python 2.7 Comparison
In Python 2.7, dynamic multi-resource handling relied on `contextlib.nested()`, which had a flaw: if an exception occurred during resource setup, previously opened resources were not guaranteed to be closed properly. Python 3.3 introduced `contextlib.ExitStack`, which guarantees clean teardown of all entered contexts even if setup fails midway.

---

## 🧪 Running Unit Tests

Run the unit test suite for `dir_second` from the root repository directory:

```bash
python3 -m unittest discover -s context_managers/dir_second -p "test_*.py"
```

Or execute directly within `dir_second`:

```bash
cd context_managers/dir_second
python3 test_dir_second.py
```
