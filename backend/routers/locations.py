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
async def create_location(
    request: LocationCreateRequest, session: AsyncSession = Depends(get_session)
) -> LocationReadCreateResponse:
    try:
        location = await add_location(session, request)
    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid parent id\nMore info:\n\n{err}",
        )

    return LocationReadCreateResponse(
        id=location.id,
        key=location.key,
        name=location.name,
        parent_id=location.parent_id,
    )


@router.post("/location/csv", tags=["locations"])
async def upload_csv(file: UploadFile, session: AsyncSession = Depends(get_session)):
    try:
        await add_nodes_pack(session, file, Location)
    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid parent id\nMore info:\n\n{err}",
        )

    return Response({'status': status.HTTP_200_OK})
