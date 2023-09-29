from typing import ClassVar

from ..prize_portion import PrizePortion
from .base_model import NobelLaureateBase


class NobelLaureateCompact(NobelLaureateBase):
    sort_order: int
    portion: PrizePortion
    motivation: str

    api_response_mapping: ClassVar[dict[str, str]] = {
        **NobelLaureateBase.api_response_mapping,
        "sort_order": "sortOrder",
        "motivation": "motivation.en",
    }
