from pydantic import root_validator
from pydash import get as pydash_get

from ..base_model import BaseModel


class NobelLaureateBase(BaseModel):
    id: int
    name: str

    @root_validator(pre=True)
    def parse_api_response(cls, values) -> dict:
        if "knownName" in values:
            values["name"] = pydash_get(values, "knownName.en")
        elif "orgName" in values:
            values["name"] = pydash_get(values, "orgName.en")

        return super().parse_api_response(values)
