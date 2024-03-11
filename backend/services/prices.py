from typing import List

from redis.asyncio import Redis
from sqlalchemy import select, text, bindparam
from sqlalchemy.ext.asyncio import AsyncSession

from models.price import Price
from schemas.prices import PriceCreateRequest, PriceGetResponse, PriceReadRequest
from services.categories import get_category
from services.locations import get_location
from services.segments import get_segments_by_user_id
from storage.engine import get_storage_conf


async def get_prices(session: AsyncSession) -> List[Price]:
    result = await session.execute(
        select(Price)
        .order_by(Price.category_id, Price.location_id, Price.matrix_id)
        .limit(100)
    )

    return [
        Price(
            price=res.price,
            matrix_id=res.matrix_id,
            location_id=res.location_id,
            category_id=res.category_id,
        )
        for res in result.scalars().all()
    ]


async def get_price(session: AsyncSession, req: PriceReadRequest) -> Price:
    result = await session.execute(
        select(Price).where(
            Price.matrix_id == req.matrix_id,
            Price.location_id == req.location_id,
            Price.category_id == req.category_id,
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
        category_id=price.category_id,
    )

    session.add(new_matrix)
    await session.commit()

    return new_matrix


async def get_target_price(
        session: AsyncSession,
        user_id: int,
        category_id: int,
        location_id: int,
        redis_session: Redis
) -> list[PriceGetResponse]:

    locations = list(map(int, (await get_location(session, location_id)).key.split("-")))
    categories = list(map(int, (await get_category(session, category_id)).key.split("-")))

    segments = await get_segments_by_user_id(user_id)
    storage = await get_storage_conf(redis_session)

    statement = text(
        """
        SELECT
            prices.location_id, prices.category_id, prices.matrix_id, matrices.segment_id, prices.price
        FROM prices
        INNER JOIN matrices ON
            prices.matrix_id = matrices.id AND
            prices.location_id IN :locations AND
            prices.category_id IN :categories AND
            matrices.segment_id IS NULL OR matrices.segment_id IN :segments
        ORDER BY prices.category_id DESC, prices.location_id DESC
        """
    )
    statement = (
        statement.bindparams(bindparam("locations", expanding=True))
        .bindparams(bindparam("categories", expanding=True))
        .bindparams(bindparam("segments", expanding=True))
    )

    rows = (
        await session.execute(
            statement,
            {
                "locations": locations,
                "categories": categories,
                "segments": segments or [],
            },
        )
    ).all()
    result = [
        PriceGetResponse(
            location_id=location_id,
            category_id=category_id,
            matrix_id=matrix_id,
            price=price,
        )
        for location_id, category_id, matrix_id, segment_id, price in rows
    ]
    return result
