from enum import Enum


class PrizePortion(str, Enum):
    FULL = "1"
    HALF = "1/2"
    THIRD = "1/3"
    QUARTER = "1/4"
