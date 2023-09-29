from typing import TypedDict

from pydantic import BaseModel

from .nobel_laureate import NobelLaureate


class NobelLaureatesResponse(BaseModel):
    records: list[NobelLaureate]
    meta: TypedDict("NobelLaureatesMeta", {"count": int})
