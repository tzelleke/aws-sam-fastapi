from typing import TypedDict

from pydantic import BaseModel

from .compact_model import NobelPrizeCompact


class NobelPrizesResponse(BaseModel):
    records: list[NobelPrizeCompact]
    meta: TypedDict("NobelPrizesMeta", {"count": int})
