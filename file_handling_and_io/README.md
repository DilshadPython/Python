# 📁 File Handling & I/O (`file_handling_and_io`) Pedagogical Module

Welcome to the **`file_handling_and_io` Pedagogical Module**. This module provides a complete reference architecture for mastering Python file handling, text modes (`r`, `w`, `a`, `x`), binary modes (`rb`, `wb`), chunked buffer stream copying, structured CSV operations (`csv.reader`, `csv.DictReader`), financial stock analysis (`google.csv`), regex pattern filtering, temporary file management (`tempfile`), and `pathlib.Path` metadata inspection.

---

## 📂 Module Architecture

```
file_handling_and_io/
├── text_file_operations.py      # Text file modes ('r', 'w', 'a', 'x'), line streaming, seek() & tell()
├── binary_file_operations.py    # Binary file I/O ('rb', 'wb'), chunked stream copying, & magic number inspection
├── csv_file_operations.py       # Structured CSV parsing, lambda sorting, & google.csv stock analysis
├── file_search_and_filter.py    # Keyword search, email extraction (re.findall), & word counting
├── temp_and_file_system.py      # Auto-cleaning temporary files (tempfile) & pathlib.Path metadata
├── test_file_handling_and_io.py # Unittest suite validating all 5 File I/O modules & datasets
├── requirements.txt             # Dependency specification (Standard library footprint)
├── README.md                    # Module documentation and usage guide
├── walkthrough.md               # Detailed walkthrough documentation
│
└── Data Assets:
    ├── cities.txt               # Sample text dataset of international city names
    ├── appendfile.txt           # Sample text dataset for appending operations
    ├── dict_city.csv            # Sample CSV dataset mapping cities and UK counties
    ├── emailList.txt            # Sample email dataset for regex search
    ├── email_from.txt           # Sample email header log dataset for regex parsing
    └── google.csv               # Historical Google stock market CSV dataset (2014-2015)
```

---

## 🌟 What is New in This Module Update

1. **Dataset Integration & Real-World Analysis**: Aligned code modules to directly parse and analyze real data assets including `google.csv` (stock market volume and prices), `dict_city.csv`, `emailList.txt`, and `cities.txt`.
2. **Standardized Python Naming**: All module filenames are valid Python identifiers enabling clean imports (`from file_handling_and_io.text_file_operations import ...`).
3. **Chunked Binary Stream Processing**: Added memory-efficient byte copying for binary assets using fixed 4KB buffer chunks.
4. **PEP 8 Compliance & Type Annotations**: Modernized code with standard Pythonic conventions, complete type hints (`List`, `Dict`, `Tuple`, `Optional`), docstrings, and `if __name__ == "__main__":` entry points.
5. **Comprehensive Unittest Suite**: Introduced `test_file_handling_and_io.py` covering text, binary, CSV, stock dataset analysis, regex email search, and temporary file operations using Python's `unittest` framework.

---

## 🔑 File Opening Modes & Methods Reference

### 1. Standard File Opening Modes

| Mode | Operation | Description |
| :--- | :--- | :--- |
| **`'r'`** | Read *(Default)* | Opens file for reading. Raises `FileNotFoundError` if path does not exist. |
| **`'w'`** | Write | Opens file for writing. Overwrites existing content or creates a new file. |
| **`'a'`** | Append | Opens file for appending. Preserves existing content and writes at end of file. |
| **`'x'`** | Exclusive Create | Creates a new file. Raises `FileExistsError` if target file already exists. |
| **`'r+'`** | Read / Write | Opens file for both reading and writing. Pointer starts at offset 0. |
| **`'b'`** | Binary Mode | Appended to mode string (e.g. `'rb'`, `'wb'`) for raw byte buffer operations. |
| **`'t'`** | Text Mode *(Default)* | Appended to mode string (e.g. `'rt'`, `'wt'`) with automatic string encoding/decoding. |

---

### 2. File Object Methods

- **`f.read(size=-1)`**: Reads up to `size` characters/bytes (or entire file if size omitted).
- **`f.readline()`**: Reads a single line ending with `\n`. Returns empty string `""` at EOF.
- **`f.readlines()`**: Reads all remaining lines into a `List[str]`.
- **`f.write(string_or_bytes)`**: Writes data to file buffer and returns character/byte count.
- **`f.writelines(list_of_strings)`**: Writes a list of strings to the file without adding automatic newlines.
- **`f.tell()`**: Returns current integer byte/character offset of the file pointer.
- **`f.seek(offset, whence=0)`**: Moves file pointer to specified `offset` relative to `whence` (0=start, 1=current, 2=end).
- **`f.flush()`**: Flushes internal memory write buffer to disk without closing file handle.

---

## 🔍 Modules & Code Examples Reference

### 1. `text_file_operations.py` — Text File Handling

```python
from file_handling_and_io.text_file_operations import (
    write_lines_to_file,
    append_line_to_file,
    read_file_lines,
    demonstrate_seek_and_tell,
)

# Write, append, read, and inspect pointer offset
write_lines_to_file("cities.txt", ["Tokyo", "London"])
append_line_to_file("cities.txt", "Paris")
lines = read_file_lines("cities.txt")
```

---

### 2. `binary_file_operations.py` — Raw Byte & Chunked Stream Operations

```python
from file_handling_and_io.binary_file_operations import (
    write_binary_data,
    copy_binary_file_chunked,
    inspect_binary_header,
)

# Chunked binary file copy (4KB buffer chunks)
bytes_copied = copy_binary_file_chunked("src.png", "dest.png", chunk_size=4096)

# Inspect magic number header
raw_bytes, hex_string = inspect_binary_header("src.png", num_bytes=4)
# hex_string -> '89 50 4E 47' (PNG Magic Number)
```

---

### 3. `csv_file_operations.py` — Structured CSV & Stock Dataset Analysis

```python
from file_handling_and_io.csv_file_operations import (
    write_csv_rows,
    read_csv_dict,
    analyze_google_stock_csv,
    sort_csv_records_by_field,
)

# Analyze google.csv historical stock metrics
metrics = analyze_google_stock_csv("google.csv")
print("Total trading days:", metrics["total_days"])
print("Max closing price:", metrics["max_close"])
```

---

### 4. `file_search_and_filter.py` — Line Search & Regex Extraction

```python
from file_handling_and_io.file_search_and_filter import (
    search_keyword_in_file,
    extract_emails_from_file,
    count_words_in_file,
)

# Extract unique emails using regex from emailList.txt
emails = extract_emails_from_file("emailList.txt")
```

---

### 5. `temp_and_file_system.py` — Temporary Files & Path Metadata

```python
from file_handling_and_io.temp_and_file_system import (
    create_temporary_file_demo,
    inspect_file_metadata,
)

# Inspect path metadata
meta = inspect_file_metadata("cities.txt")
print(meta["size_bytes"], meta["suffix"])
```

---

## 🚀 Execution & Testing Guide

### 1. Run Individual Demonstration Scripts

Execute any script directly using `python3`:

```bash
python3 file_handling_and_io/text_file_operations.py
python3 file_handling_and_io/binary_file_operations.py
python3 file_handling_and_io/csv_file_operations.py
python3 file_handling_and_io/file_search_and_filter.py
python3 file_handling_and_io/temp_and_file_system.py
```

### 2. Run the Unittest Suite

Execute the complete test suite:

```bash
python3 -m unittest file_handling_and_io/test_file_handling_and_io.py
```

Or using `pytest`:

```bash
pytest file_handling_and_io/test_file_handling_and_io.py
```
