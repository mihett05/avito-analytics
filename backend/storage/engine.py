from typing import List, Union, Dict

import redis.asyncio as redis
from fastapi import HTTPException
from redis.asyncio import Redis
from starlette import status

from config import get_config
from schemas.storage import StorageConfResponse

config = get_config()

redis_url = f"redis://{config.REDIS_USER}:{config.REDIS_PASSWORD}@{config.REDIS_HOST}:{config.REDIS_PORT}"
pool = redis.ConnectionPool.from_url(redis_url)


async def get_storage_conf(client: Redis) -> StorageConfResponse:
    if not await client.get('baseline'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Storage wasn't set yet",
        )

    return StorageConfResponse(
        baseline=await client.get('baseline'),
        discounts=await client.smembers('discounts') or []
    )


async def set_baseline(client: Redis, baseline_id: int):
    await client.set('baseline', baseline_id)


async def add_discounts(client: Redis, discount_ids: List[int]):
    await client.sadd('discounts', *set(discount_ids))


async def remove_discounts(client: Redis, discount_ids: List[int]):
    await client.srem('discounts', *set(discount_ids))
