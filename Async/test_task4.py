import pytest
from task4 import run
from unittest.mock import patch

url = "https://example.com/"
num_requests = 50
max_concurrent_requests = 10

@pytest.mark.asyncio
async def test_run():
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_get.return_value.__aenter__.return_value.status = 200
        await run(url, num_requests, max_concurrent_requests)
        assert mock_get.call_count == num_requests