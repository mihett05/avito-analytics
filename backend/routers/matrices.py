from typing import Annotated, List, Optional, Dict

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from deps.pagination import ModelTotalCount

from deps.sql_session import get_sql_session
from models import Price, Matrix
from schemas.matrices import (
    MatrixReadCreateResponse,
    MatrixCreateRequest,
    MatrixTypePydantic,
)
from services.matrices import get_matrices, get_matrix, add_matrix, delete_matrix_by_id
from services.nodes import add_prices, delete_table

router = APIRouter(tags=["matrices"])


@router.delete("/matrix")
async def delete_all_matrices(session: AsyncSession = Depends(get_sql_session)) -> Dict:
    await delete_table(session, Matrix)
    return {"status": status.HTTP_200_OK}


@router.get("/matrix")
async def read_matrices(
        total: Annotated[int, Depends(ModelTotalCount(Matrix))],
        _start: int = 1, _end: int = 50,
        session: AsyncSession = Depends(get_sql_session),
) -> List[MatrixReadCreateResponse]:
    matrices = await get_matrices(session, start=_start, end=_end)
    return [
        MatrixReadCreateResponse(
            id=matrix.id,
            name=matrix.name,
            type=matrix.type,
            segment_id=matrix.segment_id,
        )
        for matrix in matrices
    ]


@router.get("/matrix/{matrix_id}")
async def read_matrix(
        matrix_id: int, session: AsyncSession = Depends(get_sql_session)
) -> MatrixReadCreateResponse:
    matrix = await get_matrix(session, matrix_id)
    return MatrixReadCreateResponse(
        id=matrix.id, name=matrix.name, type=matrix.type, segment_id=matrix.segment_id
    )


@router.delete("/matrix/{matrix_id}")
async def delete_matrix(matrix_id: int, session: AsyncSession = Depends(get_sql_session)):
    try:
        await delete_matrix_by_id(session, matrix_id)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Matrix wasn't found",
        )

    return {"status": status.HTTP_200_OK}


@router.post("/matrix")
async def create_matrix(
        name: str,
        file: UploadFile,
        segment_id: Optional[int] = None,
        session: AsyncSession = Depends(get_sql_session)
) -> MatrixReadCreateResponse:
    try:
        # cat loc price
        matrix = await add_matrix(
            session,
            MatrixCreateRequest(
                type=(
                    MatrixTypePydantic.DISCOUNT
                    if segment_id is not None
                    else MatrixTypePydantic.BASE
                ),
                name=name,
                segment_id=segment_id,
            ),
        )  # add metadata
        await add_prices(session, file, Price, matrix)  # add data

    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid parent id\nMore info:\n\n{err}",
        )

    return MatrixReadCreateResponse(
        id=matrix.id, name=matrix.name, type=matrix.type, segment_id=matrix.segment_id
    )
