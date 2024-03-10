from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.location import Location
from schemas.locations import LocationCreateRequest


async def get_locations(session: AsyncSession) -> List[Location]:
    result = await session.execute(select(Location).order_by(Location.key).limit(100))
    return [Location(
        id=res.id,
        key=res.key,
        name=res.name,
        parent_id=res.parent_id,
    ) for res in result.scalars().all()]


async def get_location(session: AsyncSession, location_id: int) -> Location:
    result = await session.execute(select(Location).where(Location.id == location_id))
    res = result.scalar()
    return Location(
        id=res.id,
        key=res.key,
        name=res.name,
        parent_id=res.parent_id,
    )


async def add_location(session: AsyncSession, location: LocationCreateRequest) -> Location:
    parent = await get_location(session, location.parent_id)
    if parent is None:
        raise ValueError('Invalid parent id')

    new_location = Location(id=location.id, name=location.name, parent_id=location.parent_id)
    new_location.key = f'{parent.key}-{location.id}'

    session.add(new_location)
    await session.commit()

    return new_location
