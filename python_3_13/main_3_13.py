"""
Python 3.13 Feature Demonstration
---------------------------------
Highlights:
1. Precise Type Narrowing with `typing.TypeIs` (PEP 742)
2. `TypeVar` with default values (PEP 696)
3. Read-Only TypedDict fields (`typing.ReadOnly`)
4. Standard Deprecation Decorator (`warnings.deprecated`) (PEP 702)
5. Summary of GIL-free multi-threading and JIT Compiler
"""

import sys
import warnings
from typing import TypeIs, ReadOnly, TypedDict, TypeVar, Optional


# 1. Precise Type Narrowing (`typing.TypeIs`) (PEP 742)
def is_str_list(val: list[object]) -> TypeIs[list[str]]:
    """Symmetric type predicate: If returns True, val is list[str]. If False, val is NOT list[str]."""
    return all(isinstance(x, str) for x in val)


def process_items(items: list[object]) -> None:
    if is_str_list(items):
        # Type narrowed to list[str] in if-branch
        joined = ", ".join(items)
        print(f"  [TypeIs Narrowed] Joined strings: {joined}")
    else:
        # Type narrowed to list[object] excluding list[str] in else-branch
        print(f"  [TypeIs Narrowed] Non-string list containing {len(items)} items")


def demo_type_is() -> None:
    print("--- 1. Demo: typing.TypeIs (PEP 742) ---")
    process_items(["python", "3.13", "release"])
    process_items([10, 20, 30])
    print()


# 2. Type Parameter Defaults (PEP 696)
# Specify default type 'str' for generic parameter T via TypeVar(..., default=...)
T = TypeVar("T", default=str)


class Container:
    """Demonstrating TypeVar default value T = TypeVar('T', default=str)."""
    def __init__(self, value: object = "Default String Container") -> None:
        self.value = value

    def get_val(self) -> object:
        return self.value


def demo_typevar_defaults() -> None:
    print("--- 2. Demo: TypeVar Defaults (PEP 696) ---")
    default_container = Container()
    int_container = Container(42)

    print(f"  Default Container Value: {default_container.get_val()}")
    print(f"  Explicit Int Container:  {int_container.get_val()}")
    print()


# 3. Read-Only TypedDict Fields (`typing.ReadOnly`)
class UserDatabaseRecord(TypedDict):
    id: ReadOnly[int]          # Immutable field
    username: ReadOnly[str]    # Immutable field
    email: str                 # Mutable field


def demo_read_only_typeddict() -> None:
    print("--- 3. Demo: ReadOnly TypedDict ---")
    record: UserDatabaseRecord = {
        "id": 1001,
        "username": "monika_dev",
        "email": "monika@example.com"
    }

    print(f"  User Record: {record}")
    record["email"] = "monika.updated@example.com"
    print(f"  Updated email (mutable field): {record['email']}")
    print("  Note: 'id' and 'username' are marked ReadOnly and protected at type-check time.")
    print()


# 4. Standard Deprecation Decorator (`warnings.deprecated`) (PEP 702)
@warnings.deprecated("old_legacy_function is deprecated; use new_modern_function instead.")
def old_legacy_function() -> str:
    return "Legacy Output"


def demo_deprecation_warning() -> None:
    print("--- 4. Demo: @warnings.deprecated (PEP 702) ---")
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        output = old_legacy_function()
        print(f"  Legacy function output: {output}")
        if w:
            print(f"  Captured Deprecation Warning: {w[-1].message}")
    print()


# 5. CPython 3.13 Runtime Capabilities Overview
def demo_cpython_runtime_info() -> None:
    print("--- 5. Demo: Python 3.13 Runtime Architecture ---")
    print(f"  Python Version: {sys.version.split()[0]}")
    print("  GIL Status:     Free-threading build support available (--disable-gil)")
    print("  JIT Status:     Copy-and-patch JIT compiler option enabled (--enable-experimental-jit)")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.13 FEATURE DEMO       ")
    print("========================================\n")
    demo_type_is()
    demo_typevar_defaults()
    demo_read_only_typeddict()
    demo_deprecation_warning()
    demo_cpython_runtime_info()
