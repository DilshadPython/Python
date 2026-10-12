"""
Senior Level Metaprogramming & Class Reflection Module (`senior_reflection.py`).

This module provides enterprise reflection and metaprogramming patterns designed for senior software engineers
(subclass registry reflection `__subclasses__()`, dynamic class creation using `type()`, runtime method binding and decoration).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `from functools import wraps`: Preserve function signatures across dynamic decorators.
# - `import inspect`: Inspect object hierarchies and frame stacks.
# - `import sys`: System execution status utilities.
# - `from typing import Any, Callable, Dict, List, Type`: PEP 484 type hint generics.
# =========================================================================
from functools import wraps
import inspect
import sys
from typing import Any, Callable, Dict, List, Type


class BasePlugin:
    """Base class defining plugin hierarchy for subclass reflection registry."""

    def execute(self) -> str:
        """Execute default base plugin logic."""
        return "Base execution"


class DataPlugin(BasePlugin):
    """Data processing plugin implementation."""

    def execute(self) -> str:
        return "Executing Data Plugin"


class ExportPlugin(BasePlugin):
    """Export utility plugin implementation."""

    def execute(self) -> str:
        return "Executing Export Plugin"


def discover_subclasses(base_class: Type[Any]) -> List[Type[Any]]:
    """Discover all runtime registered subclasses of a given base class using `__subclasses__()`.

    Args:
        base_class (Type[Any]): Base class type.

    Returns:
        List[Type[Any]]: List of active subclass types.
    """
    return base_class.__subclasses__()


def create_dynamic_class(class_name: str, base_classes: tuple[type, ...], attributes: Dict[str, Any]) -> Type[Any]:
    """Dynamically construct a new Python class at runtime using the `type()` metaclass call.

    Args:
        class_name (str): Desired class name.
        base_classes (tuple[type, ...]): Tuple of base parent classes.
        attributes (Dict[str, Any]): Dictionary of attributes and methods.

    Returns:
        Type[Any]: Newly constructed class object.
    """
    return type(class_name, base_classes, attributes)


def attach_reflection_logging(method: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator reflecting method name and arguments before execution.

    Args:
        method (Callable[..., Any]): Target function/method.

    Returns:
        Callable[..., Any]: Wrapped function with execution logging.
    """

    @wraps(method)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[REFLECTION LOG] Invoking '{method.__name__}' with args={args}, kwargs={kwargs}")
        result = method(*args, **kwargs)
        print(f"[REFLECTION LOG] '{method.__name__}' returned -> {result}")
        return result

    return wrapper


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for senior reflection demonstration."""
    print("=== Senior Level Metaprogramming & Subclass Reflection ===")

    discovered = discover_subclasses(BasePlugin)
    print(f"Discovered BasePlugin Subclasses: {[cls.__name__ for cls in discovered]}")

    # Create dynamic class at runtime
    DynamicService = create_dynamic_class(
        "DynamicService",
        (BasePlugin,),
        {"version": "1.0.0", "custom_run": lambda self: "Dynamic class execution"},
    )

    instance = DynamicService()
    print(f"Dynamic Class Name: {type(instance).__name__}")
    print(f"Dynamic Method Output: {instance.custom_run()}")

    # Attach reflection logging wrapper
    logged_run = attach_reflection_logging(instance.custom_run)
    logged_run()

    return 0


if __name__ == "__main__":
    sys.exit(main())
