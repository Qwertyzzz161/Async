import pytest
from task3 import main
from unittest.mock import patch

google_url = "https://www.google.com"
urls = [google_url] * 50


@pytest.mark.asyncio
async def test_main():
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_get.return_value.__aenter__.return_value.status = 200
        await main(urls)
        assert mock_get.call_count == len(urls)