from typing import Annotated

from fastapi import Depends
from httpx import AsyncClient

from app.core.config import get_settings


async def get_http_client() -> AsyncClient:
    async with AsyncClient(
        base_url=get_settings().nobel_prize_api_url,
        headers={"Accept": "application/json"},
    ) as client:
        yield client


http_client = Annotated[AsyncClient, Depends(get_http_client)]
