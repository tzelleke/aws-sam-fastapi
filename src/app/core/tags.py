from enum import Enum


class Tags(Enum):
    ROOT = "Root"
    OPERATIONS = "Operations"


tags_metadata = [
    {"name": Tags.ROOT.value, "description": "Root"},
    {
        "name": Tags.OPERATIONS.value,
        "description": "Endpoints supporting operating and monitoring the application.",
    },
]
