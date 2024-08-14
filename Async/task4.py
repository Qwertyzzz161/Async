import aiohttp
import asyncio
import json

async def fetch_url(semaphore, session, url):
    async with semaphore:
        async with session.get(url) as response:
            return response.status

async def run(url, num_requests, max_concurrent_requests):
    semaphore = asyncio.Semaphore(max_concurrent_requests)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(semaphore, session, url) for _ in range(num_requests)]
        statuses = await asyncio.gather(*tasks)

        with open('statuses.json', 'w') as f:
            json.dump(statuses, f)

        print(f"Total requests: {len(statuses)}")

url = "https://example.com/"
num_requests = 50
max_concurrent_requests = 10

asyncio.run(run(url, num_requests, max_concurrent_requests))

