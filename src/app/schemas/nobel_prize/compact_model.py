from ..nobel_laureate import NobelLaureateCompact
from .base_model import NobelPrizeBase


class NobelPrizeCompact(NobelPrizeBase):
    laureates: list[NobelLaureateCompact] | None = None
