__all__ = ("main_router",)

from fastapi import APIRouter
from .hash_crd_views import router as hash_router

main_router = APIRouter(prefix="/api/v1")
main_router.include_router(hash_router)
