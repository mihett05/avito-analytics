from typing import List

from fastapi import HTTPException
from redis.asyncio import Redis
from starlette import status

from schemas.storage import StorageConfResponse


async def get_storage_conf(client: Redis):
    pass


storage_example: dict = {
    "baseline": int,
    "discounts": list[int],
    "analytics": {

    }
}
