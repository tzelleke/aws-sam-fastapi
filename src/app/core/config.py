from functools import lru_cache

from pydantic import (
    BaseSettings,
    Field,
)


class Settings(BaseSettings):
    app_name: str = "FastAPI AWS SAM"
    version: str = "0.1.0"
    log_level: str = Field(default="INFO")
    root_path: str = Field(default="/Prod")
    aws_sam_local: bool = Field(default=False)

    def __init__(self, **data) -> None:
        super().__init__(**data)

        if self.aws_sam_local:
            self.root_path = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
