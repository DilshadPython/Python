import time
import functools
import logging

logging.basicConfig(level=logging.INFO)

def log_execution_time(action_name: str):
    """Production decorator to measure and log database/API latency."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration_ms = (time.perf_counter() - start) * 1000
            logging.info(f"[{action_name}] took {duration_ms:.2f}ms")
            return result
        return wrapper
    return decorator

@log_execution_time("Database User Fetch")
def fetch_user_record(user_id: int):
    # Optimized query execution
    time.sleep(0.04)
    return {"id": user_id, "role": "cloud_engineer"}