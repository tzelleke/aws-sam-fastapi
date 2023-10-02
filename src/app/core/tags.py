from enum import Enum


class Tags(Enum):
    OPERATIONS = "Operations"


tags_metadata = [
    {
        "name": Tags.OPERATIONS.value,
        "description": "Endpoints supporting operating and monitoring the application.",
    },
]
