from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session

router = APIRouter(tags=["storage"])


@router.get("/storage/configuration")
async def read_storage(session: AsyncSession = Depends(get_session)) -> None:
    pass


@router.post("/storage/baseline")
async def set_baseline(session: AsyncSession = Depends(get_session)) -> None:
    pass


@router.post("/storage/discounts")
async def add_discounts(session: AsyncSession = Depends(get_session)) -> None:
    pass


@router.delete("/storage/discounts")
async def delete_discounts(session: AsyncSession = Depends(get_session)) -> None:
    pass
