from typing import ClassVar

from pydantic import (
    BaseModel as PydanticBaseModel,
)
from pydantic import (
    root_validator,
)
from pydash import py_


class BaseModel(PydanticBaseModel):
    api_response_mapping: ClassVar[dict[str, str]] = {}

    @root_validator(pre=True)
    def parse_api_response(cls, values) -> dict:
        for model_key, response_path in cls.api_response_mapping.items():
            if py_.has(values, response_path):
                values[model_key] = py_.get(values, response_path)

        return values
