
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
        "nextSegment" : "rosaseg1"
    },
    "rosaseg1":{
        "title" : "rosaseg1",
        "requests_unlocked": {ClientIDs.CLIENT_A:["rosacrucian"]},
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.NONE,
        "text": "Travel to the client in Chelsea.",
        "nextSegment" : "rosaseg2"
    },
    "rosaseg2":{
        "title" : "seg2",
        "requestsNeeded": ["rosacrucian"],
        "location": LocationType.HOME,
        "trigger": StoryTriggerType.REQUEST_NEEDED,
        "text": "You got the book and returned home!",
        "nextSegment" : None
    }
}

requests = {
    "rosacrucian":{
        "id":"rosacrucian",
        "text":
            "There is a certain Rosacrucian work I am looking to get my hands on.#pause=1.5#\n\nDennis, the dealer in Bloomsbury, has apparently just had some works delivered in lieu of some debt repayments from a German lawyer.#pause=1#\n\nI suspect they orignally came from Untermensch,#pause=0.5# he used to boast of having the only surviving edition of this supposed Rosacrucian work.#pause=0.5#\n\nGo to Dennis and take a look at the books, and find me that Rosacrucian work.#pause=0.5#Look them up at the museum if you're not familiar.",
        "solution":"rosacrucian",
        "books":{"Segap":["1","2","3","5","6","rosacrucian"]}
    }
}

person_convos = {
    PeopleIDs.DENNIS:{
        "rosacrucian":
        {
        "text": "Rosacrucian works?#pause=0.5# We just had some German works in from the Untermensch estate, but they've already gone out.#pause=1.7#\n\nSegap Books in Covent Garden took them.\n\nThere was nothing later than the end of the thirty years war in either of them, that's why they were so interesting, German publishing was quiet around then of course."
        }
    }
}

musuem_info = {
    "rosacrucians":"A purported 17th century society of learned men who promised to reveal the hitherto hidden order of the world. Headed by the mythical Christian Rosencrantz. All published works originate in Strasbourg.",
    "thirtyyearswar":"A large-scale European war lasting from 1618-1648",
    "strasbourg":"A French city in the large border region of Alsace. Home of the parliamentary pillar of the EEC. Famous for its large gothic cathedral with an octagonal tower."
}

