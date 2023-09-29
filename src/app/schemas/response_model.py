from typing import (
    Generic,
    TypedDict,
    TypeVar,
)

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class ResponseModel(GenericModel, Generic[DataT]):
    records: list[DataT]
    meta: TypedDict("Meta", {"count": int})
