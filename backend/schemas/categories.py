from pydantic import BaseModel


class CategoryReadRequest(BaseModel):
    id: int


class CategoryCreateRequest(BaseModel):
    id: int
    name: str
    parent_id: int


class CategoryReadCreateResponse(BaseModel):
    id: int
    key: str
    name: str
    parent_id: int
