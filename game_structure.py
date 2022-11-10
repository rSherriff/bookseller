
from enum import Enum, auto
from locations import LocationType
from utils.definitions import StoryTriggerType, ClientIDs, PeopleIDs

client_status = {
    ClientIDs.CLIENT_A: []
}

story_segments = {
    "start":{
        "nextSegment" : "chapter1title"
    },
    "chapter1title":{
        "title" : "chapter1title",
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.NONE,
        "text": "Chapter 1: April 1983",
        "nextSegment" : "seg1"
    },
    "seg1":{
        "title" : "seg1",
        "requests_unlocked": {ClientIDs.CLIENT_A:["testReq"]},
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.NONE,
        "text": "Travel to the client in Chelsea.",
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
            "Get me a copy of 'I Am Error'#pause=1.7#\n\nThen do whatever",
        "solution":"1"
    }
}

person_convos = {
    PeopleIDs.PERSON_A:{
        "testReq":
        {
        "text": "Here is some convo test dialog!"
        }
    }
}

