from enum import Enum
from mimetypes import init

class LocationType(Enum):
    CLIENT = 0,
    SHOP = 1

class Location:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

class LocationManager():
    def __init__(self) -> None:
        self.locations = {
            "client": Location("Client", LocationType.CLIENT),
            "bloomsbury": Location("skoob", LocationType.SHOP),
        }