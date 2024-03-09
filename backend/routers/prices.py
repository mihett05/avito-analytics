from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session
from schemas.prices import PriceReadCreateResponse, PriceReadRequest, PriceCreateRequest
from services.prices import get_prices, get_price, add_price

router = APIRouter()


@router.get("/prices/", tags=["prices"])
async def read_prices(request: Optional[PriceReadRequest], session: AsyncSession = Depends(get_session)):
    if request is None:  # if list was requested
        prices = await get_prices(session)
        return [PriceReadCreateResponse(
            price=price.price,
            matrix_id=price.matrix_id,
            location_id=price.location_id,
            category_id=price.category_id
        ) for price in prices]

    # if current price was requested
    price = await get_price(session, request)
    return PriceReadCreateResponse(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id
    )


@router.post("/prices/", tags=["prices"])
async def create_price(request: PriceCreateRequest, session: AsyncSession = Depends(get_session)):
    price = await add_price(session, request)
    return PriceReadCreateResponse(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id
    )
