from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session
from schemas.matrices import MatrixReadCreateResponse, MatrixCreateRequest
from services.matrices import get_matrices, get_matrix, add_matrix

router = APIRouter()


@router.get("/matrix/", tags=["matrices"])
async def read_matrices(session: AsyncSession = Depends(get_session)) -> List[MatrixReadCreateResponse]:
    matrices = await get_matrices(session)

    return [MatrixReadCreateResponse(
        id=matrix.id,
        name=matrix.name,
        type=matrix.type,
        segment_id=matrix.segment_id,
    ) for matrix in matrices]


@router.get("/matrix/{matrix_id}", tags=["matrices"])
async def read_matrix(matrix_id: int,
                      session: AsyncSession = Depends(get_session)) -> MatrixReadCreateResponse:
    matrix = await get_matrix(session, matrix_id)
    return MatrixReadCreateResponse(
        id=matrix.id,
        name=matrix.name,
        type=matrix.type,
        segment_id=matrix.segment_id
    )


@router.post("/matrix/", tags=["matrices"])
async def create_matrices(request: MatrixCreateRequest,
                          session: AsyncSession = Depends(get_session)) -> MatrixReadCreateResponse:
    matrix = await add_matrix(session, request)
    return MatrixReadCreateResponse(
        id=matrix.id,
        name=matrix.name,
        type=matrix.type,
        segment_id=matrix.segment_id
    )


@router.patch("/matrix/{matrix_id}", tags=["matrices"])
async def update_matrix(matrix_id: int, session: AsyncSession = Depends(get_session)) -> MatrixReadCreateResponse:
    pass
