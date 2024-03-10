import httpx
from loguru import logger

from utils.env import api_schedule_endpoint, group_name


def take_schedule():
    try:
        with httpx.Client() as client:
            response = client.get(api_schedule_endpoint(),
                                  params={'name': group_name()})
            return response.json()
    except httpx.HTTPError as e:
        logger.warning(e)
