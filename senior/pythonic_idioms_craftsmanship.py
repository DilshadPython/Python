"""
Track 04: Pythonic Idioms & Software Craftsmanship

Description: Master Senior Python Track 04: Become Genuinely Pythonic. EAFP vs LBYL performance, Duck Typing & structural protocols (typing.Protocol), Composition over inheritance, Guard clause flattening, and readable code idioms.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/pythonic_idioms_craftsmanship
"""

# --- Code Snippet 1 ---
def fetch_user_avatar_eafp(cache: dict, user_id: str) -> str:
    """Pythonic EAFP: Executes single hash lookup; thread-safe and zero happy path cost."""
    try:
        return cache[user_id]
    except KeyError:
        return "default_avatar.png"

# --- Code Snippet 2 ---
from typing import Protocol, runtime_checkable

@runtime_checkable
class Streamable(Protocol):
    def read_chunk(self, size: int) -> bytes: ...

def process_stream(source: Streamable) -> bytes:
    """Accepts any object implementing read_chunk capability."""
    return source.read_chunk(1024)

# --- Code Snippet 3 ---
def process_order_flat(order: dict) -> str:
    if not order:
        return "Invalid Order"
    if order.get("status") != "active":
        return "Inactive Order"
    if not order.get("items"):
        return "Empty Items"
    
    return "Order Processed Successfully"

