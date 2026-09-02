"""
Advanced Object-Oriented Programming: Mixins, Descriptors & Subclass Hooks.

This module demonstrates advanced Python OOP architectural patterns:
1. Descriptor Protocol: Custom attribute access control using __set_name__, __get__, and __set__.
2. Mixin Pattern: Reusable behavioral extension classes (e.g., JSONSerializerMixin).
3. Modern Metaprogramming: __init_subclass__ hook for automatic subclass registration (PEP 487).
"""
# "import module" loads json module from standard library for serialization.
import json
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Any, Dict, List, Type


class BoundedIntegerDescriptor:
    """
    Descriptor enforcing integer type and value bounds on class attributes.

    Demonstrates Python descriptor protocol hooks (__set_name__, __get__, __set__).
    """

    def __init__(self, min_value: int = 0, max_value: int = 100) -> None:
        """Initialize descriptor boundary limits."""
        self.min_value: int = min_value
        self.max_value: int = max_value
        self.private_name: str = ""

    def __set_name__(self, owner: Type[Any], name: str) -> None:
        """Called automatically at class creation time to bind attribute name."""
        self.private_name = f"_{name}"

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        """Getter hook returning internal instance attribute value."""
        if instance is None:
            return self
        return getattr(instance, self.private_name, self.min_value)

    def __set__(self, instance: Any, value: int) -> None:
        """Setter hook validating integer type and boundary constraints."""
        if not isinstance(value, int):
            raise TypeError(f"Attribute '{self.private_name[1:]}' must be an integer.")
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f"Attribute '{self.private_name[1:]}' value {value} must be between "
                f"{self.min_value} and {self.max_value}."
            )
        setattr(instance, self.private_name, value)


class JSONSerializerMixin:
    """
    Mixin class providing reusable JSON serialization capabilities to derived classes.
    """

    def to_json(self) -> str:
        """
        Serialize instance attributes (__dict__) to a formatted JSON string.

        Returns:
            str: JSON representation of the object's attribute state.
        """
        # Clean private underscore prefixes for user-friendly JSON keys
        clean_dict = {
            k.lstrip("_"): v
            for k, v in self.__dict__.items()
            if not callable(v) and not k.startswith("__")
        }
        return json.dumps(clean_dict, sort_keys=True)


class PluginBase:
    """
    Base class utilizing __init_subclass__ (PEP 487) for automatic subclass registration.
    """

    registered_plugins: Dict[str, Type["PluginBase"]] = {}

    def __init_subclass__(cls, plugin_name: str = "", **kwargs: Any) -> None:
        """
        Hook called whenever a subclass is derived from PluginBase.

        Args:
            plugin_name (str): Unique identifier for registering the plugin class.
        """
        super().__init_subclass__(**kwargs)
        name = plugin_name or cls.__name__
        cls.registered_plugins[name] = cls
