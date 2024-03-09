from fastapi import APIRouter

from .prices import router as prc_router
from .matrices import router as mat_router
from .locations import router as loc_router
from .categories import router as cat_router

api = APIRouter()

api.include_router(prc_router)
api.include_router(mat_router)
api.include_router(loc_router)
api.include_router(cat_router)
