# 🐍 Comprehensive Python Regular Expressions (`re`) Master Guide

Welcome to the definitive pedagogical guide on **Python Regular Expressions (`re`)**. This document provides an end-to-end learning path—from initial concepts and string matching mechanics to advanced lookaround assertions, regex performance engineering, and version-specific CPython behaviors (Python 2.7 through Python 3.13).

---

## 📌 Table of Contents
1. [Introduction to Regular Expressions & When to Use Them](#1-introduction-to-regular-expressions--when-to-use-them)
2. [The Python `re` Standard Library Module](#2-the-python-re-standard-library-module)
3. [Core `re` API Methods & Functions](#3-core-re-api-methods--functions)
4. [Match Objects & Inspection Methods](#4-match-objects--inspection-methods)
5. [Raw Strings (`r"..."`) & Escaping (`re.escape`)](#5-raw-strings-r-and-escaping-reescape)
6. [Character Classes, Metacharacters & Special Sequences](#6-character-classes-metacharacters--special-sequences)
7. [Quantifiers: Greedy vs. Non-Greedy (Lazy) Matching](#7-quantifiers-greedy-vs-non-greedy-lazy-matching)
8. [Anchors & Boundaries](#8-anchors--boundaries)
9. [Grouping Mechanics: Capturing, Non-Capturing & Named Groups](#9-grouping-mechanics-capturing-non-capturing--named-groups)
10. [Backreferences & Pattern Reuse](#10-backreferences--pattern-reuse)
11. [Compilation Flags (`re.IGNORECASE`, `re.VERBOSE`, etc.)](#11-compilation-flags-reignorecase-reverbose-etc)
12. [Lookahead and Lookbehind Assertions](#12-lookahead-and-lookbehind-assertions)
13. [Unicode vs. ASCII Behavior Across Python Versions](#13-unicode-vs-ascii-behavior-across-python-versions)
14. [10 Comprehensive Practical Examples](#14-10-comprehensive-practical-examples)
15. [Common Mistakes & Catastrophic Backtracking](#15-common-mistakes--catastrophic-backtracking)
16. [When NOT to Use Regex: String Methods vs. Regex](#16-when-not-to-use-regex-string-methods-vs-regex)

---

## 1. Introduction to Regular Expressions & When to Use Them

### What is a Regular Expression?
A **Regular Expression** (commonly shortened to **regex** or **regexp**) is a sequence of characters defining a search pattern. In CPython, regular expressions are compiled into C-level bytecode instructions executed by an internal deterministic finite state machine (DFA) / non-deterministic finite state machine (NFA) engine.

### When Should You Use Regular Expressions?
- **Complex Pattern Matching**: Searching for text matching non-literal structures (e.g., IP addresses, ISO dates, phone numbers).
- **Structural Text Validation**: Verifying that user input strictly follows a formatted schema (e.g., email addresses, credit card numbers, passwords).
- **Advanced Text Extraction**: Extracting specific values from log files, HTML attributes, or semi-structured data payloads.
- **Bulk Sanitization & Reformatting**: Complex search-and-replace operations with backreferences (e.g., converting `"Last, First"` names to `"First Last"`).

---

## 2. The Python `re` Standard Library Module

Python provides built-in support for regular expressions via the **`re`** standard library module. No external installation is required.

```python
import re
```

The `re` module caches compiled patterns automatically (up to `re._MAXCACHE`, typically 512 patterns in CPython), but explicit compilation via `re.compile()` is recommended for performance-critical or repeated operations.

---

## 3. Core `re` API Methods & Functions

| Function API | Search Scope | Return Value | Primary Use Case |
| :--- | :--- | :--- | :--- |
| **`re.search(pattern, string)`** | Scans entire string | First `Match` object or `None` | Finding substring match anywhere in target text |
| **`re.match(pattern, string)`** | Beginning of string only | `Match` object or `None` | Checking if string starts with a pattern |
| **`re.fullmatch(pattern, string)`** | Entire string exactly | `Match` object or `None` | Strict end-to-end string validation |
| **`re.findall(pattern, string)`** | Scans entire string | `List[str]` or `List[Tuple]` | Collecting all non-overlapping pattern matches |
| **`re.finditer(pattern, string)`** | Scans entire string | `Iterator[Match]` | Memory-efficient lazy iteration over matches |
| **`re.sub(pattern, repl, string)`** | Scans entire string | Modified `str` | Replacing matched patterns with string or callable |
| **`re.subn(pattern, repl, string)`** | Scans entire string | `Tuple[str, int]` | Replacing matches and returning `(new_string, num_subs)` |
| **`re.split(pattern, string)`** | Scans entire string | `List[str]` | Splitting strings by regex delimiter |
| **`re.compile(pattern, flags)`** | Pre-compilation | Compiled `Pattern` object | Reusable $O(1)$ bytecode pattern caching |
| **`re.escape(pattern)`** | Utility function | Escaped `str` | Escaping arbitrary strings with regex metacharacters |
| **`re.purge()`** | Cache utility | `None` | Flushing CPython internal regex cache (`re._MAXCACHE`) |

### Function API Examples

```python
import re

text = "Error code 404 at 2026-08-30 10:15:30. Warning code 500 at 10:16:00."

# 1. re.search: Find first match anywhere
match_search = re.search(r"\b\d{3}\b", text)
print(match_search.group())  # Output: '404'

# 2. re.match: Check start of string only
match_start = re.match(r"Error", text)
print(bool(match_start))     # Output: True

# 3. re.fullmatch: Strict end-to-end validation
is_exact = re.fullmatch(r"\d{3}", "404")
print(bool(is_exact))        # Output: True

# 4. re.findall: Return list of all matches
all_codes = re.findall(r"\b\d{3}\b", text)
print(all_codes)             # Output: ['404', '500']

# 5. re.finditer: Lazy iteration with match offsets
for m in re.finditer(r"\b\d{3}\b", text):
    print(f"Found {m.group()} at index range {m.span()}")

# 6. re.sub & re.subn: Replace matches with count
cleaned_text = re.sub(r"\b\d{3}\b", "[CODE]", text)
print(cleaned_text)          # Output: 'Error code [CODE] at 2026-08-30... Warning code [CODE]...'

new_str, count_made = re.subn(r"\b\d{3}\b", "[CODE]", text)
print(f"New Text: {new_str}, Total Replacements: {count_made}") # Output: 2 replacements

# 7. re.split: Split text by regex pattern
parts = re.split(r"\s*at\s*", text)
print(parts)                 # Output: ['Error code 404', '2026-08-30 10:15:30. Warning code 500', '10:16:00.']

# 8. re.compile & pos/endpos slice search: Reusable pattern object with slice bounds
pattern = re.compile(r"\b\d{3}\b")
# Scans text slice from character index 0 to 25 without string slicing copy overhead
slice_match = pattern.search(text, pos=0, endpos=25)
print(slice_match.group() if slice_match else None) # Output: '404'

# 9. re.escape: Safely escape user input containing regex special chars
user_input = "price is $49.99 (USD)"
safe_pattern = re.escape(user_input)
print(safe_pattern)          # Output: 'price\ is\ \$49\.99\ \(USD\)'

# 10. re.purge: Cache flush
re.purge()
```

---

## 4. Match Objects & Inspection Methods

When `re.search()`, `re.match()`, or `re.fullmatch()` succeeds, it returns a **`re.Match`** object containing metadata about the match.

### Key Match Object Attributes & Methods

```python
import re

text = "User alex_dev registered on 2026-08-30"
pattern = re.compile(r"User\s+(?P<user>\w+)\s+registered on\s+(?P<date>\d{4}-\d{2}-\d{2})")
match = pattern.search(text)

if match:
    # .group(0) or .group(): Entire matched string
    print(match.group(0))        # 'User alex_dev registered on 2026-08-30'
    
    # .group(1), .group(2): Positional capturing groups
    print(match.group(1))        # 'alex_dev'
    print(match.group(2))        # '2026-08-30'
    
    # .group('name'): Access named capturing groups
    print(match.group('user'))   # 'alex_dev'
    print(match.group('date'))   # '2026-08-30'
    
    # .groups(): Tuple of all positional capturing groups
    print(match.groups())        # ('alex_dev', '2026-08-30')
    
    # .groupdict(): Dictionary of all named capturing groups
    print(match.groupdict())     # {'user': 'alex_dev', 'date': '2026-08-30'}
    
    # match.expand(template): Template string expansion with backreferences
    print(match.expand(r"User: \g<user> (Joined: \g<date>)")) # 'User: alex_dev (Joined: 2026-08-30)'

    # pattern.groupindex: Mapping of group names to integer group indices
    print(pattern.groupindex)    # {'user': 1, 'date': 2}
    
    # .start(), .end(), .span(): Character index offsets
    print(match.start())         # 0
    print(match.end())           # 38
    print(match.span())          # (0, 38)
```

---

## 5. Raw Strings (`r"..."`) & Escaping (`re.escape`)

### Why Raw Strings Are Essential in Python Regex
In standard Python strings, the backslash `\` acts as an escape character (`\n` is newline, `\t` is tab, `\b` is backspace). Regular expressions also use backslashes for special sequences (`\b` is word boundary, `\d` is digit).

Without raw strings, you must double-escape every backslash (`"\\b\\d+\\b"`). By prefixing string literals with **`r"..."`**, Python disables string-level backslash processing:

```python
# WITHOUT raw string (confusing & error-prone):
pattern_bad = "\\b\\d{3}\\b"

# WITH raw string (clean & pythonic):
pattern_good = r"\b\d{3}\b"
```

---

## 6. Character Classes, Metacharacters & Special Sequences

### Basic Character Sets & Classes

| Metacharacter / Token | Description | Equivalent Character Set |
| :--- | :--- | :--- |
| **`.`** | Any character except newline (`\n`) | `[^\n]` (or any char with `re.DOTALL`) |
| **`\d`** | Any ASCII / Unicode digit | `[0-9]` |
| **`\D`** | Any non-digit character | `[^0-9]` |
| **`\w`** | Any word character (letters, digits, underscore) | `[a-zA-Z0-9_]` |
| **`\W`** | Any non-word character | `[^a-zA-Z0-9_]` |
| **`\s`** | Any whitespace character (space, tab, newline) | `[\t\n\r\f\v ]` |
| **`\S`** | Any non-whitespace character | `[^\t\n\r\f\v ]` |
| **`[abc]`** | Custom character set (matches 'a', 'b', or 'c') | Explicit set |
| **`[a-z]`** | Character range (lowercase 'a' through 'z') | Range set |
| **`[^abc]`** | Negated character set (matches any char EXCEPT 'a', 'b', 'c') | Inverted set |

```python
import re

text = "Item #A12 costs $49"

print(re.findall(r"\d+", text))       # Output: ['12', '49']
print(re.findall(r"\w+", text))       # Output: ['Item', 'A12', 'costs', '49']
print(re.findall(r"[A-Z]", text))     # Output: ['I', 'A']
print(re.findall(r"[^a-zA-Z0-9\s]", text)) # Output: ['#', '$'] (Special punctuation)
```

---

## 7. Quantifiers: Greedy vs. Non-Greedy (Lazy) Matching

Quantifiers specify how many occurrences of a pattern element should be matched.

| Quantifier | Meaning | Matching Mode |
| :--- | :--- | :--- |
| **`*`** | 0 or more times | **Greedy** (matches as much as possible) |
| **`*?`** | 0 or more times | **Lazy / Non-Greedy** (matches as little as possible) |
| **`+`** | 1 or more times | **Greedy** |
| **`+?`** | 1 or more times | **Lazy / Non-Greedy** |
| **`?`** | 0 or 1 time | **Greedy** |
| **`??`** | 0 or 1 time | **Lazy / Non-Greedy** |
| **`{n}`** | Exactly `n` times | Fixed count |
| **`{n,}`** | At least `n` times | **Greedy** |
| **`{n,m}`** | Between `n` and `m` times | **Greedy** |
| **`{n,m}?`** | Between `n` and `m` times | **Lazy / Non-Greedy** |

### Greedy vs. Lazy Benchmark Example

```python
import re

html_snippet = "<div>Header</div><div>Content</div>"

# GREEDY (<.*>): Matches from FIRST '<' to LAST '>' across entire string
greedy_match = re.findall(r"<div>.*</div>", html_snippet)
print(greedy_match)
# Output: ['<div>Header</div><div>Content</div>']

# LAZY / NON-GREEDY (<.*?>): Matches from '<' to NEAREST '>'
lazy_match = re.findall(r"<div>.*?</div>", html_snippet)
print(lazy_match)
# Output: ['<div>Header</div>', '<div>Content</div>']
```

---

## 8. Anchors & Boundaries

Anchors match **positions** between characters rather than characters themselves.

| Anchor | Description |
| :--- | :--- |
| **`^`** | Matches start of string (or start of line with `re.MULTILINE`) |
| **`$`** | Matches end of string (or end of line with `re.MULTILINE`) |
| **`\b`** | Word boundary (transition between `\w` and `\W` or string start/end) |
| **`\B`** | Non-word boundary |

```python
import re

text = "cat category concatenate scatter"

# \b anchor matches standalone word 'cat' only
standalone_cat = re.findall(r"\bcat\b", text)
print(standalone_cat)  # Output: ['cat']

# Matches 'cat' at start of words
word_start_cat = re.findall(r"\bcat\w*", text)
print(word_start_cat)  # Output: ['cat', 'category']
```

---

## 9. Grouping Mechanics: Capturing, Non-Capturing & Named Groups

Groups allow you to apply quantifiers to sub-patterns or extract structured sub-components.

| Syntax | Group Type | Description |
| :--- | :--- | :--- |
| **`(pattern)`** | Positional Capturing Group | Captures sub-match indexable by number (`1`, `2`, ...) |
| **`(?P<name>pattern)`** | Named Capturing Group | Captures sub-match accessible by string name key |
| **`(?:pattern)`** | Non-Capturing Group | Groups logically without capturing overhead or memory |

```python
import re

log_line = "2026-08-30 14:22:05 [ERROR] Service unavailable"

# 1. Positional Capturing Groups
match_pos = re.search(r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+\[(\w+)\]\s+(.*)", log_line)
print(match_pos.groups())
# Output: ('2026-08-30', '14:22:05', 'ERROR', 'Service unavailable')

# 2. Named Capturing Groups
pattern_named = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+\[(?P<level>\w+)\]\s+(?P<msg>.*)"
)
match_named = pattern_named.search(log_line)
print(match_named.groupdict())
# Output: {'date': '2026-08-30', 'time': '14:22:05', 'level': 'ERROR', 'msg': 'Service unavailable'}

# 3. Non-Capturing Group (?:...)
# Groups (http|https) logically without creating an extra captured group item
match_noncap = re.search(r"(?:https?://)?([\w\.-]+\.[a-z]{2,})", "https://cloudflask.com")
print(match_noncap.groups())
# Output: ('cloudflask.com',)  -- Notice protocol group is ignored
```

---

## 10. Backreferences & Pattern Reuse

**Backreferences** allow you to reference previously captured groups within the pattern itself or inside `re.sub()` replacement strings.

- In pattern: `\1`, `\2`, `(?P=name)`
- In `re.sub()` replacement string: `\1`, `\2`, `\g<name>`

### 1. Finding Duplicate Repeated Words in Text
```python
import re

text = "This is is a test text text string."

# Pattern matches word boundary + word + space + SAME word (\1) + word boundary
duplicate_pattern = r"\b(\w+)\s+\1\b"
duplicates = re.findall(duplicate_pattern, text, re.IGNORECASE)
print(duplicates)  # Output: ['is', 'text']

# Clean duplicate words
cleaned = re.sub(r"\b(\w+)\s+\1\b", r"\1", text, flags=re.IGNORECASE)
print(cleaned)     # Output: 'This is a test text string.'
```

### 2. Reformatting Names via Backreferences
```python
import re

raw_name = "Doe, John"
# Backreference \2 represents group 2 (First Name), \1 represents group 1 (Last Name)
reformatted = re.sub(r"^([A-Za-z]+),\s*([A-Za-z]+)$", r"\2 \1", raw_name)
print(reformatted)  # Output: 'John Doe'
```

---

## 11. Compilation Flags (`re.IGNORECASE`, `re.VERBOSE`, etc.)

Compilation flags modify engine evaluation rules. Multiple flags can be combined using the bitwise OR operator (`|`).

| Flag | Inline Shorthand | Behavioral Description |
| :--- | :--- | :--- |
| **`re.IGNORECASE`** | `(?i)` / `re.I` | Performs case-insensitive matching (`[a-z]` matches `[A-Z]`) |
| **`re.MULTILINE`** | `(?m)` / `re.M` | Causes `^` and `$` to match start/end of EACH line |
| **`re.DOTALL`** | `(?s)` / `re.S` | Allows dot `.` to match newline characters (`\n`) |
| **`re.VERBOSE`** | `(?x)` / `re.X` | Ignores unescaped whitespace and permits `# comments` in regex |
| **`re.ASCII`** | `(?a)` / `re.A` | Restricts `\w`, `\W`, `\b`, `\d` character sets to ASCII only |

### Clean Multi-Line Regex with `re.VERBOSE`

```python
import re

email_verbose = re.compile(r"""
    ^                       # Start of string
    [a-zA-Z0-9._%+-]+       # Local part (username)
    @                       # Literal @ symbol
    [a-zA-Z0-9.-]+          # Domain name
    \.                      # Literal dot
    [a-zA-Z]{2,}            # Top-level domain (TLD)
    $                       # End of string
""", re.VERBOSE | re.IGNORECASE)

print(bool(email_verbose.fullmatch("alex.dev@cloudflask.co.uk"))) # Output: True
```

---

## 12. Lookahead and Lookbehind Assertions

**Lookaround assertions** are zero-width assertions: they match conditions without consuming characters in the match result.

| Lookaround Type | Syntax | Description |
| :--- | :--- | :--- |
| **Positive Lookahead** | `(?=pattern)` | Asserts pattern follows target position |
| **Negative Lookahead** | `(?!pattern)` | Asserts pattern does NOT follow target position |
| **Positive Lookbehind** | `(?<=pattern)` | Asserts pattern precedes target position |
| **Negative Lookbehind** | `(?<!pattern)` | Asserts pattern does NOT precede target position |

### Lookaround Code Examples

```python
import re

# 1. Positive Lookbehind (?<=...): Extract numbers preceded by '$'
price_text = "Item A costs $49.99 and Item B costs £19.50"
usd_prices = re.findall(r"(?<=\$)\d+\.\d{2}", price_text)
print(usd_prices)  # Output: ['49.99']

# 2. Negative Lookbehind (?<!...): Find numbers NOT preceded by '$'
non_usd = re.findall(r"(?<!\$)\b\d+\.\d{2}\b", price_text)
print(non_usd)     # Output: ['19.50']

# 3. Positive Lookahead (?=...): Password Strength Validator
# Asserts string contains >= 1 digit AND >= 1 uppercase letter AND >= 8 characters
password = "CloudFlask2026!"
has_digit = bool(re.search(r"(?=.*\d)", password))
has_upper = bool(re.search(r"(?=.*[A-Z])", password))
valid_len = len(password) >= 8

print(f"Password Valid: {has_digit and has_upper and valid_len}") # Output: True
```

---

## 13. Unicode vs. ASCII Behavior Across Python Versions

### Cross-Version Architectural Evolution

```
Python 2.7 ──────────────────► Python 3.3 (PEP 393) ─────────► Python 3.8 - 3.13
ASCII Default                 Flexible String Representation    Walrus Operator &
u"..." for Unicode             \w matches Unicode by Default    15-25% Speed Boost
```

- **Python 2.7**: Strings were raw bytes by default. `\w` matched only `[a-zA-Z0-9_]` unless `re.UNICODE` (`re.U`) flag was explicitly passed with `u"..."` unicode literals.
- **Python 3.3+ (PEP 393)**: Flexible String Representation optimized memory. `\w`, `\d`, `\s` match Unicode characters globally by default (e.g., `é`, `ñ`, `α`, `日本語`).
- **Python 3.8+**: Assignment expressions (`:=` walrus operator) allow inline regex match assignment: `if match := re.search(...)`.
- **Python 3.9+**: `str.removeprefix()` and `str.removesuffix()` simplify string cleaning without regex overhead.
- **Python 3.11–3.13**: CPython regex engine bytecode execution optimized for **15–25% faster pattern execution**.

```python
import re

unicode_text = "User: René_2026, Role: Admin"
# Python 3 default: \w matches Unicode character 'é'
print(re.findall(r"\w+", unicode_text))
# Output: ['User', 'René_2026', 'Role', 'Admin']

# Force ASCII mode using re.ASCII
print(re.findall(r"\w+", unicode_text, re.ASCII))
# Output: ['User', 'Ren', '2026', 'Role', 'Admin']
```

---

## 14. 10 Comprehensive Practical Examples

### Example 1: Robust Email Address Validation
```python
import re

def validate_email(email: str) -> bool:
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return bool(pattern.fullmatch(email.strip()))

print(validate_email("alex.dev@cloudflask.co.uk"))  # True
print(validate_email("invalid-email@com"))          # False
```

### Example 2: Phone-Number Extraction & Structuring
```python
import re

def extract_phone_numbers(text: str):
    pattern = re.compile(r"\b(?P<area>\d{3})[-.\s]?(?P<prefix>\d{3})[-.\s]?(?P<line>\d{4})\b")
    return [m.groupdict() for m in pattern.finditer(text)]

sample_text = "Call 415-555-2671 or 800.555.9999 for support."
print(extract_phone_numbers(sample_text))
# Output: [{'area': '415', 'prefix': '555', 'line': '2671'}, {'area': '800', 'prefix': '555', 'line': '9999'}]
```

### Example 3: Multi-line Web URL Extraction
```python
import re

def extract_urls(content: str):
    url_pattern = re.compile(r"https?://(?:www\.)?[\w\.-]+\.[a-zA-Z]{2,}(?:/[\w\.-]*)?", re.IGNORECASE)
    return url_pattern.findall(content)

content = "Docs at https://cloudflask.com/docs and code at http://github.com/DilshadPython."
print(extract_urls(content))
# Output: ['https://cloudflask.com/docs', 'http://github.com/DilshadPython']
```

### Example 4: Social Media Username Extraction
```python
import re

def extract_username(url: str) -> str:
    pattern = re.compile(r"(?:https?://)?(?:www\.)?(?:twitter|github|linkedin)\.com/@?([a-zA-Z0-9_]+)", re.IGNORECASE)
    match = pattern.search(url)
    return match.group(1) if match else url

print(extract_username("https://github.com/alex_dev"))  # 'alex_dev'
```

### Example 5: Name Formatting ("Last, First" ➔ "First Last")
```python
import re

def format_name(name_str: str) -> str:
    return re.sub(r"^([A-Za-z]+),\s*([A-Za-z]+)$", r"\2 \1", name_str.strip())

print(format_name("Doe, John"))  # Output: 'John Doe'
```

### Example 6: Server Log File Parsing (IP, Timestamp, Status)
```python
import re

log_entry = '192.168.1.45 - - [30/Aug/2026:10:15:30 +0000] "GET /api/v1/users HTTP/1.1" 200 4521'
log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>GET|POST|PUT|DELETE)\s+(?P<path>\S+)\s+\S+"\s+(?P<status>\d{3})\s+(?P<size>\d+)'
)

match = log_pattern.search(log_entry)
if match:
    print(match.groupdict())
# Output: {'ip': '192.168.1.45', 'timestamp': '30/Aug/2026:10:15:30 +0000', 'method': 'GET', 'path': '/api/v1/users', 'status': '200', 'size': '4521'}
```

### Example 7: Password Complexity Validation
```python
import re

def validate_password_complexity(password: str) -> bool:
    # Requires >= 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special symbol
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    return bool(pattern.fullmatch(password))

print(validate_password_complexity("SecureP@ss2026"))  # True
print(validate_password_complexity("weakpass"))        # False
```

### Example 8: Multi-line File Search for Warnings/Errors
```python
import re

log_file_content = """
2026-08-30 10:00:00 [INFO] System boot initialized
2026-08-30 10:05:12 [WARNING] Memory usage above 85%
2026-08-30 10:10:44 [ERROR] Database connection lost
"""

error_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}.*?\[(?:WARNING|ERROR)\].*$", re.MULTILINE)
issues = error_pattern.findall(log_file_content)
print(issues)
# Output: ['2026-08-30 10:05:12 [WARNING] Memory usage above 85%', '2026-08-30 10:10:44 [ERROR] Database connection lost']
```

### Example 9: Cleaning & Sanitizing Text (HTML Stripping)
```python
import re

def strip_html_tags(html_text: str) -> str:
    # Strips all HTML tags and collapses extra whitespace
    clean_text = re.sub(r"<[^>]+>", "", html_text)
    return re.sub(r"\s+", " ", clean_text).strip()

raw_html = "<h1>Header</h1><p>Welcome to <strong>CloudFlask</strong>!</p>"
print(strip_html_tags(raw_html))  # Output: 'Header Welcome to CloudFlask!'
```

### Example 10: Extracting Key-Value Pairs from Structured Text
```python
import re

config_text = "host=localhost; port=5432; dbname=cloud_db; sslmode=require;"
kv_pattern = re.compile(r"(?P<key>\w+)=(?P<value>[^;\s]+)")

config_dict = {m.group("key"): m.group("value") for m in kv_pattern.finditer(config_text)}
print(config_dict)
# Output: {'host': 'localhost', 'port': '5432', 'dbname': 'cloud_db', 'sslmode': 'require'}
```

---

## 15. Common Mistakes & Catastrophic Backtracking

### 1. Catastrophic Backtracking (ReDoS Attack Risk)
When nested quantifiers are evaluated on non-matching inputs, NFA engines can experience exponential time complexity ($O(2^N)$), freezing the application thread.

```python
# DANGEROUS PATTERN (Nested Quantifiers):
bad_pattern = re.compile(r"(a+)+$")
# Evaluating this on "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab" causes CPU spike and freeze!

# SAFE PATTERN (Atomic / Flattened Quantifier):
safe_pattern = re.compile(r"a+$")
```

### 2. Forgetting Raw String Literals
Using `"\\b"` instead of `r"\b"` causes invalid pattern errors or silent matching failures.

### 3. Parsing HTML/XML with Regular Expressions
HTML is non-regular context-free grammar. Using regex to parse arbitrary HTML fails on nested tags, comments, or quotes.
- **Rule**: Use `BeautifulSoup` or `html.parser` for HTML/XML parsing; use regex only for simple flat tag stripping.

---

## 16. When NOT to Use Regex: String Methods vs. Regex

Regular expressions introduce parsing overhead and reduce readability for simple string operations. Always prefer native `str` built-in methods when pattern matching is not required.

| Goal | Native String Method (Preferred) | Regex (Avoid) |
| :--- | :--- | :--- |
| Check substring presence | `'cloud' in text` | `bool(re.search(r'cloud', text))` |
| Check start/end of string | `text.startswith('http')` | `bool(re.match(r'^http', text))` |
| Simple replacement | `text.replace('a', 'b')` | `re.sub(r'a', 'b', text)` |
| Simple string splitting | `text.split(',')` | `re.split(r',', text)` |
| Prefix/Suffix removal | `text.removeprefix('https://')` | `re.sub(r'^https://', '', text)` |
| Case conversion | `text.lower()`, `text.upper()` | `re.sub(...)` |
| Digits check | `text.isdigit()` | `bool(re.fullmatch(r'\d+', text))` |

### Summary Recommendation
- Use **Native String Methods** for fixed literal searches, simple splits, and exact prefix/suffix operations.
- Use **Regular Expressions (`re`)** only when matching dynamic pattern structures, executing multi-group extractions, or performing complex backreference replacements.
