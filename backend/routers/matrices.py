from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from deps.sql_session import get_session
from models import Price
from schemas.matrices import MatrixReadCreateResponse, MatrixCreateRequest, MatrixTypePydantic
from services.matrices import get_matrices, get_matrix, add_matrix
from services.nodes import add_nodes_pack, add_prices

router = APIRouter()


@router.get("/matrix", tags=["matrices"])
async def read_matrices(
        session: AsyncSession = Depends(get_session),
) -> List[MatrixReadCreateResponse]:
    matrices = await get_matrices(session)
    return [
        MatrixReadCreateResponse(
            id=matrix.id,
            name=matrix.name,
            type=matrix.type,
            segment_id=matrix.segment_id,
        )
        for matrix in matrices
    ]


@router.get("/matrix/{matrix_id}", tags=["matrices"])
async def read_matrix(
        matrix_id: int, session: AsyncSession = Depends(get_session)
) -> MatrixReadCreateResponse:
    matrix = await get_matrix(session, matrix_id)
    return MatrixReadCreateResponse(
        id=matrix.id,
        name=matrix.name,
        type=matrix.type,
        segment_id=matrix.segment_id
    )


@router.post("/matrix", tags=["matrices"])
async def create_matrix(
        request: MatrixCreateRequest, file: UploadFile, session: AsyncSession = Depends(get_session)
) -> MatrixReadCreateResponse:
    try:
        if request.segment_id is not None:
            request.type = MatrixTypePydantic.DISCOUNT

        matrix = await add_matrix(session, request)  # add metadata
        await add_prices(session, file, Price)  # add data

    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid parent id\nMore info:\n\n{err}",
        )

    return MatrixReadCreateResponse(
        id=matrix.id,
        name=matrix.name,
        type=matrix.type,
        segment_id=matrix.segment_id
    )


@router.patch("/matrix/{matrix_id}", tags=["matrices"])
async def update_matrix(
        matrix_id: int, session: AsyncSession = Depends(get_session)
) -> MatrixReadCreateResponse:
    pass
