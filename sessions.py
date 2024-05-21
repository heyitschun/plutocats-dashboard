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

async def get(url):
    try:
        async with session_manager.session.get(url, timeout=10) as response:
            response.raise_for_status()
            data = await response.json()
            return data
    except asyncio.TimeoutError:
        print('The request timed out')
    except aiohttp.ClientError as e:
        print(f'An error occurred: {e}')