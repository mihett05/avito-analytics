from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.category import Category
from schemas.categories import CategoryCreateRequest


async def get_categories(session: AsyncSession) -> List[Category]:
    result = await session.execute(select(Category))
    return [Category(res) for res in result.scalars().all()]


async def get_category(session: AsyncSession, category_id: int) -> Category:
    result = await session.execute(select(Category).where(id=category_id))
    return result.scalar()


async def add_category(session: AsyncSession, category: CategoryCreateRequest) -> Category:
    parent = await get_category(session, category.parent_id)
    if parent is None:
        ...  # TODO add raising exception

    new_category = Category(id=category.id, name=category.name, parent_id=category.parent_id)
    new_category.key = f'{parent.key}-{category.id}'

    session.add(new_category)
    await session.commit()

    return new_category
