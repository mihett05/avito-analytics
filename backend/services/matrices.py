from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.matrix import Matrix
from schemas.matrices import MatrixCreateRequest


async def get_matrices(session: AsyncSession) -> List[Matrix]:
    result = await session.execute(select(Matrix).order_by(Matrix.id).limit(100))
    return [Matrix(
        id=res.id,
        name=res.name,
        type=res.type,
        segment_id=res.segment_id,
    ) for res in result.scalars().all()]


async def get_matrix(session: AsyncSession, matrix_id: int) -> Matrix:
    result = await session.execute(select(Matrix).where(Matrix.id == matrix_id))
    res = result.scalar()
    return Matrix(
        id=res.id,
        name=res.name,
        type=res.type,
        segment_id=res.segment_id
    )


async def add_matrix(session: AsyncSession, matrix: MatrixCreateRequest) -> Matrix:
    new_matrix = Matrix(
        name=matrix.name,
        type=matrix.type,
        segment_id=matrix.segment_id,
    )

    session.add(new_matrix)
    await session.commit()

    return new_matrix
