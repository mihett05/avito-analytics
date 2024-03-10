from typing import List

from fastapi import APIRouter, Depends, UploadFile, Response, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from services.nodes import add_nodes_pack
from models.category import Category

from deps.sql_session import get_session
from schemas.categories import CategoryCreateRequest, CategoryReadCreateResponse
from services.categories import get_categories, get_category, add_category

router = APIRouter()


@router.get("/category", tags=["categories"])
async def read_categories(
    session: AsyncSession = Depends(get_session),
) -> List[CategoryReadCreateResponse]:
    categories = await get_categories(session)
    return [
        CategoryReadCreateResponse(
            id=category.id,
            key=category.key,
            name=category.name,
            parent_id=category.parent_id,
        )
        for category in categories
    ]


@router.get("/category/{category_id}", tags=["categories"])
async def read_category(
    category_id: int, session: AsyncSession = Depends(get_session)
) -> CategoryReadCreateResponse:
    category = await get_category(session, category_id)
    return CategoryReadCreateResponse(
        id=category.id,
        key=category.key,
        name=category.name,
        parent_id=category.parent_id,
    )


@router.post("/category", tags=["categories"])
async def create_category(
    request: CategoryCreateRequest, session: AsyncSession = Depends(get_session)
) -> CategoryReadCreateResponse:
    try:
        category = await add_category(session, request)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid parent id",
        )
    return CategoryReadCreateResponse(
        id=category.id,
        key=category.key,
        name=category.name,
        parent_id=category.parent_id,
    )


@router.post("/category/csv")
async def upload_csv(file: UploadFile, session: AsyncSession):
    try:
        await add_nodes_pack(session, file, Category)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Duplicate nodes were found or incorrect parent id's",
        )
    return Response()
