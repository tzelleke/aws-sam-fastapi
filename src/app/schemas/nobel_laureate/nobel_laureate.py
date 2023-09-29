from typing import ClassVar

from ..gender import Gender
from ..nobel_prize import NobelPrize
from .base_model import NobelLaureateBase


class NobelLaureate(NobelLaureateBase):
    gender: Gender | None
    birth_date: str | None
    death_date: str | None
    birth_country: str | None
    wikipedia_url: str | None
    prizes: list[NobelPrize]

    api_response_mapping: ClassVar[dict[str, str]] = {
        "birth_date": "birth.date",
        "death_date": "death.date",
        "birth_country": "birth.place.countryNow.en",
        "wikipedia_url": "wikipedia.english",
        "prizes": "nobelPrizes",
    }
