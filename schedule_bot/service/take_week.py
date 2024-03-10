import httpx
from loguru import logger

from utils.env import api_week_endpoint


async def take_week() -> int | None:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_week_endpoint())
        return int(response.text)
    except httpx.HTTPError as e:
        logger.warning(e)
