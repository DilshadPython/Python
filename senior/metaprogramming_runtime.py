"""
Track 02: Metaprogramming & Runtime Mechanics

Description: Master Senior Python Track 02: Metaprogramming & Runtime Mechanics. Descriptors (__get__, __set__), __new__ vs __init__, __eq__ and __hash__, MRO and super().
Level: Senior
URL: http://127.0.0.1:5000/python/senior/metaprogramming_runtime
"""

# --- Code Snippet 1 ---
class BoundedNumber:
    """Data descriptor validating numeric bounds at runtime."""
    def __init__(self, min_val: float, max_val: float):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self._name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None: return self
        return getattr(instance, self._name, None)

    def __set__(self, instance, value: float):
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"Value {value} outside range [{self.min_val}, {self.max_val}]")
        setattr(instance, self._name, value)

class Metric:
    cpu_usage = BoundedNumber(0.0, 100.0)

# --- Code Snippet 2 ---
class UppercaseString(str):
    """Subclassing immutable str via __new__ allocation."""
    def __new__(cls, value: str):
        # Value must be transformed prior to C-level allocation
        return super().__new__(cls, value.upper())

code = UppercaseString("production_key")
print(code) # "PRODUCTION_KEY"

# --- Code Snippet 3 ---
class FrozenRecord:
    def __init__(self, record_id: str, code: int):
        self._record_id = record_id
        self._code = code

    def __eq__(self, other):
        if not isinstance(other, FrozenRecord): return NotImplemented
        return self._record_id == other._record_id and self._code == other._code

    def __hash__(self):
        # Must hash strictly immutable tuple state
        return hash((self._record_id, self._code))

# --- Code Snippet 4 ---
class A:
    def hello(self): print("A")

class B(A):
    def hello(self): print("B")

class C(A):
    def hello(self): print("C")

class D(B, C):
    pass

# D.__mro__ == (D, B, C, A, object)
# Executing D().hello() prints "B".
# If B.hello is removed, it prints "C" (never "A" first).

