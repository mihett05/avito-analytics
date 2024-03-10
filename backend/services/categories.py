from typing import List

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models.category import Category
from schemas.categories import CategoryCreateRequest


async def get_categories(session: AsyncSession) -> List[Category]:
    result = await session.execute(select(Category).order_by(Category.key).limit(100))
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
    result = await session.execute(select(Category).where(Category.id == category_id))
    res = result.scalar()
    return Category(
        id=res.id,
        key=res.key,
        name=res.name,
        parent_id=res.parent_id,
    )


async def add_category(
    session: AsyncSession, category: CategoryCreateRequest
) -> Category:
    parent = await get_category(session, category.parent_id)
    if parent is None:
        raise ValueError('Invalid parent id')

    new_category = Category(
        id=category.id, name=category.name, parent_id=category.parent_id
    )
    new_category.key = f"{parent.key}-{category.id}"

    session.add(new_category)
    await session.commit()

    return new_category
