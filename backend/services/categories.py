from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.category import Category
from schemas.categories import CategoryCreateRequest, CategoryReadRequest


async def get_categories(session: AsyncSession) -> List[Category]:
    result = await session.execute(select(Category).order_by(Category.key.desc()))
    return [Category(res) for res in result.scalars().all()]


async def get_category(session: AsyncSession, category_id: Union[int, CategoryReadRequest]) -> Category:
    if isinstance(category_id, CategoryReadRequest):
        category_id = category_id.id

    result = await session.execute(select(Category).where(id=category_id))
    return result.scalar()


def add_category(session: AsyncSession, category: CategoryCreateRequest):
    parent = await get_category(session, category.parent_id)
    if parent is None:
        ...  # TODO add raising exception

    new_category = Category(id=category.id, name=category.name, parent_id=category.parent_id)
    new_category.key = f'{parent.key}-{category.id}'

    session.add(new_category)
    return new_category
