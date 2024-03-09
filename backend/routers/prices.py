from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session

router = APIRouter()


@router.get("/category/", tags=["categories"])
async def read_categories(session: AsyncSession = Depends(get_session)):
    pass


@router.get("/category/{category_id}", tags=["categories"])
async def read_category(category_id: int, session: AsyncSession = Depends(get_session)):
    pass


@router.post("/category/", tags=["categories"])
async def create_categories(session: AsyncSession = Depends(get_session)):
    pass
