"""
Track 02: Advanced OOP, ABCs & Protocols

Description: Master Mid-Level Advanced OOP: Property getters/setters, Class methods, Abstract Base Classes (ABCs), Structural Protocols, Descriptors, and Dunder methods.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/advanced_oop
"""

# --- Code Snippet 1 ---
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._balance = max(0.0, balance)

    @property
    def balance(self) -> float:
        """Read-only property getter."""
        return self._balance

    @classmethod
    def create_empty(cls, owner: str):
        """Alternative constructor initializing empty account."""
        return cls(owner=owner, balance=0.0)

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Utility method with no access to self or cls."""
        return amount > 0.0

acc = BankAccount.create_empty("Alice")
print(acc.owner, acc.balance)

# --- Code Snippet 2 ---
from abc import ABC, abstractmethod
from typing import Protocol

# 1. Nominal Interface via ABC
class StorageBackend(ABC):
    @abstractmethod
    def save(self, data: dict) -> bool:
        pass

# 2. Structural Contract via Protocol
class Renderable(Protocol):
    def render(self) -> str: ...

class DashboardWidget:
    def render(self) -> str:
        return "<div class='widget'>Widget Content</div>"

def display_component(item: Renderable):
    print("Render Output:", item.render())

display_component(DashboardWidget())

# --- Code Snippet 3 ---
class NonEmptyString:
    """Descriptor enforcing non-empty string validation."""
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, "")

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Value must be a non-empty string!")
        setattr(instance, self.private_name, value)

class Product:
    name = NonEmptyString()

p = Product()
p.name = "TeachCloud Pro"
print("Product Name:", p.name)

