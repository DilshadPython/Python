"""
Track 01: Advanced Python Fundamentals

Description: Master Mid-Level Advanced Python Fundamentals: *args, **kwargs, Generators, Decorators, Context Managers, Collections, Dataclasses, and Functional Tools.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/advanced_fundamentals
"""

# --- Code Snippet 1 ---
def build_user_profile(user_id: int, *roles: str, **metadata) -> dict:
    """Combines positional args into tuple (*roles) and kwargs into dict (**metadata)."""
    return {
        "user_id": user_id,
        "roles": roles,        # tuple of extra positional arguments
        "metadata": metadata   # dictionary of extra keyword arguments
    }

profile = build_user_profile(101, "admin", "editor", team="DevOps", active=True)
print(profile)
# Output: {'user_id': 101, 'roles': ('admin', 'editor'), 'metadata': {'team': 'DevOps', 'active': True}}

# --- Code Snippet 2 ---
def batch_streamer(dataset: list, batch_size: int = 2):
    """Generator streaming slices in memory-efficient chunks."""
    for i in range(0, len(dataset), batch_size):
        yield dataset[i:i + batch_size]

data = ["record_1", "record_2", "record_3", "record_4", "record_5"]
for chunk in batch_streamer(data, batch_size=2):
    print("Batch Chunk:", chunk)

# --- Code Snippet 3 ---
import time
from functools import wraps

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - t0) * 1000
        print(f"⚡ [{func.__name__}] executed in {elapsed:.2f} ms")
        return result
    return wrapper

@time_it
def compute_squares(n: int) -> list:
    """Computes squares up to n."""
    return [x ** 2 for x in range(n)]

res = compute_squares(10000)

# --- Code Snippet 4 ---
from dataclasses import dataclass, field
from contextlib import contextmanager

@dataclass(frozen=True)
class UserConfig:
    db_host: str = "localhost"
    port: int = 5432
    options: list = field(default_factory=list)

@contextmanager
def db_session(connection_url: str):
    print(f"🔌 Connecting to {connection_url}...")
    session = {"connected": True}
    try:
        yield session
    finally:
        print("🔒 Session closed safely.")

with db_session("postgresql://localhost:5432/mydb") as s:
    print("Querying database...", s)

