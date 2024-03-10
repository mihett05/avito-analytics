from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.price import Price
from schemas.prices import PriceCreateRequest, PriceReadRequest


async def get_prices(session: AsyncSession) -> List[Price]:
    result = await session.execute(select(Price))
    return [Price(
        price=res.price,
        matrix_id=res.matrix_id,
        location_id=res.location_id,
        category_id=res.category_id,
    ) for res in result.scalars().all()]


async def get_price(session: AsyncSession, req: PriceReadRequest) -> Price:
    result = await session.execute(
        select(Price).where(
            Price.matrix_id == req.matrix_id,
            Price.location_id == req.location_id,
            Price.category_id == req.category_id
        )
    )

    res = result.scalar()
    return Price(
        price=res.price,
        matrix_id=res.matrix_id,
        location_id=res.location_id,
        category_id=res.category_id,
    )


async def add_price(session: AsyncSession, price: PriceCreateRequest) -> Price:
    new_matrix = Price(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id
    )

    session.add(new_matrix)
    await session.commit()

    return new_matrix
