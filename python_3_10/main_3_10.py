"""
Python 3.10 Feature Demonstration
---------------------------------
Highlights:
1. Structural Pattern Matching `match / case` (PEPs 634, 635, 636)
2. Union Type Operator `X | Y` (PEP 604)
3. Strict length checks in `zip(..., strict=True)`
4. Explicit Type Aliases (`TypeAlias`) (PEP 613)
"""

from dataclasses import dataclass
from typing import TypeAlias, Any


# 1. Structural Pattern Matching `match / case` (PEPs 634/635/636)
@dataclass
class Command:
    action: str
    target: str


def handle_event(event: Any) -> str:
    match event:
        case 200 | 201:
            return "HTTP Success"
        case 400 | 401 | 403 | 404 as code:
            return f"HTTP Client Error ({code})"
        case Command(action="click", target=target):
            return f"UI Event: Clicked on {target}"
        case {"type": "notification", "msg": text}:
            return f"Notification Received: {text}"
        case [first, *rest] if len(rest) > 0:
            return f"Sequence unpack: First={first}, Rest={rest}"
        case _:
            return "Unhandled Event"


def demo_pattern_matching() -> None:
    print("--- 1. Demo: Pattern Matching match/case (PEP 634) ---")
    events = [
        200,
        404,
        Command(action="click", target="SubmitButton"),
        {"type": "notification", "msg": "Task Complete"},
        [10, 20, 30, 40],
        "unknown_data"
    ]

    for ev in events:
        result = handle_event(ev)
        print(f"  Input: {str(ev):<45} -> Match: {result}")
    print()


# 2. Union Type Operator `X | Y` (PEP 604)
# Explicit Type Alias (PEP 613)
UserId: TypeAlias = int | str


def process_user_identifier(user_id: UserId) -> str:
    # Union types work directly in isinstance checks as well!
    if isinstance(user_id, int | float):
        return f"Numeric User ID: {int(user_id):06d}"
    elif isinstance(user_id, str):
        return f"String User ID: {user_id.upper()}"
    return "Unknown Format"


def demo_union_operator() -> None:
    print("--- 2. Demo: Union Type Operator X | Y (PEP 604) ---")
    print(f"  Passed int: {process_user_identifier(42)}")
    print(f"  Passed str: {process_user_identifier('usr_monika')}")
    print()


# 3. Zip Strict Mode (`strict=True`)
def demo_zip_strict() -> None:
    print("--- 3. Demo: zip(..., strict=True) ---")
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    extra_scores = [85, 92, 78, 99]

    # Equal lengths - works cleanly
    paired = list(zip(names, scores, strict=True))
    print(f"  Paired items (Equal lengths): {paired}")

    try:
        # Unequal lengths - raises ValueError with strict=True
        list(zip(names, extra_scores, strict=True))
    except ValueError as err:
        print(f"  Caught expected error with strict=True: {err}")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.10 FEATURE DEMO       ")
    print("========================================\n")
    demo_pattern_matching()
    demo_union_operator()
    demo_zip_strict()
