import pytest
import os
from task2 import write_file, main



@pytest.mark.asyncio
async def test_write_file():
    index = 1
    await write_file(index)
    filename = f'file_{index}.txt'
    assert os.path.exists(filename)
    with open(filename, 'r') as file:
        content = file.read()
    assert content == str(index)
    os.remove(filename)


@pytest.mark.asyncio
async def test_main():
    await main()
    for i in range(1, 11):
        filename = f'file_{i}.txt'
        assert os.path.exists(filename)
        with open(filename, 'r') as file:
            content = file.read()
        assert content == str(i)
        os.remove(filename)

