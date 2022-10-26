from enum import Enum, auto

class TravelStatus(Enum):
    FINE = auto(),
    ALREADY_PRESENT = auto(),
    DAY_OVER = auto(),

class AdvanceDayStatus(Enum):
    FINE = auto(),
    TOO_EARLY = auto(),