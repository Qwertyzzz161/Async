import aiohttp
import asyncio
import json
import cProfile
import pstats
import io
from memory_profiler import profile

@profile
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


def profile_code():
    pr = cProfile.Profile()
    pr.enable()
    url = "https://example.com/"
    num_requests = 50
    max_concurrent_requests = 10
    asyncio.run(run(url, num_requests, max_concurrent_requests))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


profile_code()