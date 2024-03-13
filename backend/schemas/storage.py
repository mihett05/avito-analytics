from typing import List

from pydantic import BaseModel


class StorageConfResponse(BaseModel):
    baseline: int
    discounts: List[int]


class SetDiscountsRequest(BaseModel):
    discounts: List[int]
