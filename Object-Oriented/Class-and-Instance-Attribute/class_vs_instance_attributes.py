"""Class vs Instance Attributes Demonstration Module.

This module demonstrates the distinction between class attributes (shared defaults)
and instance attributes (object-specific state), including attribute assignment timing and lookup mechanics.
"""

from typing import Dict, Any


class VehicleInventory:
    """Class showcasing class attributes and dynamic instance attribute assignment."""

    # Class Attributes
    default_price: float = 20000.0
    stock_count: int = 0

    def __init__(self, model_name: str) -> None:
        """Initialize VehicleInventory with a model name."""
        self.model_name: str = model_name

    def configure_inventory(self, custom_price: float, stock_quantity: int) -> None:
        """Set instance-specific price and stock count attributes.

        Args:
            custom_price: Price for this vehicle instance.
            stock_quantity: Stock quantity for this vehicle instance.
        """
        self.price: float = custom_price
        self.stock_count: int = stock_quantity


if __name__ == "__main__":
    print("=== Class vs Instance Attributes Demonstration ===")
    inventory = VehicleInventory("Sedan")

    print("Class Attribute default_price:", inventory.default_price)
    print("Initial stock_count (falls back to class attribute):", inventory.stock_count)

    inventory.configure_inventory(25000.0, 3)
    print("\nAfter configure_inventory():")
    print("Instance Attribute price:", inventory.price)
    print("Instance stock_count (shadows class attribute):", inventory.stock_count)
    print("Class stock_count remains untouched:", VehicleInventory.stock_count)
