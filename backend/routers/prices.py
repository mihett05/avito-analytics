from typing import Annotated, List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from deps.pagination import ModelTotalCount

from deps.sql_session import get_session
from models import Price
from schemas.prices import (
    PriceReadCreateResponse,
    PriceReadRequest,
    PriceCreateRequest,
    PriceGetRequest,
    PriceGetResponse,
)
from services.nodes import delete_table
from services.prices import get_prices, get_price, add_price, get_target_price

router = APIRouter(tags=["prices"])


@router.post("/price/target")
async def calcualte_target_price(
    body: PriceGetRequest, session: AsyncSession = Depends(get_session)
):
    return await get_target_price(
        session=session,
        category_id=body.category_id,
        location_id=body.location_id,
        user_id=body.user_id,
    )


@router.delete("/price")
async def delete_all_prices(session: AsyncSession = Depends(get_session)) -> Dict:
    await delete_table(session, Price)
    return {"status": status.HTTP_200_OK}


@router.get("/price")
async def read_prices(
    total: Annotated[int, Depends(ModelTotalCount(Price))],
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


@router.get("/price/{category_id}/{location_id}/{matrix_id}")
async def read_price(
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


@router.post("/price")
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
