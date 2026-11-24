"""
Section 11: Asynchronous Python & Concurrent I/O (asyncio)

Description: Master Asynchronous Python (asyncio): async def, await, asyncio.gather(), concurrent I/O, httpx, and AsyncSession for high-throughput APIs.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/async_python
"""

# --- Code Snippet 1 ---
# ❌ Thread blocks sequentially for 500ms
def get_user(user_id: int):
    user = database.fetch_user(user_id) # Blocks CPU!
    return user

# --- Code Snippet 2 ---
# ✅ Yields control to event loop during I/O wait
async def get_user(user_id: int):
    user = await database.fetch_user(user_id)
    return user

# --- Code Snippet 3 ---
async def / await

# --- Code Snippet 4 ---
import asyncio
import httpx

async def fetch_user_data(client: httpx.AsyncClient, user_id: int) -> dict:
    response = await client.get(f"https://api.example.com/users/{user_id}")
    return response.json()

async def fetch_all_users_concurrently(user_ids: list[int]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [fetch_user_data(client, uid) for uid in user_ids]
        results = await asyncio.gather(*tasks) # Concurrent execution!
        return results

# Entrypoint to run event loop
profiles = asyncio.run(fetch_all_users_concurrently([101, 102, 103]))

