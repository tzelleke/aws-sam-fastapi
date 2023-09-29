# from aws_lambda_powertools.metrics import MetricUnit
from fastapi import APIRouter
from pydantic import parse_obj_as
from pydash import (
    is_none,
    omit_by,
)

from app.api.util import (
    TPaginationParams,
    TPrizeCategoryFilter,
    TPrizeYearFilter,
)
from app.core.util import logger
from app.http import http_client
from app.schemas.nobel_laureate import (
    NobelLaureate,
    NobelLaureatesResponse,
)

router = APIRouter()


@router.get("")
# @tracer.capture_method
async def get_many(
    *,
    pagination_params: TPaginationParams,
    prize_category_filter: TPrizeCategoryFilter,
    prize_year_filter: TPrizeYearFilter,
    client: http_client,
) -> NobelLaureatesResponse:
    """
    Obtain information about all Nobel Laureates
    or search for a specific set of Nobel Laureates.
    """
    params = omit_by(
        {
            **pagination_params,
            **prize_category_filter,
            **prize_year_filter.to_dict(),
        },
        is_none,
    )
    logger.debug(f"params: {params}")
    response = await client.get("/laureates", params=params)
    data = response.json()
    logger.debug(f"api response data: {data}")

    nobel_laureates = parse_obj_as(list[NobelLaureate], data["laureates"])
    meta = {"count": data["meta"]["count"]}

    return NobelLaureatesResponse(records=nobel_laureates, meta=meta)
