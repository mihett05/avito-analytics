from typing import Optional

from pydantic import BaseModel


class PriceReadRequest(BaseModel):
    matrix_id: Optional[int]
    location_id: Optional[int]
    category_id: Optional[int]


class PriceCreateRequest(BaseModel):
    price: int
    matrix_id: int
    location_id: int
    category_id: int


class PriceReadCreateResponse(BaseModel):
    price: int
    matrix_id: int
    location_id: int
    category_id: int


class PriceGetRequest(BaseModel):
    location_id: int
    category_id: int
    user_id: int


class PriceGetResponse(BaseModel):
    location_id: int
    category_id: int
    matrix_id: int
    price: float
