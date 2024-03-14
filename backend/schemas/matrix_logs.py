from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class MatrixLogTypePydantic(str, Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class MatrixLogResponse(BaseModel):
    id: int
    matrix_id: int
    type: MatrixLogTypePydantic
    happened_at: datetime
