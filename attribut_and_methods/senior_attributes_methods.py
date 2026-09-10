"""
Senior Level Attributes, Descriptors & Metaprogramming Module (`senior_attributes_methods.py`).

This module provides enterprise-grade attribute patterns designed for senior software engineers
(Custom Descriptors `__get__`/`__set__`/`__set_name__`, Attribute Interception `__getattribute__`/`__getattr__`/`__setattr__`, Memory Optimization `__slots__`, Callable Objects `__call__`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System execution status utilities.
# - `from typing import Any, Dict, Optional, Type`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import Any, Dict, Optional, Type


class ValidatedStringDescriptor:
    """Custom Data Descriptor implementing attribute validation and PEP 487 `__set_name__`."""

    def __init__(self, min_length: int = 1) -> None:
        self.min_length = min_length
        self.storage_name: str = ""

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        """PEP 487 Callback automatically storing attribute name upon class creation."""
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, "")

    def __set__(self, instance: Any, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Attribute '{self.storage_name}' must be a string")
        if len(value) < self.min_length:
            raise ValueError(f"String length must be at least {self.min_length} characters")
        setattr(instance, self.storage_name, value)


class MemoryOptimizedUser:
    """Class demonstrating memory optimization using `__slots__` instead of `__dict__`."""

    __slots__ = ("user_id", "email")

    def __init__(self, user_id: int, email: str) -> None:
        self.user_id = user_id
        self.email = email


class DynamicAttributeInterceptors:
    """Class demonstrating attribute interception hooks (`__getattribute__`, `__getattr__`, `__setattr__`)."""

    def __init__(self) -> None:
        self.known_attr = "Standard Value"

    def __getattribute__(self, item: str) -> Any:
        """Intercepts EVERY attribute access attempt."""
        # Use super() to avoid infinite recursion!
        return super().__getattribute__(item)

    def __getattr__(self, item: str) -> Any:
        """Invoked ONLY when attribute is NOT found in instance dict or class hierarchy."""
        return f"Dynamic Fallback for '{item}'"

    def __setattr__(self, key: str, value: Any) -> None:
        """Intercepts EVERY attribute assignment attempt."""
        super().__setattr__(key, value)


class CallableCalculator:
    """Class demonstrating callable objects by implementing the `__call__` dunder method."""

    def __init__(self, multiplier: int) -> None:
        self.multiplier = multiplier

    def __call__(self, x: int) -> int:
        """Allows instance object to be called directly like a function `calc(10)`."""
        return x * self.multiplier


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for senior attributes and methods demonstration."""
    print("=== Senior Level Attributes, Descriptors & Metaprogramming ===")

    # Custom Descriptor Demonstration
    class UserProfile:
        username = ValidatedStringDescriptor(min_length=3)

    user = UserProfile()
    user.username = "Dilshad"
    print(f"Validated Descriptor Username: '{user.username}'")

    # __slots__ Memory Optimization
    opt_user = MemoryOptimizedUser(101, "user@example.com")
    print(f"__slots__ User ID: {opt_user.user_id}, Email: {opt_user.email}")
    print(f"Has __dict__ attribute? {hasattr(opt_user, '__dict__')}")

    # Dynamic Attribute Interceptors
    interceptor = DynamicAttributeInterceptors()
    print(f"Known Attribute: '{interceptor.known_attr}'")
    print(f"Unknown Attribute (fallback): '{interceptor.missing_attribute}'")

    # Callable Objects (__call__)
    double = CallableCalculator(multiplier=2)
    print(f"Callable Object Double Output (double(21)): {double(21)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
