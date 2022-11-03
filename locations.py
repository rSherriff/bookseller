from difflib import get_close_matches
from enum import Enum
from mimetypes import init

from utils.definitions import ClientIDs


class LocationType(Enum):
    CLIENT = 0,
    SHOP = 1,
    HOME = 2

class Location:
    def __init__(self, name, sublocations) -> None:
        self.name = name
        self.sublocations = sublocations

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

location_manager = {
            "Client": Location("Client", {"Client":ClientSubLocation("Client", LocationType.CLIENT, ClientIDs.CLIENT_A)}),
            "Bloomsbury": Location("Bloomsbury", {"skoob":SubLocation("Skoob", LocationType.SHOP), "hiden_shop":SubLocation("hidden_shop", LocationType.SHOP, True)}),
            "Home": Location("Home", {"Home":SubLocation("Home", LocationType.HOME)})
        }
