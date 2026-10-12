"""
Track 03: Execution Context & Robustness

Description: Master Senior Python Track 03: Execution Context & Robustness. Context Managers (__enter__, __exit__, @contextmanager), contextvars task propagation, Exception Chaining (raise ... from ...), and Decimal & Fraction precision math.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/execution_context_robustness
"""

# --- Code Snippet 1 ---
import threading

class ManagedResourceLock:
    def __init__(self, lock_id: str):
        self.lock_id = lock_id
        self._lock = threading.Lock()

    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock.release()
        if exc_type is KeyError:
            return True  # Suppress expected KeyError
        return False     # Re-raise uncaught exceptions

# --- Code Snippet 2 ---
import asyncio
import contextvars

request_id_var = contextvars.ContextVar("request_id", default="UNKNOWN")

async def process_task(req_id: str):
    token = request_id_var.set(req_id)
    try:
        await asyncio.sleep(0.01)
        print("Task Context ID:", request_id_var.get())
    finally:
        request_id_var.reset(token)

# --- Code Snippet 3 ---
class PublicAPIError(Exception): pass

def handle_user_request():
    try:
        connect_private_db()
    except DatabaseTimeoutError as err:
        # Mask sensitive database hostnames from public clients
        raise PublicAPIError("Service temporarily unavailable.") from None

# --- Code Snippet 4 ---
from decimal import Decimal, ROUND_HALF_UP

# String initialization guarantees exact base-10 precision
price = Decimal("19.99")
tax = Decimal("0.07")
subtotal = price * Decimal("3")
total = (subtotal * (Decimal("1") + tax)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print("Exact Ledger Total:", total)  # Decimal('64.17')

