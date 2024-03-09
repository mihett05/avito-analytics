from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.matrices import Matrices
from schemas.categories import CategoryCreateRequest, CategoryReadRequest


async def get_matrices(session: AsyncSession) -> List[Matrices]:
    result = await session.execute(select(Matrices).order_by(Matrices.id.desc()))
    return [Matrices(res) for res in result.scalars().all()]


async def get_matrix(session: AsyncSession, matrix_id: Union[int, CategoryReadRequest]) -> Matrices:
    if isinstance(matrix_id, CategoryReadRequest):
        matrix_id = matrix_id.id

    result = await session.execute(select(Matrices).where(id=matrix_id))
    return result.scalar()


def add_matrix(session: AsyncSession, matrix: CategoryCreateRequest) -> Matrices:
    new_matrix = Matrices(id=matrix.id, name=matrix.name)
    session.add(new_matrix)

    return new_matrix

