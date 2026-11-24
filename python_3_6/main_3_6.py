"""
Python 3.6 Feature Demonstration
--------------------------------
Highlights:
1. Formatted String Literals (F-strings) (PEP 498)
2. Variable Annotations (PEP 526)
3. Underscores in Numeric Literals (PEP 515)
4. `secrets` module for secure randomness (PEP 506)
5. Class customization via `__init_subclass__` (PEP 487)
"""

import asyncio
import secrets
from typing import List, Dict


# 1. F-strings (PEP 498) & Variable Annotations (PEP 526)
class Product:
    # Variable annotations syntax (PEP 526)
    name: str
    price: float
    stock: int

    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def summary(self) -> str:
        # F-strings evaluation inside curly braces (PEP 498)
        return f"Product: {self.name.title()} | Total Value: ${self.price * self.stock:,.2f}"


def demo_fstrings_and_annotations() -> None:
    print("--- 1. Demo: F-Strings & Variable Annotations ---")
    item = Product(name="laptop", price=1299.99, stock=15)
    print(f"  {item.summary()}")
    print()


# 2. Underscores in Numeric Literals (PEP 515)
def demo_numeric_underscores() -> None:
    print("--- 2. Demo: Underscores in Numeric Literals (PEP 515) ---")
    one_million: int = 1_000_000
    byte_mask: int = 0b1111_0000
    hex_color: int = 0xFF_57_33

    print(f"  One Million:  {one_million} (Formatted: {one_million:,})")
    print(f"  Binary Mask:  {bin(byte_mask)}")
    print(f"  Hex Color:    {hex(hex_color)}")
    print()


# 3. Cryptographically Secure Tokens (`secrets`) (PEP 506)
def demo_secrets() -> None:
    print("--- 3. Demo: secrets Module (PEP 506) ---")
    api_token: str = secrets.token_hex(16)
    reset_url_token: str = secrets.token_urlsafe(16)

    print(f"  Generated Hex Token: {api_token}")
    print(f"  URL Safe Reset Token: {reset_url_token}")
    print()


# 4. Class Creation Hook (`__init_subclass__`) (PEP 487)
class PluginBase:
    subclasses: List[str] = []

    def __init_subclass__(cls, plugin_name: str = "default", **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(plugin_name)
        print(f"  [Plugin Framework] Registered Plugin: '{plugin_name}'")


class AudioPlugin(PluginBase, plugin_name="audio_processor"):
    pass


class VideoPlugin(PluginBase, plugin_name="video_renderer"):
    pass


def demo_init_subclass() -> None:
    print("--- 4. Demo: __init_subclass__ (PEP 487) ---")
    print(f"  Registered Plugins List: {PluginBase.subclasses}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.6 FEATURE DEMO        ")
    print("========================================\n")
    demo_fstrings_and_annotations()
    demo_numeric_underscores()
    demo_secrets()
    demo_init_subclass()
