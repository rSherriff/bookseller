from enum import Enum
from mimetypes import init

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

location_manager = {
            "Client": Location("Client", {"Client":SubLocation("Client", LocationType.CLIENT)}),
            "Bloomsbury": Location("Bloomsbury", {"skoob":SubLocation("Skoob", LocationType.SHOP)}),
            "Home": Location("Home", {"Home":SubLocation("Home", LocationType.HOME)})
        }