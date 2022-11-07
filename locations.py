from difflib import get_close_matches
from enum import Enum

from utils.definitions import ClientIDs, PeopleIDs


class LocationType(Enum):
    CLIENT = 0,
    SHOP = 1,
    HOME = 2,
    PERSON = 3,

class Location:
    def __init__(self, name, sublocations, desc) -> None:
        self.name = name
        self.sublocations = sublocations
        self.desc = desc

    def search_sub_locations(self, search_term):
        return get_close_matches(search_term, self.sublocations.keys())


class SubLocation:
    def __init__(self, name, type, hidden = False) -> None:
        self.name = name
        self.type = type
        self.hidden = hidden

class ClientSubLocation(SubLocation):
    def __init__(self, name, type, client_id, hidden = False) -> None:
        super().__init__(name, type, hidden)
        self.client_id = client_id

class PersonSubLocation(SubLocation):
    def __init__(self, name, type, person_id, hidden = False) -> None:
        super().__init__(name, type, hidden)
        self.person_id = person_id

location_manager = {
            "Chelsea": Location("Chelsea", {"Client":ClientSubLocation("Client", LocationType.CLIENT, ClientIDs.CLIENT_A)}, "Here is the description of this area. It will probably be rather long and extend across multiple lines. Three sentences would hopefully be enough."),
            "Bloomsbury": Location("Bloomsbury", {"skoob":SubLocation("Skoob", LocationType.SHOP), "hidden_shop":PersonSubLocation("hidden_shop", LocationType.PERSON, PeopleIDs.PERSON_A, True)},"Here is the description of this area. It will probably be rather long and extend across multiple lines. Three sentences would hopefully be enough."),
            "Southwark": Location("Southwark", {"Home":SubLocation("Home", LocationType.HOME)},"Here is the description of this area. It will probably be rather long and extend across multiple lines. Three sentences would hopefully be enough.")
        }
