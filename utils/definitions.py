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
    REQUEST_NOT_COMPLETED = auto(),
    AT_END = auto()

class StorySegmentWaiting(Enum):
    NONE = auto(),
    HOME = auto(),
    SHOP = auto(),
    CLIENT = auto()

class StoryTriggerType(Enum):
    NONE = auto()
    REQUEST_NEEDED = auto()

class ClientIDs(Enum):
    CLIENT_A = auto()

class PeopleIDs(Enum):
    PERSON_A = auto()