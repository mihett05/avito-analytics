from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session
from schemas.categories import CategoryCreateRequest, CategoryReadCreateResponse
from services.categories import get_categories, get_category, add_category

router = APIRouter()


@router.get("/category/", tags=["categories"])
async def read_categories(session: AsyncSession = Depends(get_session)):
    categories = await get_categories(session)
    return [CategoryReadCreateResponse(
        id=category.id,
        key=category.key,
        name=category.name,
        parent_id=category.parent_id,
    ) for category in categories]


@router.get("/category/{category_id}", tags=["categories"])
async def read_category(category_id: int, session: AsyncSession = Depends(get_session)):
    category = await get_category(session, category_id)
    return CategoryReadCreateResponse(
        id=category.id,
        key=category.key,
        name=category.name,
        parent_id=category.parent_id,
    )


@router.post("/category/", tags=["categories"])
async def create_categories(request: CategoryCreateRequest, session: AsyncSession = Depends(get_session)):
    category = await add_category(session, request)
    return CategoryReadCreateResponse(
        id=category.id,
        key=category.key,
        name=category.name,
        parent_id=category.parent_id
    )
