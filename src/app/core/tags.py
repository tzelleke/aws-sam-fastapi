from enum import Enum


class Tags(Enum):
    NOBEL_PRIZES = "Nobel Prizes"
    NOBEL_LAUREATES = "Nobel Laureates"
    OPERATIONS = "Operations"


tags_metadata = [
    {
        "name": Tags.NOBEL_PRIZES.value,
        "description": "Obtain information about Nobel Prizes.",
    },
    {
        "name": Tags.NOBEL_LAUREATES.value,
        "description": "Obtain information about Nobel Laureates.",
    },
    {
        "name": Tags.OPERATIONS.value,
        "description": "Endpoints supporting operating and monitoring the application.",
    },
]
