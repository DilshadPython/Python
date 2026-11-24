"""
Sequence Reflection Engine Module (`sequence_reflection.py`).

This module provides reusable helper functions and the `ReflectionEngine` class
for reversing sequences (lists, strings, tuples) preserving types, inspecting runtime attributes,
and performing dynamic method reflection.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import inspect`: Inspect live objects, signatures, and module code.
# - `import sys`: System utilities for execution status.
# - `from typing import Any, Dict, List, Sequence, TypeVar`: PEP 484 type hint generics.
# =========================================================================
import inspect
import sys
from typing import Any, Dict, List, Sequence, TypeVar

T = TypeVar("T")


class ReflectionEngine:
    """Utility class providing static reflection and sequence introspection operations."""

    @staticmethod
    def reflect_sequence(seq: Sequence[Any]) -> Sequence[Any]:
        """Recursively reflect (reverse) any sequence preserving its concrete type (list, str, tuple).

        Args:
            seq (Sequence[Any]): Target sequence to reverse.

        Returns:
            Sequence[Any]: Reversed sequence preserving original type constructor.
        """
        seq_type = type(seq)
        empty_seq = seq_type()

        if seq == empty_seq:
            return empty_seq

        rest_reversed = ReflectionEngine.reflect_sequence(seq[1:])
        first_elem = seq[0:1]

        # Combine reversed rest with first element
        return rest_reversed + first_elem  # type: ignore

    @staticmethod
    def inspect_object(obj: Any) -> Dict[str, str]:
        """Inspect public attributes and callable methods of an object at runtime.

        Args:
            obj (Any): Target object instance.

        Returns:
            Dict[str, str]: Dictionary mapping attribute names to type representation strings.
        """
        attributes: Dict[str, str] = {}
        for attr_name in dir(obj):
            if not attr_name.startswith("__"):
                try:
                    attr_val = getattr(obj, attr_name)
                    attr_type = "method" if callable(attr_val) else type(attr_val).__name__
                    attributes[attr_name] = attr_type
                except Exception as err:
                    attributes[attr_name] = f"error({err})"
        return attributes

    @staticmethod
    def invoke_dynamically(obj: Any, method_name: str, *args: Any, **kwargs: Any) -> Any:
        """Dynamically find and execute a method on an object instance via string name reflection.

        Args:
            obj (Any): Target object instance.
            method_name (str): Name of method attribute to invoke.
            *args (Any): Positional arguments for target method.
            **kwargs (Any): Keyword arguments for target method.

        Returns:
            Any: Return value of invoked method.

        Raises:
            AttributeError: If method_name does not exist on object.
            TypeError: If attribute is not callable.
        """
        if not hasattr(obj, method_name):
            raise AttributeError(f"Object '{type(obj).__name__}' has no attribute '{method_name}'")

        method = getattr(obj, method_name)
        if not callable(method):
            raise TypeError(f"Attribute '{method_name}' on '{type(obj).__name__}' is not callable")

        return method(*args, **kwargs)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for reflection engine demonstration."""
    print("=== Reflection Engine Demonstration ===")

    sample_list = [2, 4, 5, 6, 8, 9]
    sample_str = "Hello world"

    reversed_list = ReflectionEngine.reflect_sequence(sample_list)
    reversed_str = ReflectionEngine.reflect_sequence(sample_str)

    print(f"Original List: {sample_list} -> Reversed: {reversed_list}")
    print(f"Original String: '{sample_str}' -> Reversed: '{reversed_str}'")

    return 0


if __name__ == "__main__":
    sys.exit(main())
