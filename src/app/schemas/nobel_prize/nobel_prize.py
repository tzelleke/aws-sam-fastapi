from typing import ClassVar

from ..prize_portion import PrizePortion
from ..prize_status import PrizeStatus
from .base_model import NobelPrizeBase


class NobelPrize(NobelPrizeBase):
    sort_order: int
    portion: PrizePortion
    prize_status: PrizeStatus
    motivation: str

    api_response_mapping: ClassVar[dict[str, str]] = {
        **NobelPrizeBase.api_response_mapping,
        "sort_order": "sortOrder",
        "prize_status": "prizeStatus",
        "motivation": "motivation.en",
    }
