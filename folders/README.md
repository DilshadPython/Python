# Directory & Folder Management Operations in Python

A comprehensive, production-grade Python reference suite demonstrating directory creation, inspection/scanning, metadata management, deletion, and temporary folder lifecycle using the Python Standard Library (`os`, `shutil`, `tempfile`, and `pathlib.Path`).

---

## What is New

This directory has been completely refactored and expanded from 2 simple scripts (`create_folder.py`, `create_new_folder.py`) into a structured, PEP 8-compliant 5-tier architecture:

1. **`create_directory_ops.py`**: Safe single and multi-level directory creation (`os.mkdir`, `os.makedirs`, `Path.mkdir`).
2. **`scan_directory_ops.py`**: Efficient directory listings, file metadata retrieval, recursive tree walking, and globbing (`os.listdir`, `os.scandir`, `os.walk`, `Path.glob`).
3. **`manage_directory_ops.py`**: Directory renaming (`Path.rename`), moving (`shutil.move`), and cumulative folder size calculation.
4. **`remove_directory_ops.py`**: Safe empty folder deletion (`Path.rmdir`) and recursive directory tree removal (`shutil.rmtree`).
5. **`temp_directory_ops.py`**: Auto-cleaning temporary directories (`tempfile.TemporaryDirectory`) and explicit temp directory creation (`tempfile.mkdtemp`).
6. **`test_folders.py`**: Automated unittest test suite validating all 5 directory operation modules.

---

## Standard Library Modules Used

- **`os`**: Standard operating system interface for POSIX and Windows directory manipulations (`mkdir`, `makedirs`, `listdir`, `scandir`, `walk`, `rmdir`).
- **`pathlib.Path`**: Object-oriented filesystem path abstraction providing clean syntax for directory operations (`mkdir`, `rename`, `rmdir`, `glob`, `rglob`).
- **`shutil`**: High-level file and directory operations for moving (`move`) and recursive deletion (`rmtree`).
- **`tempfile`**: Secure temporary directory generation (`TemporaryDirectory`, `mkdtemp`).

---

## Detailed Methods & Attributes Reference

### 1. Directory Creation Methods

#### `os.mkdir(path, mode=0o777)`
Creates a single directory at the specified path. Raises `FileExistsError` if the directory already exists.

```python
import os

os.mkdir("new_folder")
```

#### `os.makedirs(name, mode=0o777, exist_ok=False)`
Recursively creates nested directory trees. When `exist_ok=True`, suppresses `FileExistsError` if the target directory exists.

```python
import os

os.makedirs("parent/child/grandchild", exist_ok=True)
```

#### `pathlib.Path.mkdir(mode=0o777, parents=False, exist_ok=False)`
Object-oriented method to create directories. Set `parents=True` for nested directory trees and `exist_ok=True` for safe re-runs.

```python
from pathlib import Path

Path("parent/child").mkdir(parents=True, exist_ok=True)
```

---

### 2. Directory Scanning & Traversal Methods

#### `os.listdir(path='.')`
Returns a list of entry names (files and directories) contained in the specified directory.

```python
import os

entries = os.listdir(".")
print(entries)
```

#### `os.scandir(path='.')`
Yields `DirEntry` objects providing file attributes without requiring extra system calls. Efficient for large directory structures.

**Attributes & Methods on `DirEntry`**:
- `.name`: Base entry name.
- `.path`: Full entry path string.
- `.is_dir()`: Returns `True` if entry is a directory.
- `.is_file()`: Returns `True` if entry is a file.
- `.stat()`: Returns `os.stat_result` (contains `.st_size`, `.st_mtime`).

```python
import os

with os.scandir(".") as entries:
    for entry in entries:
        print(f"Name: {entry.name}, Is Dir: {entry.is_dir()}")
```

#### `os.walk(top, topdown=True, onerror=None, followlinks=False)`
Generates file names in a directory tree by walking either top-down or bottom-up. Yields 3-tuples: `(dirpath, dirnames, filenames)`.

```python
import os

for root, dirs, files in os.walk("."):
    print(f"Directory: {root} | Subfolders: {len(dirs)} | Files: {len(files)}")
```

#### `pathlib.Path.glob(pattern)` / `Path.rglob(pattern)`
Iterates over directory entries matching `pattern`. `rglob(pattern)` is equivalent to `glob("**/" + pattern)`.

```python
from pathlib import Path

# Non-recursive match
py_files = list(Path(".").glob("*.py"))

# Recursive match
all_py_files = list(Path(".").rglob("*.py"))
```

---

### 3. Directory Management Methods

#### `pathlib.Path.rename(target)` / `os.rename(src, dst)`
Renames a directory to `target`. Raises `FileNotFoundError` if source does not exist.

```python
from pathlib import Path

src = Path("old_name")
dest = Path("new_name")
src.rename(dest)
```

#### `shutil.move(src, dst)`
Recursively moves a directory or file to another destination, cross-filesystem compatible.

```python
import shutil

shutil.move("folder_a", "destination_folder/folder_a")
```

#### `os.walk` + `Path.stat().st_size` (Directory Size Calculation)
Computes cumulative size of all contained files in a directory tree.

```python
import os
from pathlib import Path

def get_directory_size(path: Path) -> int:
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            total += (Path(root) / f).stat().st_size
    return total
```

---

### 4. Directory Removal Methods

#### `pathlib.Path.rmdir()` / `os.rmdir(path)`
Removes an empty directory. Raises `OSError` (Directory not empty) if files or subdirectories remain inside.

```python
from pathlib import Path

Path("empty_folder").rmdir()
```

#### `shutil.rmtree(path, ignore_errors=False, onerror=None)`
Deletes an entire directory tree recursively, removing all contained files and subdirectories.

```python
import shutil

shutil.rmtree("non_empty_folder")
```

---

### 5. Temporary Directory Methods

#### `tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)`
Context manager creating a temporary directory. Automatically cleans up directory and contents upon exiting the `with` block.

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory(prefix="app_") as temp_dir:
    temp_path = Path(temp_dir)
    (temp_path / "temp.txt").write_text("Data")
# Auto-deleted here
```

#### `tempfile.mkdtemp(suffix=None, prefix=None, dir=None)`
Creates a temporary directory requiring explicit deletion via `shutil.rmtree`.

```python
import shutil
import tempfile

temp_path = tempfile.mkdtemp(prefix="manual_")
# ... use directory ...
shutil.rmtree(temp_path)
```

---

## File Structure Matrix

| Module | Primary Standard Functions | Description |
| :--- | :--- | :--- |
| `create_directory_ops.py` | `os.mkdir`, `os.makedirs`, `Path.mkdir` | Demonstrates safe single & multi-level directory creation. |
| `scan_directory_ops.py` | `os.listdir`, `os.scandir`, `os.walk`, `Path.glob` | Scans directory contents, inspects metadata, and walks trees. |
| `manage_directory_ops.py` | `Path.rename`, `shutil.move`, `Path.stat` | Handles directory renaming, moving, and folder size calculations. |
| `remove_directory_ops.py` | `Path.rmdir`, `shutil.rmtree` | Demonstrates safe empty removal and recursive tree deletion. |
| `temp_directory_ops.py` | `tempfile.TemporaryDirectory`, `tempfile.mkdtemp` | Demonstrates managed and manual temporary directory handling. |
| `test_folders.py` | `unittest.TestCase` | Unit tests for all directory management functionality. |

---

## Running the Code & Unit Tests

### Run Individual Modules Directly

```bash
python3 create_directory_ops.py
python3 scan_directory_ops.py
python3 manage_directory_ops.py
python3 remove_directory_ops.py
python3 temp_directory_ops.py
```

### Run Unit Test Suite

```bash
python3 -m unittest test_folders.py
```

### Run Syntax Verification

```bash
python3 -m py_compile *.py
```
