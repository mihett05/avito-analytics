from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session

router = APIRouter()


@router.get("/location/", tags=["locations"])
async def read_locations(session: AsyncSession = Depends(get_session)):
    pass


@router.get("/location/{location_id}", tags=["locations"])
async def read_location(location_id: int, session: AsyncSession = Depends(get_session)):
    pass


@router.post("/location/", tags=["locations"])
async def create_locations(session: AsyncSession = Depends(get_session)):
    pass
