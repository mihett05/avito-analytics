from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.price import Price
from schemas.prices import PriceCreateRequest, PriceReadRequest


async def get_prices(session: AsyncSession) -> List[Price]:
    result = await session.execute(select(Price))
    return [Price(res) for res in result.scalars().all()]


async def get_price(session: AsyncSession, req: PriceReadRequest) -> Price:
    result = await session.execute(select(Price).where(matrix_id=req.matrix_id, location_id=req.location_id,
                                                       category_id=req.category_id))
    return result.scalar()


def add_price(session: AsyncSession, matrix: PriceCreateRequest) -> Price:
    new_matrix = Price(id=matrix.id, name=matrix.name)
    session.add(new_matrix)

    return new_matrix
