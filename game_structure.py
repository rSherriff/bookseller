
from enum import Enum, auto
from locations import LocationType
from utils.definitions import StoryTriggerType, ClientIDs

client_status = {
    ClientIDs.CLIENT_A: []
}

story_segments = {
    "start":{
        "nextSegment" : "seg1"
    },
    "seg1":{
        "title" : "seg1",
        "requests_unlocked": {ClientIDs.CLIENT_A:["testReq"]},
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.NONE,
        "text": "Travel to the client!",
        "nextSegment" : "seg2"
    },
    "seg2":{
        "title" : "seg2",
        "requestsNeeded": ["testReq"],
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.REQUEST_NEEDED,
        "text": "You got the book and returned home!",
        "nextSegment" : None
    }
}

requests = {
    "testReq":{
        "id":"testReq",
        "text":
            "Get me a copy of 'I Am Error'",
        "solution":"1"
    }
}

