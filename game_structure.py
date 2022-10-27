
from enum import Enum, auto
from locations import LocationType

class StoryTriggerType(Enum):
    NONE = auto()
    REQUEST_NEEDED = auto()


storySegments = {
    "start":{
        "nextSegment" : "seg1"
    },
    "seg1":{
        "title" : "seg1",
        "requests_unlocked": [1],
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.NONE,
        "text": "Here is a story segment!",
        "nextSegment" : "seg2"
    },
    "seg2":{
        "title" : "seg2",
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.NONE,
        "text": "Here is a second story segment!",
        "nextSegment" : None
    }
}

requests = {
    "1":{
        "text":[
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
            ],
        "book":1
    }
}

