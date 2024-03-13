from typing import List

from fastapi import HTTPException
from redis.asyncio import Redis
from redis.commands.json import JSON
from starlette import status

from schemas.storage import StorageConfResponse


async def get_storage_conf(client: Redis) -> StorageConfResponse:
    obj = await client.json().get('storage') or dict()
    print(obj)
    if obj.get('baseline') is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Storage wasn't set yet",
        )

    return StorageConfResponse(
        baseline=await obj.get('baseline'),
        discounts=await obj.get('discounts') or []
    )


async def set_baseline(client: Redis, baseline_id: int):
    await client.json().set('baseline', '$.storage', baseline_id)


async def add_discounts(client: Redis, discount_ids: List[int]):
    discount_ids = set(discount_ids) | set(await client.json().get('$.storage.discounts'))
    await client.json().set('discounts', '$.storage', list(discount_ids))


async def remove_discounts(client: Redis, discount_ids: List[int]):
    discount_ids = set(await client.json().get('$.storage.discounts')) - set(discount_ids)
    await client.json().c('discounts', list(discount_ids))
