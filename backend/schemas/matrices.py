from typing import Optional

from pydantic import BaseModel

from models.matrix import MatrixTypeEnum


class MatrixCreateRequest(BaseModel):
    id: int
    name: str
    type: MatrixTypeEnum
    segment_id: Optional[int]


class MatrixReadCreateResponse(BaseModel):
    id: int
    name: str
    type: MatrixTypeEnum
    segment_id: Optional[int]
