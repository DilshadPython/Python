"""
Demonstrates dynamic attribute management (delattr, hasattr, getattr) on Python class objects.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Tuple


class VehicleItem:
    """Sample class representing a vehicle item with class attributes."""
    name: str = "Volvo"
    year: int = 2010
    model: str = "EX90"


def inspect_and_delete_attribute(cls_or_obj: Any, attr_name: str) -> Tuple[bool, bool]:
    """
    Check if an attribute exists on a class or instance, delete it if present, and verify removal.
    
    Args:
        cls_or_obj (Any): Target class or object instance.
        attr_name (str): Attribute name string.
        
    Returns:
        Tuple[bool, bool]: Tuple of (existed_before, exists_after).
    """
    existed_before: bool = hasattr(cls_or_obj, attr_name)
    if existed_before:
        delattr(cls_or_obj, attr_name)
    exists_after: bool = hasattr(cls_or_obj, attr_name)
    return existed_before, exists_after


if __name__ == '__main__':
    print("Initial attributes:", {k: v for k, v in VehicleItem.__dict__.items() if not k.startswith('__')})
    before, after = inspect_and_delete_attribute(VehicleItem, 'name')
    print(f"Attribute 'name' existed before deletion: {before}, after: {after}")
    print("Attributes after deletion:", {k: v for k, v in VehicleItem.__dict__.items() if not k.startswith('__')})
