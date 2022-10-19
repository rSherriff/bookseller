from enum import Enum
from mimetypes import init

class LocationType(Enum):
    CLIENT = 0,
    SHOP = 1,
    HOME = 2

class Location:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

location_manager = {
            "client": Location("Client", LocationType.CLIENT),
            "bloomsbury": Location("Skoob", LocationType.SHOP),
            "home": Location("Home", LocationType.HOME),
        }