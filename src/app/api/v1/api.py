from fastapi import APIRouter

from app.core.tags import Tags

from .endpoints import (
    nobel_laureates,
    nobel_prizes,
)

router = APIRouter()
router.include_router(
    nobel_prizes.router, prefix="/nobel-prizes", tags=[Tags.NOBEL_PRIZES.value]
)
router.include_router(
    nobel_laureates.router, prefix="/nobel-laureates", tags=[Tags.NOBEL_LAUREATES.value]
)
