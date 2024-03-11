from fastapi import APIRouter, Depends
from redis.asyncio import Redis
from starlette import status

from deps.redis_session import get_redis_session
import storage.engine as engine
from schemas.storage import AddDeleteDiscountsRequest, StorageConfResponse

router = APIRouter(tags=["storage"])


@router.get("/storage/configuration")
async def read_storage(session: Redis = Depends(get_redis_session)) -> StorageConfResponse:
    return await engine.get_storage_conf(session)


@router.post("/storage/baseline")
async def set_baseline(baseline: int, session: Redis = Depends(get_redis_session)):
    await engine.set_baseline(session, baseline)
    return {'status': status.HTTP_200_OK}


@router.post("/storage/discounts")
async def add_discounts(discount: AddDeleteDiscountsRequest, session: Redis = Depends(get_redis_session)):
    await engine.add_discounts(session, discount.discounts)
    return {'status': status.HTTP_200_OK}


@router.delete("/storage/discounts")
async def delete_discounts(discount: AddDeleteDiscountsRequest, session: Redis = Depends(get_redis_session)):
    await engine.remove_discounts(session, discount.discounts)
    return {'status': status.HTTP_200_OK}
