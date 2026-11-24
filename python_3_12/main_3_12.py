"""
Python 3.12 Feature Demonstration
---------------------------------
Highlights:
1. Syntactic Type Parameter Lists & `type` statement (PEP 695)
2. Formalized F-string syntax (PEP 701) - quotes reuse, backslashes, nesting
3. `@override` decorator (PEP 698)
"""

from typing import override, List, Dict


# 1. Syntactic Type Parameter Lists & `type` statement (PEP 695)
# Define clean generic type aliases without TypeVar
type Vector[T] = list[T]
type KeyValueMap[K, V] = dict[K, V]


# Generic function with inline type parameter T
def get_first_element[T](items: Vector[T]) -> T | None:
    return items[0] if items else None


class Buffer[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def get_all(self) -> list[T]:
        return self._items


def demo_type_statement() -> None:
    print("--- 1. Demo: type statement & Type Parameter Lists (PEP 695) ---")
    num_vector: Vector[int] = [10, 20, 30]
    first = get_first_element(num_vector)
    print(f"  Vector[int]: {num_vector} -> First: {first}")

    buf: Buffer[str] = Buffer()
    buf.push("Python 3.12")
    buf.push("Features")
    print(f"  Buffer[str]: {buf.get_all()}")
    print()


# 2. Formalized F-Strings (PEP 701)
def demo_formalized_fstrings() -> None:
    print("--- 2. Demo: Formalized F-Strings (PEP 701) ---")
    data = {"name": "Monika", "role": "Developer"}
    lines = ["Line 1", "Line 2", "Line 3"]

    # Quote reuse inside expression: "name" inside double-quoted f-string!
    info_str = f"User profile: {data["name"]} ({data["role"]})"

    # Backslashes inside expressions: '\n'.join() allowed inside curly braces!
    joined_str = f"Multiline content:\n{'\n'.join(lines)}"

    print(f"  Quote Reuse inside F-string: {info_str}")
    print(f"  Backslash inside F-string:   {joined_str}")
    print()


# 3. `@override` Decorator (PEP 698)
class BaseHandler:
    def process(self) -> str:
        return "Base handler execution"


class CustomHandler(BaseHandler):
    @override
    def process(self) -> str:
        # Ensures this method correctly overrides BaseHandler.process
        return "Custom sub-class handler execution"


def demo_override_decorator() -> None:
    print("--- 3. Demo: @override Decorator (PEP 698) ---")
    handler = CustomHandler()
    print(f"  Handler result: {handler.process()}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.12 FEATURE DEMO       ")
    print("========================================\n")
    demo_type_statement()
    demo_formalized_fstrings()
    demo_override_decorator()
