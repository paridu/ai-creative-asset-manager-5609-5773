import pytest
import asyncio
from typing import Generator
from httpx import AsyncClient
from main import app # Assuming FastAPI entry point

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def client() -> Generator:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture
def mock_asset_metadata():
    return {
        "filename": "brand_guide_v1.pdf",
        "file_type": "application/pdf",
        "tags": ["branding", "blue", "modern"],
        "dominant_colors": ["#0000FF", "#FFFFFF"]
    }