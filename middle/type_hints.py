"""
Section 9: Modern Type Hints & Static Type Checking

Description: Master Python Type Hints: Union syntax (User | None), Generics, Protocols, TypedDict, TypeVar, and static type checking with mypy and pyright.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/type_hints
"""

# --- Code Snippet 1 ---
# ❌ What types does this take? What does it return?
def process_user_data(user_id, flags):
    user = fetch_user(user_id)
    if not user:
        return None
    return user.compute_scores(flags)

# --- Code Snippet 2 ---
# ✅ Modern Union syntax (User | None) & built-in generics
def process_user_data(
    user_id: int, 
    flags: list[str]
) -> ScoreResult | None:
    user: User | None = fetch_user(user_id)
    return user.compute_scores(flags) if user else None

# --- Code Snippet 3 ---
from typing import TypeVar, Generic, Literal, TypedDict, Protocol, TypeAlias

# 1. TypeAlias & Literal Types
UserId: TypeAlias = int
Role: TypeAlias = Literal["admin", "user", "guest"]

# 2. TypedDict Structure
class UserPayload(TypedDict):
    sub: str
    role: Role

# 3. Protocol (Duck Typing Contract)
class Renderable(Protocol):
    def render(self) -> str:
        ...

# 4. Generic Repository Contract
T = TypeVar("T")

class GenericRepository(Generic[T]):
    def __init__(self) -> None:
        self._store: dict[UserId, T] = {}

    def get_by_id(self, entity_id: UserId) -> T | None:
        return self._store.get(entity_id)

