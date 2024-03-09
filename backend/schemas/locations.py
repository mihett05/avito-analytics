from pydantic import BaseModel


class LocationReadCreateResponse(BaseModel):
    id: int
    key: str
    name: str
    parent_id: int


class LocationCreateRequest(BaseModel):
    id: int
    name: str
    parent_id: int


class LocationReadRequest(BaseModel):
    id: int
