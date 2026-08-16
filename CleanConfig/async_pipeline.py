import asyncio
import aiohttp

async def fetch_service_health(session: aiohttp.ClientSession, url: str) -> dict:
    """Poll microservice health endpoint with bounded timeout."""
    try:
        timeout = aiohttp.ClientTimeout(total=2.0)
        async with session.get(url, timeout=timeout) as resp:
            return {"url": url, "status": resp.status, "ok": resp.status == 200}
    except Exception as err:
        return {"url": url, "status": 500, "error": str(err), "ok": False}

async def check_all_microservices(service_urls: list[str]) -> list[dict]:
    """Concurrent fan-out execution across downstream services."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_service_health(session, u) for u in service_urls]
        return await asyncio.gather(*tasks)