from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session

router = APIRouter()


@router.get("/prices/", tags=["prices"])
async def read_categories(session: AsyncSession = Depends(get_session)):
    pass


@router.get("/prices/{price_id}", tags=["prices"])
async def read_category(price_id: int, session: AsyncSession = Depends(get_session)):
    pass


@router.post("/prices/", tags=["prices"])
async def create_categories(session: AsyncSession = Depends(get_session)):
    pass
