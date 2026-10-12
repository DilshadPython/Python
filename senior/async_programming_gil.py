"""
Track 10: Asynchronous Programming & The GIL

Description: Master Senior Python Track 10: Asynchronous Programming & The GIL. Concurrency models comparison, Python 3.11+ asyncio.TaskGroup structured concurrency, and preventing event loop starvation with asyncio.to_thread.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/async_programming_gil
"""

# --- Code Snippet 1 ---
import asyncio

async def fetch_user_dashboard(user_id: int):
    # TaskGroup guarantees both tasks complete before block exit.
    # If fetch_orders raises an error, fetch_analytics is automatically cancelled!
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch_orders(user_id))
        t2 = tg.create_task(fetch_analytics(user_id))
    
    return t1.result(), t2.result()

# --- Code Snippet 2 ---
import asyncio
import time

def sync_blocking_disk_io(path: str) -> str:
    time.sleep(1.0)  # Blocking synchronous call!
    return f"Read {path} successfully"

async def async_request_handler():
    # WRONG: time.sleep(1.0) freezes ALL concurrent coroutines!
    # RIGHT: Offload blocking I/O to thread pool worker
    content = await asyncio.to_thread(sync_blocking_disk_io, "/var/log/app.log")
    return content

