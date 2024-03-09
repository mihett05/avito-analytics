from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from deps.sql_session import get_session

router = APIRouter()


@router.get("/matrix/", tags=["matrices"])
async def read_matrices(session: AsyncSession = Depends(get_session)):
    pass


@router.get("/matrix/{matrix_id}", tags=["matrices"])
async def read_matrix(matrix_id: int, session: AsyncSession = Depends(get_session)):
    pass


@router.post("/matrix/", tags=["matrices"])
async def create_matrices(session: AsyncSession = Depends(get_session)):
    pass


@router.patch("/matrix/{matrix_id}", tags=["matrices"])
async def update_matrix(matrix_id: int, session: AsyncSession = Depends(get_session)):
    pass
