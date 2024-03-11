from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from deps.sql_session import get_session
from models import Price
from schemas.prices import PriceReadCreateResponse, PriceReadRequest, PriceCreateRequest
from services.nodes import delete_table
from services.prices import get_prices, get_price, add_price

router = APIRouter()


@router.delete("/price", tags=["prices"])
async def delete_all_prices(session: AsyncSession = Depends(get_session)) -> Dict:
    await delete_table(session, Price)
    return {"status": status.HTTP_200_OK}


@router.get("/price", tags=["prices"])
async def read_prices(
        session: AsyncSession = Depends(get_session),
) -> List[PriceReadCreateResponse]:
    prices = await get_prices(session)
    return [
        PriceReadCreateResponse(
            price=price.price,
            matrix_id=price.matrix_id,
            location_id=price.location_id,
            category_id=price.category_id,
        )
        for price in prices
    ]


@router.get("/price/{category_id}/{location_id}/{matrix_id}", tags=["prices"])
async def read_prices(
        category_id: int,
        location_id: int,
        matrix_id: int,
        session: AsyncSession = Depends(get_session),
) -> PriceReadCreateResponse:
    price = await get_price(
        session,
        PriceReadRequest(
            category_id=category_id, location_id=location_id, matrix_id=matrix_id
        ),
    )

    return PriceReadCreateResponse(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id,
    )


@router.post("/price", tags=["prices"])
async def create_price(
        request: PriceCreateRequest, session: AsyncSession = Depends(get_session)
) -> PriceReadCreateResponse:
    try:
        price = await add_price(session, request)
    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid parent id\nMore info:\n\n{err}",
        )
    return PriceReadCreateResponse(
        price=price.price,
        matrix_id=price.matrix_id,
        location_id=price.location_id,
        category_id=price.category_id,
    )
