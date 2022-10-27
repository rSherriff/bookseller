from enum import Enum, auto

class TravelStatus(Enum):
    FINE = auto(),
    ALREADY_PRESENT = auto(),
    DAY_OVER = auto(),

class AdvanceDayStatus(Enum):
    FINE = auto(),
    TOO_EARLY = auto(),

class AdvanceStoryStatus(Enum):
    FINE = auto()
    REQUEST_NOT_COMPLETED = auto()

class StorySegmentWaiting(Enum):
    NONE = auto(),
    HOME = auto(),
    SHOP = auto(),
    CLIENT = auto()