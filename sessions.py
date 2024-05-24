import aiohttp
import asyncio

class SessionManager:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def reinitialize_session(self):
        self.session = aiohttp.ClientSession()

    async def close_session(self):
        await self.session.close()

session_manager = SessionManager()

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            data = await response.json()
            return data