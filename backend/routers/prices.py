from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session
from schemas.prices import PriceReadCreateResponse, PriceReadRequest, PriceCreateRequest
from services.prices import get_prices, get_price, add_price

router = APIRouter()


@router.get("/prices/", tags=["prices"])
async def read_prices(session: AsyncSession = Depends(get_session)) -> List[PriceReadCreateResponse]:
    prices = await get_prices(session)
    return [PriceReadCreateResponse(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id
    ) for price in prices]


@router.get("/prices/{category_id}/{location_id}/{matrix_id}", tags=["prices"])
async def read_prices(category_id: int,
                      location_id: int,
                      matrix_id: int,
                      session: AsyncSession = Depends(get_session)) -> PriceReadCreateResponse:
    price = await get_price(session, PriceReadRequest(category_id=category_id,
                                                      location_id=location_id,
                                                      matrix_id=matrix_id))

    return PriceReadCreateResponse(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id
    )


@router.post("/prices/", tags=["prices"])
async def create_price(request: PriceCreateRequest,
                       session: AsyncSession = Depends(get_session)) -> PriceReadCreateResponse:
    price = await add_price(session, request)
    return PriceReadCreateResponse(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id
    )
