from typing import Optional

from pydantic import BaseModel


class LocationCreateRequest(BaseModel):
    id: int
    name: str
    parent_id: Optional[int]


class LocationPutRequest(BaseModel):
    id: int
    key: str
    name: str
    parent_id: Optional[int]


class LocationResponse(BaseModel):
    id: int
    key: str
    name: str
    parent_id: Optional[int]
