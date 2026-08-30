"""Legacy Computers Script (Refactored).

This module updates the original `computers.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For max size list details, see `Example-Test/max_size_list.py`.
"""


class Monitor:
    """Monitor list container capping elements."""

    def __init__(self, maximum: int) -> None:
        """Initialize Monitor with max size."""
        self.max_size: int = maximum
        self.stored_list = []

    def push(self, brand: str) -> None:
        """Push monitor brand to list, evicting oldest if max size exceeded."""
        self.stored_list.append(brand)
        if len(self.stored_list) > self.max_size:
            self.stored_list.pop(0)

    def get_list(self):
        """Return stored monitor list."""
        return self.stored_list


if __name__ == "__main__":
    print("=== Legacy Computers (Refactored) ===")
    obj = Monitor(4)
    for brand in ["Samsung", "Nokia", "Lenovo", "HP", "LG Ultra"]:
        obj.push(brand)
    print("Monitor List (max 4):", obj.get_list())
