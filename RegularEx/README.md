# Python Regular Expressions (`re`) Master Module

Welcome to the **Python Regular Expressions (`re`) Master Module**, a standardized, production-grade educational and technical reference for understanding pattern matching, text search, regex substitution, string formatting, capturing groups, lookaround assertions, and version evolution across Python 2.7 to Python 3.13.

---

## Directory Structure & Module Catalog

```text
RegularEx/
├── README.md                     # Overview, execution guide, file catalog, & syntax cheatsheet
├── docs.md                       # Technical reference detailing engine mechanics, PEPs, & version changes
├── email_validator.py            # Email validation using regex character sets, TLD matching, & re.IGNORECASE
├── name_formatter.py             # Name reformatting ("Last, First" -> "First Last") via split, groups, & re.sub
├── social_username_extractor.py  # Handle extraction from URLs using str.removeprefix(), re.sub(), & re.search()
├── url_extractor.py              # Scanning multi-line text for URLs via re.findall(), re.finditer(), & re.sub()
├── regex_iterators.py            # Compiling patterns, searching phone numbers/titles, & external file scanning
├── regex_advanced.py             # Verbose regex (re.VERBOSE), named groups, lookaround assertions, & dir()
├── test_regular_ex.py            # Comprehensive unittest test suite (10 test cases)
├── data/
│   └── REeX.txt                  # Sample dataset for file searching tests
└── [legacy wrappers]             # Backward-compatible refactored entry points (valid_email.py, format.py, etc.)
```

---

## Module Summaries

### 1. `email_validator.py`
Provides robust email validation rules matching usernames, domains, subdomains, and top-level domain extensions (`.com`, `.net`, `.co.uk`). Demonstrates `re.compile()` and `re.fullmatch()`.

### 2. `name_formatter.py`
Demonstrates string reformatting patterns ("Last, First" $\rightarrow$ "First Last") comparing standard `str.split()`, `re.search()` capturing groups, Python 3.8+ walrus operator (`:=`), and `re.sub()` backreferences.

### 3. `social_username_extractor.py`
Parses profile URLs to extract handles using `str.removeprefix()` (Python 3.9+), `re.sub()` domain stripping, and `re.search()` with non-capturing groups `(?:...)`.

### 4. `url_extractor.py`
Scans multi-line texts for web URLs, extracting domain components using `re.findall()` and `re.finditer()`, and replacing URLs with clean domain names via `re.sub()`.

### 5. `regex_iterators.py`
Demonstrates compiling patterns, searching formatted phone numbers, title names (e.g. `Mr Smith`, `Mrs Trump`), negative character sets (`[^b]at`), and scanning external data files (`data/REeX.txt`).

### 6. `regex_advanced.py`
Demonstrates advanced regex features including verbose mode (`re.VERBOSE`), named capturing groups (`(?P<name>...)`), positive/negative lookahead and lookbehind assertions (`(?=...)`, `(?<=...)`), and object introspection via `dir()`.

### 7. `test_regular_ex.py`
A complete `unittest` test suite verifying all module functions, edge cases, pattern matches, and introspection behavior.

---

## Regex Syntax Quick Reference

| Syntax | Description | Example Match |
| :--- | :--- | :--- |
| `.` | Any character except newline | `a.c` matches `abc`, `a1c` |
| `\d` / `\D` | Digit (0-9) / Non-digit | `\d{3}` matches `123` |
| `\w` / `\W` | Word character (`[a-zA-Z0-9_]`) / Non-word | `\w+` matches `user_1` |
| `\s` / `\S` | Whitespace (space, tab, newline) / Non-whitespace | `\s+` matches spaces |
| `^` / `$` | Start of string / End of string | `^hello$` |
| `[...]` / `[^...]` | Character set / Complement (negated) set | `[^b]at` matches `cat`, not `bat` |
| `*` / `+` / `?` | 0 or more / 1 or more / 0 or 1 repetition | `colou?r` matches `color`, `colour` |
| `{m,n}` | Between `m` and `n` repetitions | `\d{3,4}` matches 3 or 4 digits |
| `(...)` | Capturing group | `(\w+)@(\w+)` |
| `(?:...)` | Non-capturing group | `(?:www\.)?google\.com` |
| `(?P<name>...)` | Named capturing group | `(?P<id>\d+)` |
| `(?=...)` / `(?<=...)` | Positive lookahead / Positive lookbehind | `\d+(?=\$)"` matches `50` in `50$` |

---

## How to Run the Code

### Running Individual Python Modules

```bash
# Email validation demonstration
python3 email_validator.py

# Name reformatting demonstration
python3 name_formatter.py

# Username extraction demonstration
python3 social_username_extractor.py

# URL parsing and extraction
python3 url_extractor.py

# Regex searching and file scanning
python3 regex_iterators.py

# Advanced regex flags, assertions, and dir() introspection
python3 regex_advanced.py
```

### Running the Unit Test Suite

Execute the `unittest` framework from the terminal:

```bash
python3 -m unittest test_regular_ex.py
```

Or run with verbose output:

```bash
python3 -m unittest -v test_regular_ex.py
```

---

## Summary of Python Version Evolution (`re` Module)

| Feature / Behavior | Python 2.7 | Python 3.3 - 3.10 | Python 3.11 - 3.13 |
| :--- | :--- | :--- | :--- |
| **Unicode Support** | Byte vs Unicode flag (`re.UNICODE`) | Default matching is Unicode-aware (`\w` matches Unicode words) | Enhanced Unicode 15.0+ regex properties |
| **Walrus Assignment (`:=`)** | Not supported | Supported in Python 3.8+ (`if m := re.search(...)`) | Fully supported |
| **`str.removeprefix()`** | Not available (used `re.sub` or slicing) | Introduced in Python 3.9 | Standard string method |
| **Atomic Grouping (`(?>...)`)** | Not supported | Introduced in Python 3.11 (`(?>...)` & possessive quantifiers `*+`, `++`) | Optimized matching engine |
