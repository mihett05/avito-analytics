from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.location import Location
from schemas.locations import LocationCreateRequest


async def get_locations(session: AsyncSession) -> List[Location]:
    result = await session.execute(select(Location))
    return [Location(res) for res in result.scalars().all()]


async def get_location(session: AsyncSession, location_id: int) -> Location:
    result = await session.execute(select(Location).where(id=location_id))
    return result.scalar()


async def add_location(session: AsyncSession, location: LocationCreateRequest) -> Location:
    parent = await get_location(session, location.parent_id)
    if parent is None:
        ...  # TODO add raising exception

    new_location = Location(id=location.id, name=location.name, parent_id=location.parent_id)
    new_location.key = f'{parent.key}-{location.id}'

    session.add(new_location)
    await session.commit()

    return new_location
