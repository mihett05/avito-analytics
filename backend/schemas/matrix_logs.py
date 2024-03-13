from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class MatrixLogTypePydantic(str, Enum):
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'


class MatrixLogCreateRequest(BaseModel):
    matrix_id: int
    type: MatrixLogTypePydantic = MatrixLogTypePydantic.CREATE


class MatrixLogResponse(BaseModel):
    id: int
    matrix_id: int
    type: MatrixLogTypePydantic
    happened_at: datetime
