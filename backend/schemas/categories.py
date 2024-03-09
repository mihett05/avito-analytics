from typing import Optional

from pydantic import BaseModel


class CategoryCreateRequest(BaseModel):
    id: int
    name: str
    parent_id: int


class CategoryReadCreateResponse(BaseModel):
    id: int
    key: str
    name: str
    parent_id: Optional[int]
