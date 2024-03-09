from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.categories import Categories
from schemas.categories import CategoryCreateRequest, CategoryReadRequest


async def get_categories(session: AsyncSession) -> List[Categories]:
    result = await session.execute(select(Categories).order_by(Categories.key.desc()))
    return [Categories(res) for res in result.scalars().all()]


async def get_category(session: AsyncSession, category_id: Union[int, CategoryReadRequest]) -> Categories:
    if isinstance(category_id, CategoryReadRequest):
        category_id = category_id.id

    result = await session.execute(select(Categories).where(id=category_id))
    return result.scalar()


def add_category(session: AsyncSession, category: CategoryCreateRequest):
    parent = await get_category(session, category.parent_id)
    if parent is None:
        ...  # TODO add raising exception

    new_category = Categories(id=category.id, name=category.name, parent_id=category.parent_id)
    new_category.key = f'{parent.key}-{category.id}'

    session.add(new_category)
    return new_category
