from datetime import date
from typing import ClassVar

from ..base_model import BaseModel
from ..prize_category import PrizeCategory


class NobelPrizeBase(BaseModel):
    award_year: int
    category: PrizeCategory
    date_awarded: date | None

    api_response_mapping: ClassVar[dict[str, str]] = {
        "award_year": "awardYear",
        "category": "category.en",
        "date_awarded": "dateAwarded",
    }
