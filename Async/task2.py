import asyncio

async def write_file(index):
    filename = f'file_{index}.txt'
    with open(filename, 'w') as file:
        file.write(str(index))
    print(f'File {filename} created.')

async def main():
    tasks = [write_file(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)

asyncio.run(main())