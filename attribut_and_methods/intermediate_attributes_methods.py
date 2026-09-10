"""
Intermediate Level Attributes & Methods Module (`intermediate_attributes_methods.py`).

This module provides functional attribute and method patterns designed for intermediate developers
(`@classmethod`, `@staticmethod`, `@property` getter/setter/deleter, `getattr`, `setattr`, `hasattr`, `delattr`, container dunders).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System execution status utilities.
# - `from typing import Any, Dict, List, Optional`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import Any, Dict, List, Optional


class Account:
    """Class demonstrating Class Attributes, Classmethods, Staticmethods, and Property Descriptors."""

    # Class Attribute: Shared across all instances of Account
    BANK_NAME: str = "Global Python Bank"
    total_accounts: int = 0

    def __init__(self, account_holder: str, initial_balance: float) -> None:
        self.account_holder = account_holder
        self._balance = initial_balance  # Protected attribute by convention
        Account.total_accounts += 1

    # Property Getter
    @property
    def balance(self) -> float:
        """Property getter returning account balance."""
        return self._balance

    # Property Setter
    @balance.setter
    def balance(self, new_balance: float) -> None:
        """Property setter validating and setting account balance."""
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_balance

    # Classmethod: Receives `cls` as first parameter
    @classmethod
    def create_corporate_account(cls, company_name: str) -> "Account":
        """Classmethod factory creating an account with default $10,000 corporate balance."""
        return cls(company_name, 10000.0)

    # Staticmethod: Utility function bound to class namespace (no self or cls)
    @staticmethod
    def validate_account_name(name: str) -> bool:
        """Staticmethod utility validating account holder name formatting."""
        return len(name.strip()) >= 3


class CustomContainer:
    """Class demonstrating container dunder methods (`__getitem__`, `__setitem__`, `__contains__`)."""

    def __init__(self) -> None:
        self._items: Dict[str, Any] = {}

    def __getitem__(self, key: str) -> Any:
        return self._items[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._items[key] = value

    def __contains__(self, key: str) -> bool:
        return key in self._items


def demonstrate_dynamic_attribute_functions(obj: Any) -> None:
    """Demonstrate built-in reflection functions `getattr`, `setattr`, `hasattr`, `delattr`, and `dir`."""
    print(f"hasattr(obj, 'account_holder'): {hasattr(obj, 'account_holder')}")

    # getattr with default fallback
    holder = getattr(obj, "account_holder", "Unknown")
    print(f"getattr(obj, 'account_holder'): '{holder}'")

    # setattr dynamic mutation
    setattr(obj, "branch_code", "NY-001")
    print(f"getattr after setattr (branch_code): '{getattr(obj, 'branch_code')}'")

    # delattr dynamic removal
    delattr(obj, "branch_code")
    print(f"hasattr after delattr (branch_code): {hasattr(obj, 'branch_code')}")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate attributes and methods demonstration."""
    print("=== Intermediate Level Attributes & Methods Demonstration ===")

    # Staticmethod validation
    is_valid = Account.validate_account_name("Dilshad")
    print(f"Staticmethod Name Check: {is_valid}")

    # Classmethod factory invocation
    corp_acc = Account.create_corporate_account("Tech Corp")
    print(f"Classmethod Account Balance: ${corp_acc.balance}")
    print(f"Shared Class Attribute (total_accounts): {Account.total_accounts}")

    # Property Setter validation
    corp_acc.balance = 12500.0
    print(f"Updated Property Balance: ${corp_acc.balance}")

    print("\n--- Dynamic Attribute Functions ---")
    demonstrate_dynamic_attribute_functions(corp_acc)

    return 0


if __name__ == "__main__":
    sys.exit(main())
