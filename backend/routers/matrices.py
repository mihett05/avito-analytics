from typing import List, Optional, Dict

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from deps.sql_session import get_session
from models import Price, Matrix
from schemas.matrices import MatrixReadCreateResponse, MatrixCreateRequest, MatrixTypePydantic
from services.matrices import get_matrices, get_matrix, add_matrix
from services.nodes import add_prices, delete_table

router = APIRouter()


@router.delete("/matrix", tags=["matrices"])
async def delete_all_matrices(session: AsyncSession = Depends(get_session)) -> Dict:
    await delete_table(session, Matrix)
    return {"status": status.HTTP_200_OK}


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
        name: str, file: UploadFile, segment_id: Optional[int] = None, session: AsyncSession = Depends(get_session)
) -> MatrixReadCreateResponse:
    try:
        # cat loc price
        matrix = await add_matrix(session, MatrixCreateRequest(
            type=MatrixTypePydantic.DISCOUNT if segment_id is not None else MatrixTypePydantic.BASE,
            name=name,
            segment_id=segment_id
        ))  # add metadata
        await add_prices(session, file, Price, matrix)  # add data

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
