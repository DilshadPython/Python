"""
Attribute & Method Inspector Engine Module (`attribute_method_inspector.py`).

This module provides reusable helper functions and the `AttributeMethodInspector` class
for categorizing an object's attributes, methods, descriptors, and dunders at runtime.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import inspect`: Standard library module for object reflection and type checks.
# - `import sys`: System execution status utilities.
# - `from typing import Any, Dict, List, Type`: PEP 484 type hint generics.
# =========================================================================
import inspect
import sys
from typing import Any, Dict, List, Type


class AttributeMethodInspector:
    """Inspector engine analyzing object attributes, methods, properties, and dunders."""

    @staticmethod
    def inspect_object(obj: Any) -> Dict[str, Dict[str, str]]:
        """Inspect and categorize all attributes and methods on an object instance.

        Args:
            obj (Any): Target object instance or type.

        Returns:
            Dict[str, Dict[str, str]]: Categorized dict containing:
                - 'dunder_methods': Special double-underscore methods.
                - 'public_methods': Callable methods and functions.
                - 'instance_attributes': Value attributes and fields.
                - 'properties': Property descriptor attributes.
        """
        categories: Dict[str, Dict[str, str]] = {
            "dunder_methods": {},
            "public_methods": {},
            "instance_attributes": {},
            "properties": {},
        }

        cls = obj if inspect.isclass(obj) else type(obj)

        for attr_name in dir(obj):
            try:
                # Check for property descriptor on class level
                class_attr = getattr(cls, attr_name, None)
                if isinstance(class_attr, property):
                    categories["properties"][attr_name] = "property"
                    continue

                attr_val = getattr(obj, attr_name)

                if attr_name.startswith("__") and attr_name.endswith("__"):
                    categories["dunder_methods"][attr_name] = type(attr_val).__name__
                elif callable(attr_val):
                    categories["public_methods"][attr_name] = "method"
                else:
                    categories["instance_attributes"][attr_name] = type(attr_val).__name__
            except Exception as err:
                categories["instance_attributes"][attr_name] = f"error({err})"

        return categories

    @staticmethod
    def get_lookup_hierarchy(cls: Type[Any], attr_name: str) -> List[str]:
        """Trace attribute lookup hierarchy across Class MRO, instance dict, and descriptors.

        Args:
            cls (Type[Any]): Target class.
            attr_name (str): Attribute identifier.

        Returns:
            List[str]: Execution resolution order steps.
        """
        resolution_steps: List[str] = [
            f"1. Check if '__getattribute__' is overridden on {cls.__name__}",
            f"2. Check for Data Descriptor in Class MRO for '{attr_name}'",
            f"3. Check Instance '__dict__' for '{attr_name}'",
            f"4. Check for Non-Data Descriptor in Class MRO for '{attr_name}'",
            f"5. Check Class '__dict__' across MRO: {[c.__name__ for c in cls.__mro__]}",
            f"6. Fallback to '__getattr__' if attribute '{attr_name}' was not found",
        ]
        return resolution_steps


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for attribute method inspector demonstration."""
    print("=== Attribute & Method Inspector Engine Demonstration ===")

    class Sample:
        """Sample class for inspection demonstration."""

        def __init__(self, name: str) -> None:
            self.name = name

        @property
        def uppercase_name(self) -> str:
            return self.name.upper()

        def greet() -> str:
            return "Hello"

    sample_obj = Sample("Dilshad")
    report = AttributeMethodInspector.inspect_object(sample_obj)

    print(f"Properties: {list(report['properties'].keys())}")
    print(f"Instance Attributes: {report['instance_attributes']}")
    print(f"Public Methods Sample: {list(report['public_methods'].keys())[:5]}")
    print(f"Dunder Methods Count: {len(report['dunder_methods'])}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
