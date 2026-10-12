# Python 3.6 Overview & Features

**Release Date:** December 23, 2016  
**Key Focus:** Formatted String Literals (F-strings), Variable Annotations, Numeric Underscores, Cryptographic Randomness (`secrets`), and Async Comprehensions.

---

## 🚀 Key Features & Syntax Additions

### 1. Formatted String Literals (F-strings) (PEP 498)
Introduced the `f"..."` prefix for string literals, allowing expressions to be evaluated directly inside curly braces `{expression}` at runtime. F-strings are faster, cleaner, and less error-prone than `%` formatting or `.format()`.

### 2. Variable Type Annotations (PEP 526)
Extended PEP 484 type hints to variable declarations: `variable_name: type = value`.
- Class variables and instance attributes can now be explicitly typed.

### 3. Underscores in Numeric Literals (PEP 515)
Allowed single underscores `_` in digits of numeric literals for improved visual readability:
- `million = 1_000_000`
- `binary = 0b1111_0000`
- `hex_val = 0xFF_FF_FF`

### 4. Cryptographically Secure Pseudo-Random Numbers (`secrets`) (PEP 506)
Added the `secrets` module, dedicated to generating cryptographically strong random numbers suitable for managing security credentials, API keys, tokens, and password reset URLs.

### 5. Asynchronous Generators & Async Comprehensions (PEP 525 & PEP 530)
- **Async Generators**: Generators that use `yield` inside an `async def` function.
- **Async Comprehensions**: Comprehensions operating over async iterables: `[i async for i in async_gen()]`.

### 6. Subclass Customization Hook (`__init_subclass__`) (PEP 487)
Introduced `__init_subclass__` as a clean alternative to metaclasses for customizing class creation of subclasses.

### 7. Ordered Dictionaries by Default
CPython 3.6 implemented dictionaries using a compact representation that preserved key insertion order as a side effect (made an official language guarantee in Python 3.7).

---

## 🛠️ Summary Table of Important PEPs

| PEP | Feature | Description |
|---|---|---|
| **PEP 498** | Formatted String Literals | `f"{var}"` expression string interpolation |
| **PEP 526** | Variable Annotations | Type annotations syntax for variables and attributes |
| **PEP 515** | Numeric Underscores | Visual grouping in numbers (`1_000_000`) |
| **PEP 506** | `secrets` module | Secure random generation for cryptography & security |
| **PEP 525 / 530** | Async Generators & Comprehensions | `async for`, `yield` in `async def`, async comprehensions |
| **PEP 487** | `__init_subclass__` | Lightweight class hierarchy customization hook |

---

## 💻 Pythonic Code Showcase

Check `main_3_6.py` and `f_string.py` in this directory for runnable code examples demonstrating:
- Formatting string expressions and numbers using f-strings
- Type-annotating class and instance variables
- Using `secrets.token_hex()` and `secrets.token_urlsafe()` for security
- Writing numeric literals with underscores
- Utilizing `__init_subclass__` for class registry patterns
