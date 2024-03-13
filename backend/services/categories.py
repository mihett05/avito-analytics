from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from models.category import Category
from schemas.categories import CategoryCreateRequest


async def get_categories(
    session: AsyncSession, start: int = None, end: int = None
) -> List[Category]:
    query = select(Category)
    if start is not None and end is not None:
        query = query.where(start <= Category.id, Category.id <= end)
    result = await session.execute(query)

    return [
        Category(
            id=res.id,
            key=res.key,
            name=res.name,
            parent_id=res.parent_id,
        )
        for res in result.scalars().all()
    ]


async def get_category(session: AsyncSession, category_id: int) -> Category:
    result = (
        await session.execute(select(Category).where(Category.id == category_id))
    ).scalar()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid category id"
        )

    return Category(
        id=result.id,
        key=result.key,
        name=result.name,
        parent_id=result.parent_id,
    )


async def add_category(
    session: AsyncSession, category: CategoryCreateRequest
) -> Category:
    parent = await get_category(session, category.parent_id)
    if parent is None:
        raise ValueError("Invalid parent id")

    new_category = Category(
        id=category.id, name=category.name, parent_id=category.parent_id
    )
    new_category.key = f"{category.id}-{parent.key}"

    session.add(new_category)
    await session.commit()

    return new_category
