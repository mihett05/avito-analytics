from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session
from schemas.locations import LocationCreateRequest, LocationReadCreateResponse
from services.locations import get_locations, get_location, add_location

router = APIRouter()


@router.get("/location/", tags=["locations"])
async def read_locations(session: AsyncSession = Depends(get_session)) -> List[LocationReadCreateResponse]:
    locations = await get_locations(session)
    return [LocationReadCreateResponse(
        id=location.id,
        key=location.key,
        name=location.name,
        parent_id=location.parent_id
    ) for location in locations]


@router.get("/location/{location_id}", tags=["locations"])
async def read_location(location_id: int,
                        session: AsyncSession = Depends(get_session)) -> LocationReadCreateResponse:
    location = await get_location(session, location_id)
    return LocationReadCreateResponse(
        id=location.id,
        key=location.key,
        name=location.name,
        parent_id=location.parent_id
    )


@router.post("/location/", tags=["locations"])
async def create_locations(request: LocationCreateRequest,
                           session: AsyncSession = Depends(get_session)) -> LocationReadCreateResponse:
    location = await add_location(session, request)
    return LocationReadCreateResponse(
        id=location.id,
        key=location.key,
        name=location.name,
        parent_id=location.parent_id
    )
