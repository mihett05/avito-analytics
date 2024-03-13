from typing import List

from fastapi import HTTPException
from redis.asyncio import Redis
from starlette import status

from schemas.storage import StorageConfResponse


async def get_storage_conf(client: Redis) -> StorageConfResponse:
    if not await client.hget('storage', 'baseline'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Storage wasn't set yet",
        )

    return StorageConfResponse(
        baseline=await client.hget('storage', 'baseline'),
        discounts=await client.hget('storage', 'discounts') or []
    )


async def set_baseline(client: Redis, baseline_id: int):
    await client.hset(
        name='storage',
        key='baseline',
        value=baseline_id,
    )


async def add_discounts(client: Redis, discount_ids: List[int]):
    await client.sadd('discounts', *set(discount_ids))


async def remove_discounts(client: Redis, discount_ids: List[int]):
    await client.srem('discounts', *set(discount_ids))
