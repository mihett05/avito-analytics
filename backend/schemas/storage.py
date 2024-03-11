from typing import List

from pydantic import BaseModel


class StorageConfResponse(BaseModel):
    baseline: int
    discounts: List[int]


class AddDeleteDiscountsRequest(BaseModel):
    discounts: List[int]
