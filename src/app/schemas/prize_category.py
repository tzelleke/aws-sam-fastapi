from enum import Enum


class PrizeCategory(str, Enum):
    PHYSICS = "Physics"
    CHEMISTRY = "Chemistry"
    PHYSIOLOGY_OR_MEDICINE = "Physiology or Medicine"
    PEACE = "Peace"
    LITERATURE = "Literature"
    ECONOMIC_SCIENCES = "Economic Sciences"
