from functools import lru_cache
import os
from pathlib import Path

from pydantic import (
    BaseSettings,
    Field,
)

# See: https://hindenes.com/testing-fastapi-basesettings
ENABLE_SETTINGS_CACHE = os.getenv("ENABLE_SETTINGS_CACHE", "TRUE").lower() == "true"


class Settings(BaseSettings):
    app_name: str = "FastAPI AWS SAM"
    version: str = "0.1.0"
    log_level: str = Field(default="INFO")
    root_path: str = Field(default="/Prod")
    frontend_dir: Path = Field(default=Path(__file__).parent.parent.parent / "frontend")
    aws_sam_local: bool = Field(default=False)

    def __init__(self, **data) -> None:
        super().__init__(**data)

        if self.aws_sam_local:
            self.root_path = ""


@lru_cache
def get_cached_settings() -> Settings:
    return Settings()


def get_settings() -> Settings:
    if ENABLE_SETTINGS_CACHE:
        return get_cached_settings()
    return Settings()
