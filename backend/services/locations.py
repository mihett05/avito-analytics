from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.locations import Locations
from schemas.locations import LocationCreateRequest, LocationReadRequest


async def get_locations(session: AsyncSession) -> List[Locations]:
    result = await session.execute(select(Locations).order_by(Locations.key.desc()))
    return [Locations(res) for res in result.scalars().all()]


async def get_location(session: AsyncSession, location_id: Union[int, LocationReadRequest]) -> Locations:
    if isinstance(location_id, LocationReadRequest):
        location_id = location_id.id

    result = await session.execute(select(Locations).where(id=location_id))
    return result.scalar()


def add_location(session: AsyncSession, location: LocationCreateRequest) -> Locations:
    parent = await get_location(session, location.parent_id)
    if parent is None:
        ...  # TODO add raising exception

    new_location = Locations(id=location.id, name=location.name, parent_id=location.parent_id)
    new_location.key = f'{parent.key}-{location.id}'

    session.add(new_location)
    return new_location
