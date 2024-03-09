from typing import Optional

from pydantic import BaseModel


class MatrixReadRequest(BaseModel):
    id: int


class MatrixCreateRequest(BaseModel):
    id: int
    name: str
    segment_id: Optional[int]


class MatrixReadCreateResponse(BaseModel):
    id: int
    name: str
    segment_id: Optional[int]
