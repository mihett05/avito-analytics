from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.matrix import Matrix
from schemas.categories import CategoryCreateRequest, CategoryReadRequest


async def get_matrices(session: AsyncSession) -> List[Matrix]:
    result = await session.execute(select(Matrix).order_by(Matrix.id.desc()))
    return [Matrix(res) for res in result.scalars().all()]


async def get_matrix(session: AsyncSession, matrix_id: Union[int, CategoryReadRequest]) -> Matrix:
    if isinstance(matrix_id, CategoryReadRequest):
        matrix_id = matrix_id.id

    result = await session.execute(select(Matrix).where(id=matrix_id))
    return result.scalar()


def add_matrix(session: AsyncSession, matrix: CategoryCreateRequest) -> Matrix:
    new_matrix = Matrix(id=matrix.id, name=matrix.name)
    session.add(new_matrix)

    return new_matrix

