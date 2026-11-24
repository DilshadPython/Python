# Technical Documentation: Python Operator Precedence & Internal Dunder Hooks

## 📊 Python Operator Precedence Table (Highest to Lowest)

| Precedence Group | Operator | Description | Associativity |
| :--- | :--- | :--- | :--- |
| **1. Primary** | `()` `[]` `.` | Grouping, Indexing, Attribute Access | Left-to-Right |
| **2. Exponentiation** | `**` | Power / Exponentiation | Right-to-Left |
| **3. Unary** | `+x` `-x` `~x` | Positive, Negative, Bitwise NOT | Right-to-Left |
| **4. Multiplicative** | `*` `/` `//` `%` `@` | Multiplication, Division, Floor Div, Modulo, Matrix | Left-to-Right |
| **5. Additive** | `+` `-` | Addition, Subtraction | Left-to-Right |
| **6. Bitwise Shift** | `<<` `>>` | Left Shift, Right Shift | Left-to-Right |
| **7. Bitwise AND** | `&` | Bitwise AND | Left-to-Right |
| **8. Bitwise XOR** | `^` | Bitwise XOR | Left-to-Right |
| **9. Bitwise OR** | `\|` | Bitwise OR | Left-to-Right |
| **10. Comparison** | `==` `!=` `>` `<` `>=` `<=` `is` `in` | Relational, Identity, Membership | Left-to-Right |
| **11. Logical NOT** | `not` | Boolean NOT | Right-to-Left |
| **12. Logical AND** | `and` | Boolean AND | Left-to-Right |
| **13. Logical OR** | `or` | Boolean OR | Left-to-Right |
| **14. Assignment** | `=` `+=` `-=` `:=` | Assignment & Walrus Expression | Right-to-Left |

---

## 🔍 Operator Dunder Protocol Hooks Mapping

| Operator | Dunder Method Hook | Reverse Dunder Hook | In-Place Dunder Hook |
| :--- | :--- | :--- | :--- |
| `+` | `__add__(self, other)` | `__radd__(self, other)` | `__iadd__(self, other)` |
| `-` | `__sub__(self, other)` | `__rsub__(self, other)` | `__isub__(self, other)` |
| `*` | `__mul__(self, other)` | `__rmul__(self, other)` | `__imul__(self, other)` |
| `/` | `__truediv__(self, other)` | `__rtruediv__(self, other)` | `__itruediv__(self, other)` |
| `//` | `__floordiv__(self, other)` | `__rfloordiv__(self, other)` | `__ifloordiv__(self, other)` |
| `%` | `__mod__(self, other)` | `__rmod__(self, other)` | `__imod__(self, other)` |
| `@` | `__matmul__(self, other)` | `__rmatmul__(self, other)` | `__imatmul__(self, other)` |
| `==` | `__eq__(self, other)` | N/A | N/A |
| `<` | `__lt__(self, other)` | `__gt__(self, other)` | N/A |
