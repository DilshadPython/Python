# Pedagogical Technical Reference: Python Regular Expressions (`re`) & Version Evolution

This document provides a comprehensive technical guide to the mechanics of CPython's regular expression engine (`sre`), AST/compilation pipeline, object introspection (`re.Pattern` and `re.Match`), design patterns, security considerations (ReDoS prevention), and cross-version evolution from Python 2.7 through Python 3.13.

---

## 1. Engine Architecture & CPython Implementation

Python's regular expression functionality is powered by the `sre` (Secret Labs' Regular Expression) engine implemented in C (`Modules/_sre.c`).

### Compilation Pipeline

When a regex pattern string is supplied to `re.compile()`:
1. **Parsing**: The pattern string is parsed into an abstract syntax tree of regex tokens.
2. **Optimization**: Consecutive literals, character sets, and quantifiers are simplified.
3. **Bytecode Compilation**: The pattern is compiled into SRE bytecode (an array of 16-bit or 32-bit unsigned integers representing opcode instructions like `FAILURE`, `SUCCESS`, `AT`, `CATEGORY`, `MAX_UNTIL`).
4. **Execution**: When `search()`, `match()`, or `finditer()` is called, the C-based matching loop (`sre_match` / `sre_search`) executes the SRE bytecode against the target string.

---

## 2. Introspection of `re.Pattern` and `re.Match` Objects

Python 3.7 explicitly exposed `re.Pattern` and `re.Match` as top-level types in the `re` module, allowing clear type annotations.

### `re.Pattern` Object Attributes and Methods

A compiled pattern object (`re.Pattern`) encapsulates the compiled regex bytecode and matching configuration.

```python
import re

pattern: re.Pattern = re.compile(r"(?P<area>\d{3})-(?P<number>\d{7})", re.IGNORECASE)

# Attributes and Methods via dir(pattern)
print(pattern.pattern)     # Raw regex string: '(?P<area>\d{3})-(?P<number>\d{7})'
print(pattern.flags)       # Integer bitmask of compilation flags (e.g. re.IGNORECASE)
print(pattern.groups)      # Total number of capturing groups: 2
print(pattern.groupindex)  # Mapping of named groups: {'area': 1, 'number': 2}
```

Key methods on `re.Pattern`:
- `pattern.search(string[, pos[, endpos]])`: Scans string for first match.
- `pattern.match(string[, pos[, endpos]])`: Matches pattern strictly at start of string.
- `pattern.fullmatch(string[, pos[, endpos]])`: Matches pattern against entire string.
- `pattern.findall(string)`: Returns list of matching strings or tuples.
- `pattern.finditer(string)`: Returns an iterator yielding `re.Match` objects.
- `pattern.sub(repl, string, count=0)`: Replaces matches with replacement string.

### `re.Match` Object Attributes and Methods

A match object (`re.Match`) represents the result of a successful pattern match.

```python
match: re.Match = pattern.search("Call 532-6580010 today")

print(match.group(0))         # Full match: '532-6580010'
print(match.group('area'))    # Named group match: '532'
print(match.groups())         # Tuple of all captured groups: ('532', '6580010')
print(match.groupdict())      # Dictionary of named groups: {'area': '532', 'number': '6580010'}
print(match.span())           # (start, end) index tuple: (5, 16)
print(match.start(), match.end()) # 5, 16
```

---

## 3. Comprehensive Version Evolution (Python 2.7 to Python 3.13)

### Python 2.7 vs Python 3.x Differences

1. **String Types & Unicode Default**:
   - **Python 2.7**: `re` treated standard `str` strings as byte sequences. Matching Unicode required explicit `u"..."` prefix and `re.UNICODE` flag.
   - **Python 3.x**: All `str` objects are Unicode sequences by default. `\w`, `\d`, and `\s` match Unicode characters unless `re.ASCII` (or `b"..."` bytes pattern) is specified.

2. **Module Types**:
   - **Python 2.7 - 3.6**: `type(re.compile(""))` returned `_sre.SRE_Pattern`. `re.Pattern` was not a public alias.
   - **Python 3.7+**: Exposed public type aliases `re.Pattern` and `re.Match` for type hints.

### Key Feature Timeline

- **Python 3.8 (PEP 572: Walrus Assignment Expressions `:=`)**:
  Allowed inline assignment and conditional testing of regex matches:
  ```python
  if match := re.search(r"^(\w+)@(\w+\.\w+)$", email):
      print(match.groups())
  ```

- **Python 3.9 (`str.removeprefix` / `str.removesuffix`)**:
  Provided clean built-in string methods for simple prefix/suffix stripping without incurring regular expression compilation overhead:
  ```python
  # Replaces re.sub(r"^https://", "", url)
  clean_url = url.removeprefix("https://")
  ```

- **Python 3.11 (Atomic Grouping & Possessive Quantifiers)**:
  Python 3.11 added support for atomic groups `(?>...)` and possessive quantifiers (`*+`, `++`, `?+`, `{m,n}+`). These constructs disable backtracking inside the group, preventing catastrophic backtracking vulnerabilities.
  ```python
  # Atomic group disables backtracking inside (?>...)
  pattern = re.compile(r"(?>\w+)@example\.com")
  ```

- **Python 3.12 - 3.13 Engine & Unicode Updates**:
  CPython 3.12 and 3.13 optimized `sre_match` execution loops, reducing matching overhead for simple character classes and updating Unicode table mappings to Unicode 15.1.

---

## 4. Performance & Security Notes: Preventing ReDoS

### Regular Expression Denial of Service (ReDoS)

ReDoS occurs when a regular expression experiences **catastrophic backtracking** on non-matching or partially matching inputs. This happens when nested or overlapping quantifiers force the engine to evaluate an exponential number of paths $O(2^n)$.

#### Dangerous (Vulnerable) Pattern Example:
```python
# VULNERABLE: Nested quantifiers (a+)+
bad_pattern = re.compile(r"^(a+)+$")
# Testing against 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaX' causes high CPU freeze!
```

#### Safe Patterns & Mitigations:
1. **Eliminate Overlapping Quantifiers**: Unify patterns so multiple paths cannot match the same character.
2. **Use Possessive Quantifiers / Atomic Groups (Python 3.11+)**: Prevent backtracking once a partial sequence has matched:
   ```python
   # Python 3.11+ Atomic quantifier
   safe_pattern = re.compile(r"^(a++)+$")
   ```
3. **Pre-compile Regular Expressions**: Use `re.compile()` outside loops or hot code paths to avoid re-parsing the pattern string on every function call.

---

## 5. Introspection Comparison Table

| Attribute / Method | Object Type | Returns | Description |
| :--- | :--- | :--- | :--- |
| `pattern.pattern` | `re.Pattern` | `str` / `bytes` | Original regex pattern string |
| `pattern.flags` | `re.Pattern` | `int` | Bitmask of flags (`re.IGNORECASE`, etc.) |
| `pattern.groups` | `re.Pattern` | `int` | Count of capturing groups |
| `pattern.groupindex` | `re.Pattern` | `dict` | Mapping of group names to 1-based indices |
| `match.group([g1, ...])` | `re.Match` | `str` / `tuple` | Matched subgroup string(s) |
| `match.groups()` | `re.Match` | `tuple` | Tuple of all captured subgroup values |
| `match.groupdict()` | `re.Match` | `dict` | Dict mapping named groups to captured values |
| `match.span([group])` | `re.Match` | `tuple[int, int]` | Tuple of `(start, end)` indices for group |
