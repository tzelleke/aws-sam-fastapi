from typing import Any

from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

# from aws_lambda_powertools.metrics import MetricUnit
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.core.config import get_settings
from app.core.metadata import (
    description,
    license,
    summary,
)
from app.core.tags import (
    Tags,
    tags_metadata,
)
from app.core.util import logger

app = FastAPI(
    root_path=get_settings().root_path,
    title=get_settings().app_name,
    version=get_settings().version,
    summary=summary,
    description=description,
    openapi_tags=tags_metadata,
    license_info=license,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=[Tags.OPERATIONS], description="Health check")
async def healthcheck() -> dict[str, str]:
    return {"status": "OK"}


@app.get("/", tags=[Tags.ROOT], description="Root")
# @tracer.capture_method
async def root() -> dict[str, str]:
    # metrics.add_metric(name="RootInvocations", unit=MetricUnit.Count, value=1)
    logger.info("root() - HTTP 200")
    return {"message": "Hello World!"}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
# @tracer.capture_lambda_handler
# @metrics.log_metrics(capture_cold_start_metric=True)
def handler(event: dict, context: LambdaContext) -> Any:
    asgi_handler = Mangum(app)

    return asgi_handler(event, context)


if __name__ == "__main__":
    import os

    import uvicorn

    os.environ["AWS_SAM_LOCAL"] = "TRUE"
    os.environ["LOG_LEVEL"] = "DEBUG"
    uvicorn.run(
        "app.main:app", port=8080, log_level="debug", reload=True, access_log=False
    )
