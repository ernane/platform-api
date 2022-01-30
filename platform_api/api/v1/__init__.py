from fastapi import APIRouter

from platform_api.api.v1.resources import items


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(items.router, prefix="/items", tags=["items"])
    return api_router