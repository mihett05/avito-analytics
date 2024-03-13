from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.matriciets_logs import MatrixLogs
from schemas.matrix_logs import MatrixLogCreateRequest


async def get_matrices_logs(session: AsyncSession, start: int = 1, end: int = 50) -> List[MatrixLogs]:
    page = end - start + 1
    result = await session.execute(
        select(MatrixLogs)
        .offset(page * (start // page))
        .limit(page)
        .order_by(MatrixLogs.happened_at.desc())
    )

    return [
        MatrixLogs(id=res.id, matrix_id=res.matrix_id, type=res.type, happened_at=res.happened_at)
        for res in result.scalars().all()
    ]


async def get_matrix_logs(session: AsyncSession, matrix_id: int, start: int = 1, end: int = 50) -> List[MatrixLogs]:
    page = end - start + 1
    result = await session.execute(
        select(MatrixLogs)
        .where(MatrixLogs.matrix_id == matrix_id)
        .offset(page * (start // page))
        .limit(page)
        .order_by(MatrixLogs.happened_at.desc())
    )

    return [
        MatrixLogs(id=res.id, matrix_id=res.matrix_id, type=res.type, happened_at=res.happened_at)
        for res in result.scalars().all()
    ]


async def add_matrix_log(session: AsyncSession, matrix: MatrixLogCreateRequest) -> MatrixLogs:
    new_matrix = MatrixLogs(matrix_id=matrix.matrix_id, type=matrix.type)

    session.add(new_matrix)
    await session.commit()

    return new_matrix
