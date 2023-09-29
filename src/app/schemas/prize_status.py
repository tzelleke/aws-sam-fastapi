from enum import Enum


class PrizeStatus(str, Enum):
    DECLINED = "declined"
    RECEIVED = "received"
    RESTRICTED = "restricted"
