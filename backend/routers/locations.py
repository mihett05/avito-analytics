from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.location import Location
from services.nodes import read_and_add_nodes

from deps.sql_session import get_session
from schemas.locations import LocationCreateRequest, LocationReadCreateResponse
from services.locations import get_locations, get_location, add_location

router = APIRouter()


@router.get("/location", tags=["locations"])
async def read_locations(
    session: AsyncSession = Depends(get_session),
) -> List[LocationReadCreateResponse]:
    locations = await get_locations(session)
    return [
        LocationReadCreateResponse(
            id=location.id,
            key=location.key,
            name=location.name,
            parent_id=location.parent_id,
        )
        for location in locations
    ]


@router.get("/location/{location_id}", tags=["locations"])
async def read_location(
    location_id: int, session: AsyncSession = Depends(get_session)
) -> LocationReadCreateResponse:
    location = await get_location(session, location_id)
    return LocationReadCreateResponse(
        id=location.id,
        key=location.key,
        name=location.name,
        parent_id=location.parent_id,
    )


@router.post("/location", tags=["locations"])
async def create_locations(
    request: LocationCreateRequest, session: AsyncSession = Depends(get_session)
) -> LocationReadCreateResponse:
    location = await add_location(session, request)
    return LocationReadCreateResponse(
        id=location.id,
        key=location.key,
        name=location.name,
        parent_id=location.parent_id,
    )


@router.post("/location/csv")
async def upload_csv(file: UploadFile, session: AsyncSession):
    try:
        await read_and_add_nodes(session, file, Location)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate nodes were found or incorrect parent id's",
        )
    return Response()
