"""Demonstrates and compares standalone Functions vs Object Methods in Python.

This module provides clear comparisons between standalone functions, instance methods,
class methods, static methods, and descriptor reflection using dir().
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Any, Dict, List


# Standalone Function (Bound to module namespace)
def standalone_function(x: int, y: int) -> int:
    """Standalone function defined at module level."""
    return x + y


class CalculatorService:
    """Class showcasing instance methods, class methods, and static methods."""

    def __init__(self, base_value: int = 100):
        self.base_value: int = base_value

    def instance_method(self, value: int) -> int:
        """Instance method: bound to instance (self). Accesses instance state."""
        return self.base_value + value

    @classmethod
    def class_method(cls, value: int) -> int:
        """Class method: bound to class (cls). Accesses class state/constructor."""
        return value * 2

    @staticmethod
    def static_method(value: int) -> int:
        """Static method: unbound utility function contained within class namespace."""
        return value ** 2


def inspect_method_attributes(obj: Any) -> List[str]:
    """Inspect public methods and attributes of a function or method object using dir().

    Args:
        obj: Function or bound method object.

    Returns:
        List of non-dunder attribute names available on the target object.
    """
    attributes = dir(obj)
    return [attr for attr in attributes if not attr.startswith("__")]


def compare_function_and_method() -> Dict[str, Any]:
    """Compare standalone functions against class instance methods, class methods, and static methods.

    Returns:
        Dict[str, Any]: Comparison analysis dictionary containing type information and dir() attributes.
    """
    service = CalculatorService(100)

    return {
        "function_analysis": {
            "name": standalone_function.__name__,
            "type": type(standalone_function).__name__,  # 'function'
            "public_attributes": inspect_method_attributes(standalone_function),
            "description": "Standalone function defined at module level.",
        },
        "instance_method_analysis": {
            "name": service.instance_method.__name__,
            "type": type(service.instance_method).__name__,  # 'method'
            "self_bound": service.instance_method.__self__ is service,
            "underlying_func": service.instance_method.__func__.__name__,
            "public_attributes": inspect_method_attributes(service.instance_method),
            "result": service.instance_method(50),
            "description": "Bound method tied to instance (self).",
        },
        "class_method_analysis": {
            "name": CalculatorService.class_method.__name__,
            "type": type(CalculatorService.class_method).__name__,  # 'method'
            "result": CalculatorService.class_method(50),
            "description": "Bound method tied to class object (cls).",
        },
        "static_method_analysis": {
            "name": CalculatorService.static_method.__name__,
            "type": type(CalculatorService.static_method).__name__,  # 'function'
            "result": CalculatorService.static_method(5),
            "description": "Unbound function nested inside class.",
        },
    }


if __name__ == "__main__":
    res = compare_function_and_method()
    print("=== Functions vs Methods Comparison ===")
    print("Function Type:", res["function_analysis"]["type"])
    print("Instance Method Type:", res["instance_method_analysis"]["type"])
    print("Underlying Function:", res["instance_method_analysis"]["underlying_func"])
    print("Instance Method Result:", res["instance_method_analysis"]["result"])
    print("Class Method Result:", res["class_method_analysis"]["result"])
    print("Static Method Result:", res["static_method_analysis"]["result"])
