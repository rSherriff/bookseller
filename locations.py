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

class SubLocation:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

class ClientSubLocation(SubLocation):
    def __init__(self, name, type, client_id) -> None:
        super().__init__(name, type)
        self.client_id = client_id

location_manager = {
            "Client": Location("Client", {"Client":ClientSubLocation("Client", LocationType.CLIENT, ClientIDs.CLIENT_A)}),
            "Bloomsbury": Location("Bloomsbury", {"skoob":SubLocation("Skoob", LocationType.SHOP)}),
            "Home": Location("Home", {"Home":SubLocation("Home", LocationType.HOME)})
        }