from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.matrix import Matrix
from schemas.matrices import MatrixCreateRequest


async def get_matrices(session: AsyncSession) -> List[Matrix]:
    result = await session.execute(select(Matrix))
    return [Matrix(res) for res in result.scalars().all()]


async def get_matrix(session: AsyncSession, matrix_id: int) -> Matrix:
    result = await session.execute(select(Matrix).where(id=matrix_id))
    return result.scalar()


async def add_matrix(session: AsyncSession, matrix: MatrixCreateRequest) -> Matrix:
    new_matrix = Matrix(id=matrix.id, name=matrix.name)

    session.add(new_matrix)
    await session.commit()

    return new_matrix
