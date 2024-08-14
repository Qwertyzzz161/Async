import asyncio
import aiohttp

async def fetch_url(session, url, semaphore):
    async with semaphore:
            async with session.get(url) as response:
                print(f"Request to {url}, status code: {response.status}")


async def main(urls, max_concurrent_requests=10):
    semaphore = asyncio.Semaphore(max_concurrent_requests)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, semaphore) for url in urls]
        await asyncio.gather(*tasks)


google_url = "https://www.google.com"
urls = [google_url] * 50


asyncio.run(main(urls))