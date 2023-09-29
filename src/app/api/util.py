from enum import Enum
from typing import Annotated

from fastapi import (
    Depends,
    Query,
)
from fastapi.exceptions import RequestValidationError


def pagination_params(
    offset: Annotated[
        int | None,
        Query(
            ge=0,
            description="Pagination: defines the number of records to skip before returning the result.",  # noqa: E501
        ),
    ] = None,
    limit: Annotated[
        int,
        Query(
            ge=1,
            description="Pagination: defines the number of records to return in the result.",  # noqa: E501
        ),
    ] = 10,
) -> dict[str, int]:
    return {"offset": offset, "limit": limit}


TPaginationParams = Annotated[dict[str, int], Depends(pagination_params)]


class PrizeCategoryAbbreviation(str, Enum):
    PHYSICS = "phy"
    CHEMISTRY = "che"
    PHYSIOLOGY_OR_MEDICINE = "med"
    PEACE = "pea"
    LITERATURE = "lit"
    ECONOMIC_SCIENCES = "eco"


def prize_category_filter(
    prize_category: Annotated[
        PrizeCategoryAbbreviation | None,
        Query(
            alias="nobel-prize-category",
            description="Filters the result by Nobel Prize Category.",
        ),
    ] = None,
) -> dict[str, str]:
    return {"nobelPrizeCategory": prize_category.value if prize_category else None}


TPrizeCategoryFilter = Annotated[dict[str, str], Depends(prize_category_filter)]


class PrizeYearFilter:
    def __init__(
        self,
        prize_year: Annotated[
            int | None,
            Query(
                ge=1901,
                alias="nobel-prize-year",
                description="Filters the result by Nobel Prize Award Year.",
            ),
        ] = None,
        prize_year_to: Annotated[
            int | None,
            Query(
                ge=1901,
                alias="nobel-prize-year-to",
                description="Used in combination with nobel-prize-year. Allows to filter the result by a range of Nobel Prize Years.",  # noqa: E501
            ),
        ] = None,
    ):
        self.prize_year = prize_year
        self.prize_year_to = prize_year_to
        if self.prize_year_to and not self.prize_year:
            raise RequestValidationError(
                [
                    {
                        "loc": ["query", "nobel-prize-year-to"],
                        "msg": "Nobel-prize-year-to requires nobel-prize-year",
                        "type": "value_error",
                    }
                ]
            )
        if (
            self.prize_year_to
            and self.prize_year
            and self.prize_year_to < self.prize_year
        ):
            raise RequestValidationError(
                [
                    {
                        "loc": ["query", "nobel-prize-year-to"],
                        "msg": "Nobel-prize-year-to must not be smaller than nobel-prize-year",  # noqa: E501
                        "type": "value_error",
                    }
                ]
            )

    def to_dict(self) -> dict[str, int]:
        return {
            "nobelPrizeYear": self.prize_year,
            "yearTo": self.prize_year_to,
        }


TPrizeYearFilter = Annotated[PrizeYearFilter, Depends(PrizeYearFilter)]
