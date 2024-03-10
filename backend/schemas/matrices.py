from enum import Enum
from typing import Optional

from pydantic import BaseModel


class MatrixTypePydantic(str, Enum):
    BASE = 'BASE'
    DISCOUNT = 'DISCOUNT'


class MatrixCreateRequest(BaseModel):
    id: int
    name: str
    type: MatrixTypePydantic
    segment_id: Optional[int]


class MatrixReadCreateResponse(BaseModel):
    id: int
    name: str
    type: MatrixTypePydantic
    segment_id: Optional[int]
