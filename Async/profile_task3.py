import cProfile
import pstats
import io
from memory_profiler import profile
import asyncio
import aiohttp

@profile
async def fetch_url(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url) as response:
                print(f"Request to {url}, status code: {response.status}")
        except Exception as e:
            print(f"Error fetching {url}: {e}")

async def main(urls, max_concurrent_requests=10):
    semaphore = asyncio.Semaphore(max_concurrent_requests)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, semaphore) for url in urls]
        await asyncio.gather(*tasks)




def profile_code():
    pr = cProfile.Profile()
    pr.enable()
    google_url = "https://www.google.com"
    urls = [google_url] * 50
    asyncio.run(main(urls))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


profile_code()