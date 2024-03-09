from pydantic import BaseModel


class LocationCreateRequest(BaseModel):
    id: int
    name: str
    parent_id: int


class LocationReadCreateResponse(BaseModel):
    id: int
    key: str
    name: str
    parent_id: int
