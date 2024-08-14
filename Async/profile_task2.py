import asyncio
import cProfile
import pstats
import io
from memory_profiler import profile

@profile
async def write_file(index):
    filename = f'file_{index}.txt'
    with open(filename, 'w') as file:
        file.write(str(index))
    print(f'File {filename} created.')


async def main():
    tasks = [write_file(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)

def profile_code():
    pr = cProfile.Profile()
    pr.enable()
    asyncio.run(main())
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


profile_code()

