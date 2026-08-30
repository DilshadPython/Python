"""Legacy Products Script (Refactored).

This module updates the original `products.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
"""


class Item:
    """Class representing an item product."""

    def __init__(self, item_name: str, item_color: str, item_num: str) -> None:
        """Initialize Item with name, color, and number."""
        self.item_name: str = item_name
        self.item_color: str = item_color
        self.item_num: str = f"{item_color}.{item_num}"

    def item_detail(self) -> str:
        """Return formatted item detail string."""
        return f"{self.item_name} {self.item_color}"


if __name__ == "__main__":
    print("=== Legacy Products (Refactored) ===")
    obj_1 = Item("Carbon", "Red", "081")
    print(obj_1.item_detail())
