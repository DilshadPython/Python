"""
Python 3.7 Feature Demonstration
--------------------------------
Highlights:
1. Data Classes (`dataclasses` module) (PEP 557)
2. Context Variables (`contextvars` module) (PEP 567)
3. High-precision nanosecond timing (PEP 564)
4. Postponed annotations behavior (PEP 563)
"""

from __future__ import annotations  # PEP 563: Postponed evaluation of annotations
import contextvars
from dataclasses import dataclass, field
import time
from typing import List, Optional


# 1. Data Classes (`@dataclass`) (PEP 557)
@dataclass(order=True, frozen=False)
class UserProfile:
    user_id: int
    username: str
    email: str
    roles: List[str] = field(default_factory=list)
    is_active: bool = True

    def add_role(self, role: str) -> UserProfile:
        # Self-referencing return type annotation supported without quotes thanks to PEP 563
        self.roles.append(role)
        return self


def demo_dataclasses() -> None:
    print("--- 1. Demo: Data Classes (PEP 557) ---")
    user1 = UserProfile(user_id=1, username="alice", email="alice@example.com")
    user1.add_role("admin").add_role("developer")

    user2 = UserProfile(user_id=2, username="bob", email="bob@example.com", roles=["user"])

    print(f"  Generated User 1 Repr: {user1}")
    print(f"  Is User 1 active?      {user1.is_active}")
    print(f"  Are users equal?       {user1 == user2}")
    print()


# 2. Context Variables (`contextvars`) (PEP 567)
request_id_var: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("request_id", default=None)


def process_request() -> None:
    req_id = request_id_var.get()
    print(f"  [Worker Thread/Task] Processing with Request ID: {req_id}")


def demo_contextvars() -> None:
    print("--- 2. Demo: Context Variables (PEP 567) ---")
    token = request_id_var.set("REQ-98765-XYZ")
    try:
        process_request()
    finally:
        request_id_var.reset(token)

    print(f"  After Reset Request ID: {request_id_var.get()}")
    print()


# 3. High-Precision Nanosecond Timing (PEP 564)
def demo_nanosecond_timing() -> None:
    print("--- 3. Demo: Nanosecond Timers (PEP 564) ---")
    start_ns = time.perf_counter_ns()
    
    # Simple work
    _ = [x ** 2 for x in range(50_000)]
    
    elapsed_ns = time.perf_counter_ns() - start_ns
    elapsed_ms = elapsed_ns / 1_000_000

    print(f"  Elapsed Time (Nanoseconds):  {elapsed_ns:,} ns")
    print(f"  Elapsed Time (Milliseconds): {elapsed_ms:.3f} ms")
    print()


if __name__ == "__main__":
    print("========================================")
    print("        PYTHON 3.7 FEATURE DEMO        ")
    print("========================================\n")
    demo_dataclasses()
    demo_contextvars()
    demo_nanosecond_timing()
