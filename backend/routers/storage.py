from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, UploadFile, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session
from models.location import Location
from schemas.locations import LocationCreateRequest, LocationReadCreateResponse
from services.locations import get_locations, get_location, add_location
from services.nodes import add_nodes_pack

router = APIRouter()


@router.get("/storage/configuration", tags=["storage"])
async def read_storage(session: AsyncSession = Depends(get_session)) -> None:
    pass


@router.post("/storage/baseline", tags=["storage"])
async def set_baseline(session: AsyncSession = Depends(get_session)) -> None:
    pass


@router.post("/storage/discounts", tags=["storage"])
async def add_discounts(session: AsyncSession = Depends(get_session)) -> None:
    pass


@router.delete("/storage/discounts", tags=["storage"])
async def delete_discounts(session: AsyncSession = Depends(get_session)) -> None:
    pass
